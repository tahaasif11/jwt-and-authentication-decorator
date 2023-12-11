from flask import request
import jwt
import config
import models.user_model as user_model
from functools import wraps
from utilities.helper import success_response
from datetime import datetime, timedelta


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            message = "Authentication Token is missing!"
            return success_response(False, message)
        try:
            data = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])

            current_user = user_model.find_user_by_email(data['user']['email'])
            if current_user is None:
                message = "User not found!"
                return success_response(False, message)

        except Exception as e:
            message = str(e)
            return success_response(False, message)

        return f(*args, **kwargs)

    return decorated


# Login API
def login():
    if request.method == "POST":
        data = request.get_json()

        user = user_model.login(data)

        if user:
            try:
                expires_delta = timedelta(minutes=15)
                expiration_time = datetime.utcnow() + expires_delta

                token = jwt.encode(
                    {"user": user, "exp": expiration_time},
                    config.SECRET_KEY,
                    algorithm="HS256"
                )
                message = "Successfully fetched auth token"
                return success_response(True, message, token)
            except Exception as e:
                message = str(e)
                return success_response(False, message)
        else:
            message = "Invalid email or password"
            return success_response(False, message)


@token_required
def get_all_furniture():
    if request.method == "GET":
        fornitures = user_model.get_all_furniture()
        message = "Successfully get data"
        return success_response(True,message,fornitures)


@token_required
def create_furniture():
    if request.method == "POST":
        data = request.get_json()
        user_model.insert_forniture(data)
        message = "Successfully created data"
        return success_response(True,message)
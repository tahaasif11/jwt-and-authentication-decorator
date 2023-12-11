import pymysql
from flask import jsonify
import config


def openDbconnection():
  try:
    connection = pymysql.connect(host='localhost', user=config.username, passwd=config.password, db=config.data_base)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    return connection, cursor

  except Exception as e:
    print(e)
    return False


connection, cursor = openDbconnection()


def success_response(success, message, data=None):
  response = {
    'success': success,
    'message': message,
  }

  if data is not None:
    response['resp_data'] = data

  return jsonify(response)
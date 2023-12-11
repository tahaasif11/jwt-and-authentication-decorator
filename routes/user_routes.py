from flask import Blueprint
from controllers import user_controller
form_bp = Blueprint("form_bp", __name__)

# routes
form_bp.route('/login', methods=['POST'])(user_controller.login)
form_bp.route('/get_all_furniture', methods=['GET'])(user_controller.get_all_furniture)
form_bp.route('/create_furniture', methods=['POST'])(user_controller.create_furniture)
__author__ = 'tauren'

from flask import Blueprint, json, jsonify, request, abort
from models import User, db
from flask_login import LoginManager, login_user
from itsdangerous import URLSafeTimedSerializer


auth_api = Blueprint('auth_api', __name__)
login_manager = LoginManager()
login_serializer = URLSafeTimedSerializer('SECRET KEY')


@login_manager.request_loader
def load_user_from_request(request):
    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = load_token(api_key)
        if user:
            return user
    return None


@login_manager.token_loader
def load_token(token):
    data = login_serializer.loads(token)
    user = User.query.filter_by(id=data[0]).first()
    if user and data[1] == user.password_hash:
        return user
    return None


@auth_api.route('/access_token', methods=['POST'])
def access_token():
    """
    Token Based Auth
    User submits a username+password and the server generates a api access token.
    """
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        abort(400)

    user_record = User.query.filter_by(username=username).first()
    if user_record is None:
        abort(400)

    if user_record.verify_password(password):
        access_token = user_record.get_auth_token()
        return jsonify({'access_token': access_token, 'username': 'test'}), 201
    abort(400)

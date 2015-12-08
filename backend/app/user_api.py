__author__ = 'tauren'

from flask import abort
from flask_restful import Resource
from flask.ext.restful import fields, marshal, reqparse
from flask_login import current_user
from models import User, db

user_fields = {
        'username': fields.String,
        'id': fields.Integer,
        'uri': fields.Url('user')
}


class UserApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided', location='json')
        super(UserApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        new_user = User(args['username'], args['password'])
        db.session.add(new_user)
        db.session.commit()
        return 201

    def get(self):
        user = User.query.filter_by(id=current_user.id).all()
        if not user:
            return abort(404)
        return {'results': marshal(user, user_fields)}

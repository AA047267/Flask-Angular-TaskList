__author__ = 'tauren'

from flask import abort
from flask_restful import Resource
from flask.ext.restful import fields, marshal, reqparse
from flask_login import current_user
from models import Task, db

task_fields = {
        'title': fields.String,
        'user_id': fields.Integer,
        'uri': fields.Url('task')
}


class TaskListApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        super(TaskListApi, self).__init__()

    def get(self):
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        if not tasks:
            return abort(404)
        return {'results': marshal(tasks, task_fields)}

    def post(self):
        args = self.reqparse.parse_args()
        task = Task(current_user.id, args['title'])
        db.session.add(task)
        db.session.commit()


class TaskApi(Resource):

    def get(self, id):
        task = Task.query.filter_by(id=id, user_id=current_user.id).first()
        if not task:
            return abort(404)
        return {'results': marshal(task, task_fields)}


__author__ = 'tauren'

from flask import Flask
from flask_restful import Api
from flask_login import login_required


def create_app(config_file):

    application = Flask(__name__)
    application.config.from_pyfile(config_file)

    from models import db, Task, User
    from auth import auth_api, login_manager
    from task_api import TaskListApi, TaskApi
    from user_api import UserApi

    db.init_app(application)
    login_manager.init_app(application)

    application.register_blueprint(auth_api, url_prefix='/api/auth')

    api = Api(application, decorators=[login_required])
    api.add_resource(TaskListApi, '/api/tasks', endpoint='tasks')
    api.add_resource(TaskApi, '/api/tasks/<int:id>', endpoint='task')
    api.add_resource(UserApi, '/api/users', endpoint='user')

    return application
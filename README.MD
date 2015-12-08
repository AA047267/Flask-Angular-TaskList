# Task List Backend

## Angular App

## REST API
### Authentication
Get an access token for the API:

    POST localhost:8000/api/auth/access_token {'username':'name', 'password':'pw'}
    
Create a new user:

    POST localhost:8000/api/users {'username':'x', 'password':'pw'}
    
### Endpoints
Get all tasks:

    GET localhost:8000/api/tasks?api_key=x

Get a particular task:
    
    GET localhost:8000/api/tasks/<task id>?api_key=x

Create a task:

    POST localhost:8000/api/tasks?api_key=x {'title':'name of task'}

TODO:
Update a task
Delete a task
Update user username/password
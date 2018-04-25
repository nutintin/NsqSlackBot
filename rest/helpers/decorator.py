from flask import current_app, request

from functools import wraps
# from flask_jwt import current_identity
# from .helper import mongo

from rest.exceptions import BadRequest


def _validate_app_secret_key():

    secret_key = request.headers.get('X-Api-Key', None)

    if not secret_key == current_app.config['APP_SECRET_KEY']:
        raise BadRequest("Forbidden Access", 403, 1)


# def _validate_admin():

#     is_admin = mongo.db.user.find_one({"_id": current_identity.id}, {"is_admin": 1,"is_active": 1, "_id": 0})

#     try:
#         is_active_status = is_admin['is_active']
#         is_admin_status = is_admin['is_admin']
#     except Exception:
#         raise BadRequest("User doesn't have permissions to take this actions", 
#                          200, 1)

#     if not is_admin_status or not is_active_status:
#         raise BadRequest("User doesn't have permissions to take this actions", 
#                          200, 1)


def _validate_nsq():
    print(request.form)
    is_token_valid = request.form['token'] == current_app.config['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == current_app.config['SLACK_TEAM_ID']
    print(request.form)
    if not is_token_valid or not is_team_id_valid:
        raise BadRequest("User doesn't have permissions to take this actions")


def secret_key_required():
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            _validate_app_secret_key()
            return func(*args, **kwargs)
        return decorator
    return wrapper


# def admin_required():
#     def wrapper(func):
#         @wraps(func)
#         def decorator(*args, **kwargs):
#             _validate_admin()
#             return func(*args, **kwargs)
#         return decorator
#     return wrapper


def nsq_required():
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            _validate_nsq()
            return func(*args, **kwargs)
        return decorator
    return wrapper
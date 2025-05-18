from flask import Blueprint, request
from app import db
from app.models.user import User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return {'username': user.username, 'email': user.email}, 200
    return {'message': 'User not found'}, 404

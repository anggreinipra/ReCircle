from flask import Blueprint, request, jsonify
from app import db
from app.models.blog import Blog
from flask_jwt_extended import jwt_required

bp = Blueprint('blogs', __name__, url_prefix='/blogs')

@bp.route('', methods=['POST'])
@jwt_required()
def create_blog():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')

    if not title or not content or not author:
        return jsonify({'message': 'Title, content, and author are required'}), 400

    blog = Blog(title=title, content=content, author=author)
    db.session.add(blog)
    db.session.commit()

    return jsonify({'message': 'Blog created successfully', 'blog': blog.serialize()}), 201


@bp.route('', methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    return jsonify([blog.serialize() for blog in blogs]), 200


@bp.route('/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify({'message': 'Blog not found'}), 404
    return jsonify(blog.serialize()), 200


@bp.route('/<int:blog_id>', methods=['PUT'])
@jwt_required()
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify({'message': 'Blog not found'}), 404

    data = request.get_json()
    blog.title = data.get('title', blog.title)
    blog.content = data.get('content', blog.content)
    blog.author = data.get('author', blog.author)

    db.session.commit()
    return jsonify({'message': 'Blog updated', 'blog': blog.serialize()}), 200


@bp.route('/<int:blog_id>', methods=['DELETE'])
@jwt_required()
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify({'message': 'Blog not found'}), 404

    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog deleted successfully'}), 200

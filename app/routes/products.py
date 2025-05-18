from flask import Blueprint, request
from app import db
from app.models.product import Product

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return {'products': [product.name for product in products]}, 200

@bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return {'name': product.name, 'category': product.category, 'price': product.price}, 200
    return {'message': 'Product not found'}, 404

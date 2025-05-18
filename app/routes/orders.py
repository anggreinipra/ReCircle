from flask import Blueprint, request
from app import db
from app.models.order import Order

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        quantity=data['quantity'],
        user_id=data['user_id'],
        product_id=data['product_id'],
        total_price=data['quantity'] * data['price']
    )
    db.session.add(new_order)
    db.session.commit()
    return {'message': 'Order created successfully'}, 201

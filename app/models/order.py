from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    product = db.relationship('Product', backref='orders')
    user = db.relationship('User', backref='orders')

    def __repr__(self):
        return f"<Order {self.id} by {self.user.username}>"

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    is_zero_waste = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Product {self.name}>"

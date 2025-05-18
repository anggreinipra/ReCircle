from ..utils.auth import bp as auth_bp
from .users import bp as users_bp
from .products import bp as products_bp
from .orders import bp as orders_bp
from .blog import bp as blog_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(blog_bp)

from flask_cqlalchemy import CQLAlchemy

db = CQLAlchemy()


def init_app(app):
    db.init_app(app)
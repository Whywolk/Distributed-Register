from server_app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}')"

    def to_json(self):
        return {'id': self.id,
                'name': self.name,
                'password': self.password}

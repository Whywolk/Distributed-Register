from server_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}')"

    def to_json(self):
        return {'id': self.id,
                'uid': self.uid,
                'name': self.name,
                'password': self.password}


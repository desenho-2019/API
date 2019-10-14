from app import db

class user(db.Model):
    __tablename__ = 'user'

    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, name=None, email=None):
        self.name =name
        self.email =email
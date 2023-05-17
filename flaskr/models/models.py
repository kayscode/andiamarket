from ..database.db import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f" client({self.first_name},{self.last_name})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    sigle = db.Column(db.String(20))
    email = db.Column(db.String(50))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

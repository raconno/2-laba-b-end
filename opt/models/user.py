from opt.db import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    category = db.relationship("CategoryModel", back_populates="user")
    cost = db.relationship("CostModel", back_populates="user")

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(128), unique=True, nullable=False)

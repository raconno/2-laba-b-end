from sqlalchemy.sql import func
from opt.db import db


class CostModel(db.Model):
    __tablename__ = "cost"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), unique=False, nullable=False)
    description = db.Column(db.String(512), nullable=False)
    money = db.Column(db.Float(precision=2), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())

    category = db.relationship("CategoryModel", back_populates="cost")
    user = db.relationship("UserModel", back_populates="cost")
    currency = db.relationship("CurrencyModel", back_populates="cost")

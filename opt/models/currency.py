from opt.db import db


class CurrencyModel(db.Model):
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key=True)
    currency_symbol = db.Column(db.String(20), nullable=False)
    exchange_rate = db.Column(db.Float, nullable=False)

    cost = db.relationship("CostModel", back_populates="currency")

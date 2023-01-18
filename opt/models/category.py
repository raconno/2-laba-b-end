from opt.db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False)
    title = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)

    cost = db.relationship("CostModel", back_populates="category")
    user = db.relationship("UserModel", back_populates="category")

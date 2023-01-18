# import json
from logging import warning

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from opt.db import db
from opt.models import CategoryModel, CostModel
from opt.schemas import CategorySchema, CategoryQuerySchema

blp = Blueprint('category', __name__, description='requests for categories')


@blp.route("/category/<string:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def delete(self, category_id):  # delete by id
        try:
            category = CategoryModel.query.filter_by(id=category_id).all()[0]
        except IndexError:
            abort(400, message='No category with such id')

        try:
            costs = CostModel.query.filter_by(category_id=category_id).all()
            for cost in costs:
                db.session.delete(cost)
                db.session.commit()

            db.session.delete(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message='No category with such id')
        return category

    @blp.response(200, CategorySchema)
    def get(self, category_id):  # get by id
        return CategoryModel.query.get_or_404(category_id)


@blp.route("/category")
class CategoryList(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):  # create user
        # {"username": "<>", "email": "<>", "password": "<>"}
        user = CategoryModel(**category_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='Category with this title already exists'
            )
        return user

    @blp.arguments(CategoryQuerySchema, location='query', as_kwargs=True)
    @blp.response(200, CategorySchema(many=True))
    def get(self, **kwargs):  # get all categories
        user_id = kwargs.get('user_id')
        query = CategoryModel.query
        if user_id:
            query = query.filter(CategoryModel.user_id == user_id)
        return query.all()

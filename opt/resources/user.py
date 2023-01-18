import json
from logging import warning

from opt.db import db
from opt import app, entities
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify, render_template, session, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from opt.models import CostModel, CategoryModel
from opt.models.user import UserModel
from opt.schemas import UserSchema

blp = Blueprint('user', __name__, description='requests for users')


@blp.route("/")
class Init(MethodView):
    def get(self):
        return {"hi":"hello"}


@blp.route("/user")
class User(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):  # create user
        # {"username": "<>", "email": "<>", "password": "<>"}
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='User with this name already exists'
            )
        return user

    @blp.response(200, UserSchema(many=True))
    def get(self):  # get all
        return UserModel.query.all()


@blp.route("/user/<string:user_id>")
class User_args(MethodView):
    @blp.response(200, UserSchema)
    def delete(self, user_id):  # delete by id
        try:
            user = UserModel.query.filter_by(id=user_id).all()[0]
            warning(user.id)
        except IndexError:
            abort(400, message='No user with such id')
        try:
            costs = CostModel.query.filter_by(user_id=user_id).all()
            for cost in costs:
                db.session.delete(cost)
                db.session.commit()

            categories = CategoryModel.query.filter_by(user_id=user_id).all()
            for category in categories:
                db.session.delete(category)
                db.session.commit()

            db.session.delete(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Something goes wrong while deleting user')
        return user

    @blp.response(200, UserSchema)
    def get(self, user_id):  # get by id
        return UserModel.query.get_or_404(user_id)

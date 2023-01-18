# import json
from logging import warning

from sqlalchemy.exc import IntegrityError

from opt import app, entities
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify, render_template, session, request, redirect, url_for

from opt.db import db
from opt.models import CostModel
from opt.schemas import CostSchema, CostQuerySchema

blp = Blueprint('cost', __name__, description='requests for costs')


@blp.route("/cost")
class Category(MethodView):
    @blp.arguments(CostSchema)
    @blp.response(200, CostSchema)
    def post(self, cost_data):  # create category
        cost = CostModel(**cost_data)
        try:
            db.session.add(cost)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Error when creating cost')
        return cost

    @blp.arguments(CostQuerySchema, location='query', as_kwargs=True)
    @blp.response(200, CostSchema(many=True))
    def get(self, **kwargs):  # get all categories
        user_id = kwargs.get('user_id')
        if not user_id:
            return abort(400, message='Need at least user_id to get costs')
        query = CostModel.query.filter(CostModel.user_id==user_id)
        return query.all()


@blp.route("/cost/<string:cost_id>")
class Category(MethodView):
    @blp.response(200, CostSchema)
    def get(self, cost_id):  # get all categories
        return CostModel.query.get_or_404(cost_id)

    @blp.response(200, CostSchema)
    def delete(self, cost_id):
        try:
            cost = CostModel.query.filter_by(id=cost_id).all()[0]
        except IndexError:
            abort(400, message='No cost with such id')

        try:
            db.session.delete(cost)
            db.session.commit()
        except IntegrityError:
            abort(400, message='No cost with such id')
        return cost

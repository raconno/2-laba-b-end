import json
from logging import warning

from opt.db import db
from opt import app, entities
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify, render_template, session, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from opt.models import CostModel
from opt.models.currency import CurrencyModel
from opt.schemas import CurrencySchema

blp = Blueprint('currency', __name__, description='requests for currancies')


@blp.route("/currency")
class User(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):  # create currency
        # {"currencyname": "<>", "email": "<>", "password": "<>"}
        currency = CurrencyModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='Currency with this name already exists'
            )
        return currency

    @blp.response(200, CurrencySchema(many=True))
    def get(self):  # get all
        return CurrencyModel.query.all()


@blp.route("/currency/<string:currency_id>")
class Currency_args(MethodView):
    @blp.response(200, CurrencySchema)
    def delete(self, currency_id):  # delete by id
        try:
            currency = CurrencyModel.query.filter_by(id=currency_id).all()[0]
        except IndexError:
            abort(400, message='No currency with such id')
        try:
            costs = CostModel.query.filter_by(currency_id=currency_id).all()
            for cost in costs:
                db.session.delete(cost)
                db.session.commit()

            db.session.delete(currency)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Something goes wrong while deleting currency')
        return currency

    @blp.response(200, CurrencySchema)
    def get(self, currency_id):  # get by id
        return CurrencyModel.query.get_or_404(currency_id)

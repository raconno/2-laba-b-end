from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str()


class CategoryQuerySchema(Schema):
    user_id = fields.Int()


class CostSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    currency_id = fields.Int(load_default=1)
    description = fields.Str()
    money = fields.Float(required=True)
    created_at = fields.Str(dump_only=True)


class CostQuerySchema(Schema):
    user_id = fields.Int()
    category_id = fields.Int()


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    currency_symbol = fields.Str(required=True)
    exchange_rate = fields.Float(required=True)

# import json
# from opt import app, entities
# from flask import request
# from flask_smorest import abort, Api
#
# from opt.resources.user import blp as UserBlueprint
# from opt.resources.category import blp as CategoryBlueprint
# from opt.resources.cost import blp as CostBlueprint
#
# app.config["PROPAGATE_EXCEPTIONS"] = True
# app.config["API_TITLE"] = "Finance REST API"
# app.config["API_VERSION"] = "v1"
# app.config["OPENAPI_VERSION"] = "3.8.3"
# app.config["OPENAPI_URL_PREFIX"] = "/"
# app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
#
#
# api = Api(app)
#
# api.register_blueprint(UserBlueprint)
# api.register_blueprint(CategoryBlueprint)
# api.register_blueprint(CostBlueprint)
#
# #
# # @app.post('/create_user')  # {"username": "<>", "email": "<>", "password": "<>"}
# # def create_user():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         username = req['username']
# #         email = req['email']
# #         password = req['password']
# #     except KeyError:
# #         abort(400, message='user data is not found. must be specified "username", "email" and "password".')
# #     result = repo.create_user(username, email, password)
# #     return json.dumps(result)
# #
# #
# # @app.route("/create_category", methods=['POST'])  # {"user_id": "<>", "title": "<>", "description": "<>"}
# # def create_category():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         title = req['title']
# #         description = req['description']
# #     except KeyError:
# #         abort(400, message='user data is not found. must be specified "user_id", "title" and "description".')
# #     result = repo.create_category(user_id, title, description)
# #     return json.dumps(result)
# #
# #
# # @app.route("/get_category", methods=['POST'])  # {"user_id": "<>", "category_id": "<>"} !!!!!CHANGE
# # def category():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id" and "category_id".')
# #
# #     try:
# #         user = repo.USERS[user_id]
# #     except KeyError:
# #         abort(400, message='no user with such id.')
# #
# #     data = user.get_category_by_id(category_id)
# #     return json.dumps(data)
# #
# #
# # @app.route("/update_category", methods=['PATCH'])  # {"user_id": "<>", "category_id": "<>", "title"/"description"}
# # def update_category():
# #     repository = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id" and "category_id".')
# #     title = req.get('title')
# #     description = req.get('description')
# #     result = repository.update_category(user_id, category_id, title, description)
# #     return json.dumps(result)
# #
# #
# # @app.route("/delete_category", methods=['DELETE'])  # {"user_id": "<>", "category_id": "<>"}
# # def delete_category():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id" and "category_id".')
# #     result = repo.delete_category(user_id, category_id)
# #     return json.dumps(result)
# #
# #
# # @app.route("/create_cost", methods=['POST'])  # {"user_id": "<>", "category_id": "<>", "description": "<>", "money":
# # # "<>"}
# # def create_cost():
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #         description = req['description']
# #         money = req['money']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id", "category_id", "description" and "money".')
# #
# #     repository = entities.get_repo()
# #     result = repository.create_cost(user_id, category_id, description, money)
# #     return json.dumps(result)
# #
# #
# # @app.route("/get_cost", methods=['POST'])  # {"user_id": "<>", "category_id": "<>", "cost_id": "<>"}
# # def cost():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #         cost_id = req['cost_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id", "category_id" and "cost_id".')
# #
# #     result = repo.get_cost(user_id, category_id, cost_id)
# #     return json.dumps(result)
# #
# #
# # @app.route("/get_all_costs")  # {"user_id": "<>"}
# # def get_all_costs():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id".')
# #
# #     all_costs = repo.get_all_costs(user_id)
# #     return json.dumps(all_costs)
# #
# #
# # @app.route("/delete_cost", methods=['DELETE'])  # {"user_id": "<>", "category_id": "<>", "cost_id": "<>"}
# # def delete_cost():
# #     repo = entities.get_repo()
# #     req = request.args.to_dict()
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #         cost_id = req['cost_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id", "category_id" and "cost_id".')
# #
# #     result = repo.delete_cost(user_id, category_id, cost_id)
# #     return json.dumps(result)
# #
# #
# # @app.route("/update_cost", methods=['POST'])  # {"user_id": "<>", "category_id": "<>", "cost_id": "<>",
# # # "money"/"description"}
# # def update_cost():
# #     req = request.args.to_dict()
# #     money = req.get('money')
# #     description = req.get('description')
# #     try:
# #         user_id = req['user_id']
# #         category_id = req['category_id']
# #         cost_id = req['cost_id']
# #     except KeyError:
# #         abort(400, message='must be specified "user_id", "category_id" and "cost_id".')
# #
# #     repository = entities.get_repo()
# #     result = repository.update_cost(user_id, category_id, cost_id, money, description)
# #     print("cost_id " + cost_id)
# #     print("money " + money)
# #     print("description " + description)
# #     return json.dumps(result)

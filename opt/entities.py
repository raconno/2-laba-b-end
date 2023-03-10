# from datetime import datetime
# from lab import exceptions
# from collections import defaultdict
# from flask import session
# from flask_smorest import abort


repo = None

# def get_repo():
#     global repo
#     if repo is None:
#         session.clear()
#         repo = Repository()
#     #     user1 = repo.USERS[repo.create_user("11", "11", "11")]
#     #     user2 = repo.USERS[repo.create_user("22", "22", "22")]
#     #     user3 = repo.USERS[repo.create_user("33", "33", "33")]
#     #     user4 = repo.USERS[repo.create_user("44", "44", "44")]
#     #     user5 = repo.USERS[repo.create_user("55", "55", "55")]
#     #
#     #     categ_id = user1.create_category("category1", "for user 1")
#     #     user1.create_category("category2", "for user 1")
#     #     user1.create_category("category3", "for user 1")
#     #
#     #     user2.create_category("category1", "for user 2")
#     #     user2.create_category("category2", "for user 2")
#     #     user2.create_category("category3", "for user 2")
#     #
#     #     user3.create_category("category1", "for user 3")
#     #     user3.create_category("category2", "for user 3")
#     #     user3.create_category("category3", "for user 3")
#     #
#     #     user4.create_category("category1", "for user 4")
#     #     user4.create_category("category2", "for user 4")
#     #     user4.create_category("category3", "for user 4")
#     #
#     #     user5.create_category("category1", "for user 5")
#     #     user5.create_category("category2", "for user 5")
#     #     user5.create_category("category3", "for user 5")
#     #
#     #     user1.create_cost(categ_id, "argreg", 10.3)
#     #     user1.create_cost(categ_id, "fgds", 15)
#     #     user1.create_cost(categ_id, "hser", 22)
#     return repo
#
#
# class Repository:
#     USER_ID = 1
#     USERS = {}
#
#     def check_user_id(self, user_id):
#         if user_id not in self.USERS.keys():
#             abort(404, message='no user with such id.')
#
#     def check_category_id(self, user_id, category_id):
#         if category_id not in self.USERS[user_id].CATEGORIES.keys():
#             abort(404, message='such user has no such category.')
#
#     def check_cost_id(self, user_id, category_id, cost_id):
#         if cost_id not in self.USERS[user_id].COSTS[cost_id].keys():
#             abort(404, message='such user has no such cost in such category')
#
#     def create_user(self, username, email, password):
#         for _, user in self.USERS.items():
#             if user.username.title() == username:
#                 abort(404, message='choose another username.')
#             if user.email.lower() == email:
#                 abort(404, message='account with such email is already exists.')
#
#         new_user = User(username.title(), email.lower(), password)
#         self.USERS[str(self.USER_ID)] = new_user
#         self.USER_ID += 1
#         return {"user_id": self.USER_ID - 1}
#
#     def delete_user(self, user_id):
#         try:
#             deleted_user = self.USERS[str(user_id)]
#             del self.USERS[str(user_id)]
#             return deleted_user
#         except KeyError:
#      # def log_in(self, nick, password):
#     #     for id, user in self.USERS.items():
#     #         if user.email.lower() == nick or user.username.title() == nick:
#     #             if user.password == password:
#     #                 return id
#     #             else:
#     #                 raise Exception("Wrong password!")
#     #     raise Exception("Wrong email or username.")
#
#     def create_category(self, user_id, title, description):
#         self.check_user_id(user_id)
#
#         for _, category in self.USERS[user_id].CATEGORIES.items():
#             if category.title == title:
#                 abort(404, message='choose another title.')
#         category_id = self.USERS[user_id].create_category(title, description)
#         return {"category_id": category_id}
#
#     def delete_category(self, user_id, category_id):
#         self.check_user_id(user_id)
#         self.check_category_id(user_id, category_id)
#
#         self.USERS[user_id].delete_category(category_id)
#         return {'status': True}
#
#     def update_category(self, user_id, category_id, title, description):
#         self.check_user_id(user_id)
#         self.check_category_id(user_id, category_id)
#
#         for _, category in self.USERS[user_id].CATEGORIES.items():
#             if category.title == title:
#                 abort(404, message='choose another title')
#
#         return self.USERS[user_id].update_category(category_id, title, description)
#
#     def get_all_costs(self, user_id):
#         self.check_user_id(user_id)
#
#         all = []
#         for category_id in self.USERS[user_id].CATEGORIES.keys():
#             all.append(self.USERS[user_id].get_category_by_id(category_id))
#         return all
#
#     def get_cost(self, user_id, category_id, cost_id):
#         self.check_user_id(user_id)
#         self.check_category_id(user_id, category_id)
#         self.check_cost_id(user_id, category_id, cost_id)
#
#         return self.USERS[user_id].get_cost_by_id(cost_id)
#
#     def delete_cost(self, user_id, category_id, cost_id):
#         self.check_user_id(user_id)
#         self.check_category_id(user_id, category_id)
#         self.check_cost_id(user_id, category_id, cost_id)
#
#         return self.USERS[user_id].delete_cost(cost_id)
#
#     def update_cost(self, user_id, category_id, cost_id, money, description):
#         if self.USERS[user_id].COSTS.get(str(cost_id)) is not None:
#             self.USERS[user_id].update_cost(cost_id, money, description)
#
#     def create_cost(self, user_id, category_id, description, money):
#         if user_id not in self.USERS.keys():
#             abort(404, message='no user with such id.')
#
#         if category_id not in self.USERS[user_id].CATEGORIES.keys():
#             abort(404, message='such user has no such category.')
#
#         return self.USERS[user_id].create_cost(category_id, description, money)
#
#
# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
#
#         self.CATEGORY_ID = 1
#         self.COST_ID = 1
#         self.CATEGORIES = {}
#         self.COSTS = {}
#
#     def create_category(self, title, description):
#         self.CATEGORIES[str(self.CATEGORY_ID)] = Category(title, description)
#         self.CATEGORY_ID += 1
#         return self.CATEGORY_ID - 1
#
#     def get_all_categories(self):
#         categories_dict = defaultdict(dict)
#         for id, category in self.CATEGORIES.items():
#             categories_dict[id] = {"title": category.title,
#                                    "description": category.description}
#         return categories_dict
#
#     def get_category_by_id(self, category_id):
#         if self.CATEGORIES.get(category_id) is None:
#             abort(404, message='such user has no such category.')
#         category = self.CATEGORIES[category_id]
#         return {"id": category_id,
#                 "title": category.title,
#                 "description": category.description,
#                 "costs": self.get_costs_in_category(category_id)}
#
#     def update_category(self, category_id, title, description):
#         if title:
#             self.CATEGORIES[category_id].title = title
#         if description:
#             self.CATEGORIES[category_id].description = description
#         return self.get_category_by_id(category_id)
#
#     def delete_category(self, category_id):
#         self.CATEGORIES.pop(category_id)
#         for cost_id in list(self.COSTS.keys()):
#             if self.COSTS[cost_id].category_id == category_id:
#                 self.COSTS.pop(cost_id)
#
#     def create_cost(self, category_id, description, money):
#         self.COSTS[str(self.COST_ID)] = Cost(str(category_id), description, str(money))
#         self.COST_ID += 1
#         return {"id": self.COST_ID - 1, "description": description, "money": money}
#
#     def get_cost_by_id(self, cost_id):
#         cost = self.COSTS.get(cost_id)
#         return {'id': cost_id,
#                 'description': cost.description,
#                 'money': cost.money,
#                 'creation_datetime': cost.creation_datetime}
#
#     def get_costs_in_category(self, category_id):
#         cost_list = []
#         for cost_id, cost in self.COSTS.items():
#             if cost.category_id == category_id:
#                 cost_list.append({"id": cost_id, "description": cost.description, "money": cost.money})
#         return cost_list
#
#     def update_cost(self, cost_id, money, description):
#         print("IN USER")
#         self.COSTS[str(cost_id)].money = str(money)
#         self.COSTS[str(cost_id)].description = description
#
#     def delete_cost(self, cost_id):
#         self.COSTS.pop(cost_id)
#         return {"status": True}
#
#
# class Category:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#
#
# class Cost:
#     def __init__(self, category_id, description, money):
#         self.category_id = category_id
#         self.creation_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         self.description = description
#         self.money = money

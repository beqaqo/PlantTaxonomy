from flask_restx import Resource, reqparse

from src.ext import dpi

@dpi.route("/api/users")
class UserApi(Resource):
    def get(self):
        return 'hellow world', 200
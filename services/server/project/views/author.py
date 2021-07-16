from flask import Blueprint
from flask_restful import Resource, Api

from project.models.author import Author

authors_blueprint = Blueprint("authors", __name__, url_prefix="/api")
api = Api(authors_blueprint)


class AuthorsList(Resource):
    @classmethod
    def get(cls):
        response_object = {}
        authors = [author.json() for author in Author.query.all()]
        response_object["data"] = authors
        response_object["status"] = "success"
        return response_object, 200


api.add_resource(AuthorsList, "/authors")

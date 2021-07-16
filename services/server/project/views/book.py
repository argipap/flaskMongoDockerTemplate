from flask import Blueprint
from flask_restful import Resource, Api

from project.models.book import Book

books_blueprint = Blueprint("books", __name__, url_prefix="/api")
api = Api(books_blueprint)


class BooksList(Resource):
    @classmethod
    def get(cls):
        response_object = {}
        books = [book.json() for book in Book.query.all()]
        response_object["data"] = books
        response_object["status"] = "success"
        return response_object, 200


api.add_resource(BooksList, "/books")

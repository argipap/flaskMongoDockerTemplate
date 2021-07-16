from project import db
from project.models.author import Author


class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()

    def __repr__(self):
        return f"{self.title}, {self.author.name}, {self.year}"

    def json(self):
        return {"book": self.__repr__()}

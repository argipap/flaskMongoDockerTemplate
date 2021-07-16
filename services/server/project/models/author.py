from project import db


class Author(db.Document):
    name = db.StringField()

    def __repr__(self):
        return f"{self.name}"

    def json(self):
        return {"author": self.__repr__()}

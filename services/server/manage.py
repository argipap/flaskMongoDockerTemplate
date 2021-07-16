import sys
import unittest
import coverage

from flask.cli import FlaskGroup
from project.models.author import Author 
from project.models.book import Book 

COV = coverage.coverage(
    branch=True, include="project/*", omit=["project/tests/*", "project/config.py"]
)
COV.start()

from project import create_app, db  # noqa:E402

app = create_app()
cli = FlaskGroup(create_app=create_app)


# @cli.command("recreate_db")
# def recreate_db():
#     db.drop_all()
#     db.create_all()
#     db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    mark_pilgrim = Author(name='Mark Pilgrim')
    dive = Book(title='Dive Into Python', author=mark_pilgrim, year=2004)
    mark_pilgrim.save()
    dive.save()


@cli.command("delete_all")
def delete_all():
    authors = [author for author in Author.query.all()]
    for author in authors:
        print(author)
        author.remove()


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == "__main__":
    cli()

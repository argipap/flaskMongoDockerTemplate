from flask_mongoalchemy import MongoAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# instantiate the db
db = MongoAlchemy()

# flask-cors for cross-origin requests
cors = CORS()

# flask-migration for database migrations
migrate = Migrate()

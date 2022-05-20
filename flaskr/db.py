from flask_sqlalchemy import SQLAlchemy
from app import app
from models.PetsModel import Pet
# setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ice:hello@localhost/pets'
db = SQLAlchemy(app)


# create tables
db.create_all()

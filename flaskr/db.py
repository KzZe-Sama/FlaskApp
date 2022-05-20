from flask_sqlalchemy import SQLAlchemy
# setup
def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ice:hello@localhost/pets'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    print("running")
    # create tables
    db.create_all()

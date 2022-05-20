from flask_sqlalchemy import SQLAlchemy
def db(app): 
    if app is not None:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ice:hello@localhost/pets'
        db = SQLAlchemy(app)
        return db
    return None
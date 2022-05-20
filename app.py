import imp
from flask import Flask,Blueprint
from flaskr.db import setup_db
from flaskr.routes.route import main

app = Flask(__name__)
app.register_blueprint(main)

# calling db
setup_db(app)
if __name__ == '__main__':
  app.run(debug=True)

# routes
from flaskr.routes import route
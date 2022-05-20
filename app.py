from flask import Flask
from flaskr.db import setup
app = Flask(__name__)


if __name__ == '__main__':
  app.run(debug=True)
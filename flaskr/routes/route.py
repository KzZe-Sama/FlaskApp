from flask import Blueprint,jsonify


main = Blueprint('main',__name__)

@main.route('/')
def main_index():
    return jsonify({"message":"List of pets"})
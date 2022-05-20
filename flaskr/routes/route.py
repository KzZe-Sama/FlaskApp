from flask import Blueprint,jsonify


main = Blueprint('main',__name__)

@cross-origin()
@main.route('/')
def main_index():
    return jsonify({"message":"List of pets"})
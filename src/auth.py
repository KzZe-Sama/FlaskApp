from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth.post("/register")
def register():
    return "User Registered"


@auth.get("/loadme")
def load_me():
    return {"user": "me"}

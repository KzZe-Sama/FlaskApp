from flask import Blueprint

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/bookmarks")


@bookmarks.get("/")
def get_all():
    return {"bookmarks": []}

from app import app
from app.blogs.blogs import Blogs
from flask import jsonify, request


@app.route("/create_blog", methods=["POST"])
def create_blog():
    try:
        data = request.get_json()
        response = Blogs().create_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


@app.route("/delete_blog", methods=["DELETE"])
def delete_blog():
    try:
        data = request.get_json()
        response = Blogs().delete_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


@app.route("/update_blog", methods=["PUT"])
def update_blog():
    try:
        data = request.get_json()
        response = Blogs().update_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})

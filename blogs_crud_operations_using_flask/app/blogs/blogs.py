from app.model.connect_to_db import ConnectDB
from flask import jsonify, request


class Blogs(object):
    def __init__(self):
        self.desc = "All Blogs Operations"
        self.collection_name = "blogs"

    def create_blog(self, data):
        try:
            blog_dict = {
                "title": data.get("title", ""),
                "description": data.get("description", ""),
            }

            ConnectDB().connect_db()[self.collection_name].insert_one(blog_dict)

            return {"status": "success", "message": "Blog created successfully"}
        except Exception as e:
            return {"status": "failure", "message": str(e)}

    def delete_blog(self, data):
        try:
            ConnectDB().connect_db()[self.collection_name].delete_one(
                {"_id": data.get("blog_id")}
            )

            return {"status": "success", "message": "Blog deleted successfully"}
        except Exception as e:
            return {"status": "failure", "message": str(e)}

    # def update_blog(self, data):
    #     try:
    #         ConnectDB().connect_db()[self.collection_name].update_one(
    #             {"_id": data.get("blog_id")},
    #             {
    #                 "$set": {
    #                     "title": data.get("title"),
    #                     "description": data.get("description"),
    #                 }
    #             },
    #         )
    #         return {"status": "success", "message": "Blog updated successfully"}
    #     except Exception as e:
    #         return {"status": "failure", "message": str(e)}

    def update_blog(self, data):
        try:
            blog_dict = {
                "title": data.get("title", ""),
                "description": data.get("description", ""),
            }
            ConnectDB().connect_db()[self.collection_name].update_one(
                {"_id": data.get("blog_id")}, {"$set": blog_dict}
            )
            return {"status": "success", "message": "Blog updated successfully"}
        except Exception as e:
            return {"status": "failure", "message": str(e)}

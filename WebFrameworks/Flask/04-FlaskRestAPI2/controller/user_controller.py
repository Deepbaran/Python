from app import app
from model.user_model import user_model
from flask import request
from datetime import datetime

obj = user_model()

@app.route("/users/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/users/addone", methods=["POST"])
def user_addone_controller():
    # request body is in request.form
    return obj.user_addone_model(request.form)

@app.route("/users/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route("/users/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/users/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(id, request.form)

@app.route("/users/getall-pagination", methods=["GET"])
def user_pagination_controller():
    # query parameter passed in request.args
    return obj.user_pagination_model(request.args)

@app.route("/users/<uid>/upload/avatar", methods=["PUT"])
def user_upload_avatar_controller(uid):
    # https://api.github.com/users
    file = request.files['avatar']
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "")
    fileExtension = str(file.filename).split(".")[-1]
    filename = f"{uniqueFileName}.{fileExtension}"
    filepath = f"uploads/avatar/{filename}"
    file.save(filepath)
    print(filepath)
    return obj.user_upload_avatar_model(uid, filepath)

@app.route("/uploads/avatar/<id>")
def user_get_avatar_controller(id):
    return obj.user_get_avatar_controller(id)
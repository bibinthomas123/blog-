from flask import Blueprint,render_template,request
from pymongo import MongoClient
from flask_ckeditor import CKEditorField




db = MongoClient("mongodb://127.0.0.1:27017/")

document = db["blog"]
posts = document["posts"]
users = document["users"]


views = Blueprint("views",__name__)


@views.route("/")
def home():
    all_data = posts.find({}).limit(10)
    return render_template("index.html",data=list(all_data))

@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/post")
def possts():

    # post = posts.find(post_id).limit(1)

    return render_template("single_post.html")

@views.route("/edit-posts")
def edit_posts():
    # body = CKEditorField("body")

    return render_template("post.html")

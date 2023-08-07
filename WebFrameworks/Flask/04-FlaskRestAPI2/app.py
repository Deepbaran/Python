from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def signup():
    return "This is home page"

# We are importing the controllers at the end, because we want them to be imported after app variable is defined
from controller import * # for 'import *' to work, we need to make sure that the directory is a package/module (add __init__.py file)
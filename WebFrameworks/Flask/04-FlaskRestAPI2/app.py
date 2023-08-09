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

if __name__ == "__main__":
    # If you do not wish to set environment variable as DEBUG, then pass debug=True here
    app.run(port=5000, debug=True)

"""
1. Make it a employee management application with SQLite/PostgreSQL/MySQL
2. Add Unit Testing and Test Coverage
3. Encrypt Password with base64
4. Use query parameter for some of the endpoints
5. add sanitation check of the data that is passed as parameters or payloads
6. improve the structure of the directories more (if possible-controllers,handler,services,DAO/DTO)
7. add more exceptions for different error codes
8. create frontend for this app (with unit tests and coverage)
9. create a 404 page 
10. Make sure to add pagination and API versioning
"""
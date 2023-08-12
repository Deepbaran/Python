from config import dbconfig
from functools import wraps
import mysql.connector
from flask import make_response, request
import jwt
import re
import json

class auth_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=dbconfig['hostname'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True) # Records received from the DB will be in dictionary format
            print("Connection Successful: auth_model")
        except:
            print("Some error: auth_model")

    def token_auth(self, endpoint=""):
        def inner1(func):
            @wraps(func) # This will handle the error -> AssertionError: View function mapping is overwriting an existing endpoint function: inner2
            def inner2(*args, **kwargs):
                endpoint = request.url_rule
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[-1]
                    try:
                        jwtdecoded = jwt.decode(token, key="Deep", algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR": "TOKEN_EXPIRED"}, 401)
                    role_id = jwtdecoded["payload"]["role_id"]
                    self.cur.execute(f"SELECT roles FROM accessibility_view WHERE endpoint='{endpoint}'")
                    result = self.cur.fetchall()
                    if result:
                        allowed_roles = json.loads(result[0]["roles"])
                        if role_id in allowed_roles:
                            return func(*args, **kwargs)
                        else:
                            return make_response({"ERROR": "INVALID_ROLE"}, 404)
                    else:
                        return make_response({"ERROR": "UNKNOWN_ENDPOINT"}, 404)
                else:
                    return make_response({"ERROR": "INVALID_TOKEN"}, 401)
            return inner2
        return inner1
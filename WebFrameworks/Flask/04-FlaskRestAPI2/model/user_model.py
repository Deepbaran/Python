import mysql.connector
import json
from flask import make_response

class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="12345678",database="flask_tutorial_1")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True) # Records received from the DB will be in dictionary format
            print("Connection Successful")
        except:
            print("Some error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0: 
            # We can return string and dictionary for json response
            # Serialize obj to a JSON formatted str.
            # content-type -> text/html
            # return json.dumps(result)

            # content-type -> application/json 
            # return {"payload":result}

            res = make_response({"payload":result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*" # Setting all CORS requests in the header
            return res
        else: 
            # return "No Data Found"
            return make_response({"message":"No Data Found"}, 204)
            # 204 is a status code that is such a status code where we do not need to send any response body. hence the body is not sent

    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        # self.con.commit() # As autocommit is enabled, we do not need to commit everytime
        # return "User Created Successfully"
        return make_response({"message":"User Created Successfully"}, 201)
    
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount > 0 : 
            # return "User Updated Successfully"
            return make_response({"message":"User Updated Successfully"}, 201)
        else: 
            # return "Nothing to Update"
            return make_response({"message":"Nothing to Update"}, 202)

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0 : 
            # return "User Deleted Successfully"
            return make_response({"message":"User Deleted Successfully"}, 200)
        else: 
            # return "Nothing to Delete"
            return make_response({"message":"Nothing to Delete"}, 202)
        
    def user_patch_model(self, id, data):
        # UPDATE users SET col1=val, col2=val WHERE id={id}
        qry = "UPDATE users SET "
        for k, v in data.items():
            qry += f"{k}='{v}',"
        qry = qry[:-1] + f" WHERE id='{id}'" # Removing the comma at the end of the query and adding the WHERE condition
        self.cur.execute(qry)
        if self.cur.rowcount > 0 : 
            # return "User Updated Successfully"
            return make_response({"message":"User Updated Successfully"}, 201)
        else: 
            # return "Nothing to Update"
            return make_response({"message":"Nothing to Update"}, 202)
        
    def user_pagination_model(self, data):
        limit = int(data["limit"])
        page = int(data["page"])
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}" # startingIndex (starts from 0th Index), Limit
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result) > 0:
            res = make_response({"payload":result, "page_no":page, "limit":limit}, 200)
            return res
        else:
            return make_response({"message":"No Data Found"}, 204)
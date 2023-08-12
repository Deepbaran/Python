from config import dbconfig
import mysql.connector
from flask import make_response, send_file
from datetime import datetime, timedelta
import jwt

class user_model():
    def __init__(self):
        try:
            print(dbconfig)
            self.con = mysql.connector.connect(host=dbconfig['hostname'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True) # Records received from the DB will be in dictionary format
            print("Connection Successful: user_model")
        except:
            print("Some error: user_model")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if result: 
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
        self.cur.execute(f"INSERT INTO users(name, email, phone, password, role_id) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['password']}', '{data['role_id']}')")
        # self.con.commit() # As autocommit is enabled, we do not need to commit everytime
        # return "User Created Successfully"
        return make_response({"message":"User Created Successfully"}, 201)
    
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}',role_id='{data['role_id']}' WHERE id={data['id']}")
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
        if result:
            res = make_response({"payload":result, "page_no":page, "limit":limit}, 200)
            return res
        else:
            return make_response({"message":"No Data Found"}, 204)
        
    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount > 0 : 
            return make_response({"message":"File Uploaded Successfully"}, 201)
        else: 
            return make_response({"message":"Nothing to Upload"}, 202)
        
    def user_get_avatar_controller(self, id):
        self.cur.execute(f"SELECT avatar FROM users WHERE id={id}")
        result = self.cur.fetchall()
        if result and result[0]["avatar"]:
            return make_response(send_file(result[0]["avatar"]), 200)
        else:
            return make_response({"message":"No Data Found"}, 204)
        
    def user_login_model(self, data):
        self.cur.execute(f"SELECT id, name, email, phone, avatar, role_id FROM users WHERE email='{data['email']}' AND password='{data['password']}'")
        result = self.cur.fetchall()
        if result:
            userdata = result[0]
            exp_time = datetime.now() + timedelta(minutes=15)
            exp_epoch_time = int(exp_time.timestamp()) # Gives epoch time
            payload= {
                "payload": userdata,
                "exp": exp_epoch_time
            }
            token = jwt.encode(payload=payload, key="Deep", algorithm="HS256")
            return make_response({"token": token}, 200)
        else:
            return make_response({"message":"No Data Found"}, 204)
        
    def user_addmultiple_controller(self, data):
        # INSERT INTO table(columns) VALUES () () ()
        qry = "INSERT INTO users(name, email, phone, password, role_id) VALUES "
        for userdata in data:
            qry += f"('{userdata['name']}', '{userdata['email']}', '{userdata['phone']}', '{userdata['password']}', '{userdata['role_id']}'),"
        qry = qry[:-1] # qry.rstrip(",")
        self.cur.execute(qry)
        return make_response({"message":"Users Created Successfully"}, 201)
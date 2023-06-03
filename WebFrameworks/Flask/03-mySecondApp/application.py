from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name

class TestSchema(ma.Schema):
    class Meta:
        fields = ('name',)

test_schema = TestSchema()
tests_schema = TestSchema(many=True)

@app.route('/test', methods=['POST'])
def add_test():
    if 'id' in request.json:
        return 'Only one attribute "name" is expected. Received an unknown attribte "id"'
    else:
        new_test = Test(request.json['name'])
        db.session.add(new_test)
        db.session.commit()
        return test_schema.jsonify(new_test)

@app.route('/test', methods=['GET'])
def get_tests():
    res = Test.query.all()
    data = tests_schema.dump(res)
    return jsonify(data)

@app.route('/test/<id>', methods=['GET'])
def get_test(id):
    res = Test.query.get(id)
    return test_schema.jsonify(res)

@app.route('/test/<id>', methods=['PUT'])
def update_test(id):
    if 'id' not in request.json:
        return 'attribue "id" is required'
    else:
        res = Test.query.get(id)
        res.name = request.json["name"] if 'name' in request.json else res.name
        db.session.commit()
        return test_schema.jsonify(res)

@app.route('/test/<id>', methods=['DELETE'])
def delete_test(id):
    res = Test.query.get(id)
    db.session.delete(res)
    db.session.commit()
    return test_schema.jsonify(res)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
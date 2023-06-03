from flask import Flask, request, jsonify, logging
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os # This module generally uses with file paths

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Without this there will be warnings in the console.
# Init db
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema() # Not putting strict=True will give warning in console. Marshmalow 3.0.0 fixed this issue
products_schema = ProductSchema(many=True) # Many Product Schemas are queried

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    # Get the data from Postman/Frontend
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    # Save to db
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    app.logger.info(result)
    return jsonify(result)

# Get Single Product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    # Get the updated data from Frontend
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    # Set the updated data into the existing data set
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Get Single Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit() # Always comming after making any changes in the database
    return product_schema.jsonify(product)

# Run Server
if __name__ == "__main__":
    app.run(debug=True) # debug=True marks it as development. remove it before go-live
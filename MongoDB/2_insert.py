import pymongo

if __name__ == "__main__":
    # The code here will run only if we run this file.
    # This code will not run if we import.
    print("Welcome to pyMongo")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # Create Database [We need to create a collection along with a database. And if we are using Pymongo, then we need to add a Document to the Collection]
    db = client["test"]
    # Create Collection
    collection = db['testcollection']

    # Create Document
    doc = {"name": "Deep", "age": 25} # If we do not provide a _id key (to uniquelt identify the documents), MongoDB automatically adds it to the document
    collection.insert_one(doc) # insert one document

    # Insert Many
    doc1 = {"name": "Sumit", "age": 27}
    doc2 = {"name": "Kartik", "age": 23}
    collection.insert_many([doc1,doc2]) # insert many documents

    doc = {"_id": 1, "name": "Deep", "age": 25}
    collection.insert_one(doc)
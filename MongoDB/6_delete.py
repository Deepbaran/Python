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

    doc = {"name": "Sumit", "age": 28}
    collection.delete_one(doc) # Delete one document/record where name is Sumit and age is 28

    doc = {"name": "Deep"}
    deleted = collection.delete_many(doc) # Delete all documents where name is Deep
    print(deleted.deleted_count) # number of records deleted
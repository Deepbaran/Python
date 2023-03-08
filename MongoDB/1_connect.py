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
    
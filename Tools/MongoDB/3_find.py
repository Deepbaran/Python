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

    # Find
    one = collection.find_one({"name": "Deep"}) # {'_id': ObjectId('638c7e4050c7bf19bde61a44'), 'name': 'Deep', 'age': 25}
    print(one)

    all = collection.find({"name": "Deep"})
    print(all) # <pymongo.cursor.Cursor object at 0x000001C5CA653520>
    for doc in all:
        print(doc)
        # {'_id': ObjectId('638c7e4050c7bf19bde61a44'), 'name': 'Deep', 'age': 25}
        # {'_id': 1, 'name': 'Deep', 'age': 25}

    all_specific_fields = collection.find({"name": "Deep"}, {"_id": 0, "name": 0}) # Exclude _id and name from the results. We cannot mix exclusion and inclusion in one projection
    # By default all fields are marked as 1 (inclusion). So, we just need to manually exclude fields (mark them as 0)
    # One thing to remember. If we mark one field as 1 manually, then all the other fields will become 0 automatically, unless we are marking them manually as 1 too.
    # And if we mark a field as 0 manually, then all the other fields will become 1 automatically, unless we are marking them manually as 0 too.
    # This rule does not apply to _id. _id does not depend if others are marked as 0 or 1. _id by default is set as 1 and if we want to mark it as 0, we will need to manually do it.
    # As name is set as 0 here, so age automatically becomes 1
    for doc in all_specific_fields:
        print(doc)
        #{'age': 25}
        #{'age': 25}

    # With limit
    first_one = collection.find({"name": "Deep"}).limit(1)
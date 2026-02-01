from connection import db

collection = db["users"]

collection.create_index("email", unique=True)
collection.create_index("phone", unique=True)

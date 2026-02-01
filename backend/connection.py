from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URL from .env
MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("❌ MONGO_URL not found in .env file")

# Create MongoDB client
client = MongoClient(MONGO_URL, server_api=ServerApi('1'))

# Test connection
try:
    client.admin.command('ping')
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

# Select database
db = client["internship_db"]

import re
from difflib import SequenceMatcher
from database import collection

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def classify_data(name, email, phone):
    
    existing_users = list(collection.find())

    # Exact duplicate check
    for user in existing_users:
        if user["email"] == email or user["phone"] == phone:
            return "duplicate", "Exact email or phone already exists"

    # False positive check (similar name)
    for user in existing_users:
        if similarity(user["name"], name) > 0.85:
            return "false_positive", "Similar name detected"

    return "unique", "Data is unique"

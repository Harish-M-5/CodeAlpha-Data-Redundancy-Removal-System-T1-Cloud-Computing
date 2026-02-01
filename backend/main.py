from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import collection
from validation import validate_email, classify_data

app = FastAPI(title="Data Redundancy Removal System")

class User(BaseModel):
    name: str
    email: str
    phone: str

@app.post("/add-user")
def add_user(user: User):

    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    status, reason = classify_data(user.name, user.email, user.phone)

    if status == "duplicate":
        raise HTTPException(status_code=400, detail=reason)

    if status == "false_positive":
        return {
            "status": status,
            "reason": reason,
            "message": "Manual review required"
        }

    collection.insert_one(user.dict())

    return {
        "status": "unique",
        "message": "User added successfully"
    }

# Task 1: Data Redundancy Removal System in Cloud Computing Intership 

--- 

## Internship Overview
This project is part of my internship to design and implement a **Data Redundancy Removal System** using **FastAPI** and **MongoDB Atlas**, hosted on **Azure Cloud**. The goal is to build a backend system capable of identifying and preventing duplicate or redundant data entries in a cloud database while maintaining database accuracy and efficiency. The project also includes **API testing using Postman**.

---

## What is Data Redundancy Removal System in Cloud Computing?
Data redundancy occurs when the same piece of data exists multiple times in a database. Redundant data increases storage costs,reduces database efficiency and can lead to error in processing.  
This system ensures that only **unique and verified data** is appended to the cloud database, thereby improving **database accuracy**, **query efficiency**, and overall **data reliability**.

---

## Project Overview
This project implements a backend system that:
- Detects duplicate data in the cloud database
- Classifies entries as unique, duplicate, or false positive
- Prevents insertion of redundant data
- Appends only validated and verified entries
- Integrates with MongoDB Atlas for cloud storage
- Provides API endpoints tested via **Swagger** and **Postman**
- Is ready for **Azure deployment** for public access

---

## Features
- **Duplicate Detection**: Checks email and phone fields for existing entries  
- **False Positive Classification**: Flags similar but not exact entries  
- **Validation Mechanism**: Ensures new entries are verified before insertion  
- **MongoDB Atlas Integration**: Cloud-hosted database for scalability  
- **FastAPI Backend**: Efficient, asynchronous Python API  
- **Postman Testing**: Professional API testing and validation  
- **Azure Deployment**: Publicly accessible backend

---

## Technology Stack Used

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Backend development |
| FastAPI | REST API framework |
| MongoDB Atlas | Cloud database |
| Pymongo | MongoDB Python connector |
| Uvicorn | ASGI server for FastAPI |
| Python-dotenv | Environment variable management |
| Postman | API testing |
| Azure | Cloud deployment |

---


## Project Folder Structure

```
backend/
│
├── main.py
├── validation.py 
├── database.py
├── connection.py 
├── requirements.txt
└── .env

```


---

## Installation & Setup

1. **Clone the Repository**
```
git clone https://github.com/<my-github-my username>/data-redundancy-removal.git

cd data-redundancy-removal/backend
``` 


- install Python Dependencies

``` pip install -r requirements.txt ```


2. **Setup Environment Variables**

- Create a .env file in the backend folder:

``` MONGO_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/internship_db?retryWrites=true&w=majority ```


3. **Run the Server Locally**

``` uvicorn main:app --reload ```


4. **Test API**

 ``` http://127.0.0.1:8000/docs ``` 

Postman for API testing

---

## Design: Data Redundancy System

- The system identifies duplicate or redundant entries using MongoDB unique indexes on email and phone fields.

- Incoming data is checked against existing records before insertion.

- False positives are flagged if the data closely resembles existing entries but is not identical.

--- 

## Validation Mechanism

- Uses validation.py to implement:

- Exact match checks for email and phone.

- Similarity checks for false positive detection.

- Ensures only unique and validated entries are appended to the database.

  --- 

## Prevent Duplicate Data Insertion

- MongoDB indexes enforce unique constraints.

- Any attempt to insert a duplicate email or phone triggers an error and prevents the data from being saved


--- 

## Append Only Unique & Verified Entries

- New entries are appended only after validation.

- False positives are logged for review.

- Ensures the database contains clean and verified data at all times

  ---

## Database Accuracy & Efficiency

- Using MongoDB Atlas for a cloud-hosted database.

- Unique indexes improve query performance and maintain data integrity.

- Cloud deployment ensures scalable and reliable backend access

  --- 

## MongoDB Atlas

- Fully managed cloud database service.

- Provides high availability, auto-scaling, and security.

- Allows remote connection from Azure-hosted FastAPI backend

--- 

## API Testing with Postman

Add User: POST /add-user

Body: JSON

{
  "name": "Harish",
  "email": "harish@gmail.com",
  "phone": "9876543210"
}


Responses:

status: unique → Successfully added.

status: duplicate → Email/phone already exists.

status: false_positive → Similar data exists, manual review recommended

## API Testing Screenshot 
<img width="1920" height="1080" alt="Screenshot 2026-02-01 182246" src="https://github.com/user-attachments/assets/e2ac7161-c9e2-482d-96f7-3a9fee46572a" />


<img width="1920" height="1080" alt="Screenshot 2026-02-01 182608" src="https://github.com/user-attachments/assets/3053009d-4e78-499b-b73f-96e46a803e89" />

<img width="1920" height="1080" alt="Screenshot 2026-02-01 182629" src="https://github.com/user-attachments/assets/0c495f3a-7bce-44ea-a8db-21401a326424" />


---

## Azure Deployment

- Backend deployed as FastAPI app on Azure App Service.

- Environment variables set in Azure for MongoDB Atlas connection.

- Public URL allows remote API testing and integration.

- Fully cloud-ready and scalable for enterprise usage

  
---

## How the Project Runs

- Start backend server 

- Send POST requests to /add-user with JSON data.

- System validates entries.

- Unique entries are saved to MongoDB Atlas.

- API responses provide status for each operation

  ---

## Key Concepts Covered

- Cloud backend development with FastAPI.

- MongoDB Atlas cloud database integration.

- Data redundancy and duplicate prevention.

- API testing using Postman & Swagger.

- Azure deployment and environment configuration

  ---

## Configuration

- .env file for sensitive credentials.

- MongoDB Atlas cluster setup.

- Azure App Service environment variables.

- Python dependencies managed via requirements.txt.

- Internship Documentation

- Designed system architecture for cloud.

- Implemented backend APIs and validation logic.

- Tested using Postman and Swagger UI.

- Deployed backend on Azure cloud with MongoDB Atlas.

## Acknowledgment

Special thanks to internship mentors and online documentation for guiding cloud database integration, FastAPI setup, and Azure deployment.

## Conclusion

- This project demonstrates a real-world cloud backend system capable of handling data redundancy efficiently. - It ensures database accuracy, supports scalable deployment on Azure, and provides a professional-level API ready for production usage.

---




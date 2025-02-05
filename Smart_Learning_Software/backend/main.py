from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory storage for users and documents
users_db: Dict[int, dict] = {}
documents_db: Dict[int, dict] = {}


# Pydantic models for validation
class User(BaseModel):
    name: str
    age: int
    email: str


class Document(BaseModel):
    title: str
    content: str
    owner_id: int  # The user who owns the document


# --- USER ROUTES ---

@app.post("/user/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user_id] = user
    return {"message": "User created successfully", "user_id": user_id, "user": user}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {"message": "User updated successfully", "user_id": user_id, "user": user}


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully", "user_id": user_id}


# --- DOCUMENT ROUTES ---

@app.post("/document/{document_id}")
def create_document(document_id: int, document: Document):
    if document_id in documents_db:
        raise HTTPException(status_code=400, detail="Document already exists")
    if document.owner_id not in users_db:
        raise HTTPException(status_code=404, detail="Owner (User) not found")

    documents_db[document_id] = document
    return {"message": "Document created successfully", "document_id": document_id, "document": document}


@app.get("/document/{document_id}")
def get_document(document_id: int):
    if document_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents_db[document_id]


@app.put("/document/{document_id}")
def update_document(document_id: int, document: Document):
    if document_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    if document.owner_id not in users_db:
        raise HTTPException(status_code=404, detail="Owner (User) not found")

    documents_db[document_id] = document
    return {"message": "Document updated successfully", "document_id": document_id, "document": document}


@app.delete("/document/{document_id}")
def delete_document(document_id: int):
    if document_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    del documents_db[document_id]
    return {"message": "Document deleted successfully", "document_id": document_id}
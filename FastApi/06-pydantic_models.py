#############################################################
# Pydantic Models                                           #
#############################################################

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Instance
app = FastAPI()

user_details = {}
count_id = 1

class User(BaseModel):
    name:str = Field(..., min_length=3, max_length=10)
    phone:int = Field(..., ge=999999999, le=000000000)
    email:EmailStr

@app.post('/create')
def create_yser(user:User):
    global count_id
    user_details[count_id] = user
    response = {
        "message": "User Successfully created",
        "user_id": count_id,
        "user": user_details[count_id]
    }
    count_id += 1
    return response

@app.get('/users')
def get_users():
    if not user_details:
        raise HTTPException(status_code=404, details="No Users Found")
    return user_details

@app.get('/user{user_id}')
def get_single_user(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404, details="No Users Found")
    return user_details[user_id]

@app.put("/user/{user_id}")
def update_user(user_id:int, user:User):
    if user_id not in user_details:
        raise HTTPException(status_code=404, details="user Not Found")
    user_details[user_id] = user
    return {"message": "user Updated", "user": user}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in user_details:
        raise HTTPException(status_code=404, details="user Not Found" )
    delete= user_details.pop(user_id)
    return{"message": "User Deleted", "user": delete}
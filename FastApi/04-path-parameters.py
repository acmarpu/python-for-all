#############################################################
# Path Parameter '/'                                           #
#############################################################

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Instance
app = FastAPI()


# Method 01

@app.get("/getmyapi2/{name}/{mobile}")
def home(name:str, mobile:str):
    
    """
    This API expects name and mobile as path parameters.
    Both parameters are required.
    If either parameter is missing, FastAPI returns a validation error.

    """
    return {"name":name, "mobile":mobile}

# python -m uvicorn 04-path-parameters:app --reload
# http://127.0.0.1:8000/getmyapi2/ashoka/123456789


# Method 02

students = {
    1:{"name":"suresh",
       "courses": {
           101:{"class": "python", "fee":5000},
           102:{"class": "jav", "fee":5000}
       }},

    2:{"name":"ramesh",
       "courses": {
         201:{"class": "genai", "fee":5000},
         202:{"class": "devops", "fee":5000}
       }

       }
}

@app.get("/student/{student_id}/course/{course_id}")
def get_users(student_id: int, course_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student ID not found")

    return students[student_id]["courses"][course_id]

# python -m uvicorn basic-fastapi:app --reload
# http://127.0.0.1:8000/student/1/course/102

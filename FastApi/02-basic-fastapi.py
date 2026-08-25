from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Instance
app = FastAPI()

# Creat (POST)       --- @app.post: Create data
# Read (GET)         --- @app.get: Retrieve data
# Update (PUT/PATCH) --- @app.put / @app.patch: Update data
# Delete(DELETE)     --- @app.delete: Remove data

#############################################################
# simple Function                                           #
#############################################################

@app.get("/")
def home():
    return {"message": "This is my First FastAPI Call"}

# python -m uvicorn 02-basic-fastapi:app --reload
# http://127.0.0.1:8000/
# When a user hits the URL /, FastAPI routes/forwards that request to the function associated with /


@app.get("/getFastAPI")
def home():
    return {"message": "i have FastAPI"}

# http://127.0.0.1:8000/getFastAPI


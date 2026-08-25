#############################################################
# Query Parameters '?'                                      #
#############################################################

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Instance
app = FastAPI()

# Method 01

@app.get("/getmyapi1")
def home(name:str):
    """
    this api will expect the name as quer param
    if not will throw the error

    """
    return {"message":"my name is", "name": name}

# python -m uvicorn 03-query-parameters:app --reload
# http://127.0.0.1:8000/getmyapi1?name=ashoka



# Method 02

@app.get("/getmyapi2")
def home(name:str, mobile:str):
    """
    This API expects name and mobile as query parameters.
    Both parameters are required.
    If either parameter is missing, FastAPI returns a validation error.

    """
    return {"name":name, "mobile":mobile}

# http://127.0.0.1:8000/getmyapi2?name=ashoka&mobile=1234



# Method 03

products = [
    {"id": 1, "name": "pen", "category": "Stationery", "price": 30},
    {"id": 2, "name": "notebook", "category": "Stationery", "price": 120},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 250},
    {"id": 4, "name": "Eraser", "category": "Stationery", "price": 10},
    {"id": 5, "name": "pencil", "category": "Stationery", "price": 10},
]


@app.get("/products")
def search_products(
    category: Optional[str] = None,
    max_price: Optional[int] = None
):
    filter_products = products

    if category:
        filter_products = [
            p for p in filter_products
            if p["category"].lower() == category.lower()
        ]

    if max_price:
        filter_products = [
            p for p in filter_products
            if p["price"] <= max_price
        ]

    return filter_products


# http://127.0.0.1:8000/products?category=Stationery

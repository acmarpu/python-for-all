--------------------------------------------------------------------
#### FasrAPI
--------------------------------------------------------------------
✓ FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+
✓ Designed to create APIs quickly and efficiently with minimal code and maximum performance
✓ Built on top of Starlette (for web handling) and Pydantic (for data validation)
✓ Uses Python type hints to enable automatic validation, code completion, and error checking
✓ Auto-generates interactive API documentation using Swagger UI and ReDoc
✓ Built-in data validation and async support (via Pydantic and async/await syntax)
✓ Supports a Dependency Injection system for clean, testable, and reusable components.
✓ Blazing fast performance – Comparable to Node.js and Go
✓ Based on Python type hints – Clear, readable, and IDE-friendly code
✓ Automatic data validation – Uses Pydantic to validate request and response data
✓ Auto-generated API documentation – Swagger UI and ReDoc are built-in
✓ Async/await support – Perfect for building non-blocking, high-performance APIs
✓ Dependency Injection system – Makes authentication, database access, and reusable logic cleaner
✓ Testing made easy – Great support for unit testing and mocking
✓ Microservices ready – Ideal for building modular, scalable APIs
✓ Built-in JSON support – Automatically parses requests and formats responses as JSON
✓ Leverages full Python ecosystem – Works smoothly with NumPy, Pandas, Scikit-learn, etc.
✓ Great for mobile app backends, AI/ML APIs, IoT devices, and more
✓ Easy integration with OAuth2, JWT, and other authentication methods
✓ Supports background tasks, CORS, WebSockets, and middleware out of the box


--------------------------------------------------------------------
####  Query Parameters 
--------------------------------------------------------------------
* A query prameter is a value passed in the URL after the ? symbol, used to filter or customize the request without affecting the endpoint path itself.
    - Query parameters are included in the URL.
    - They start after the ? symbol
    - Multiple query parameters are separated using &.
    - Query parameters can be used with GET, POST, PUT, PATCH, DELETE, and other HTTP methods.
    - The maximum URL length is not fixed at 1000 characters. The limit depends on the browser, server, proxy, and other infrastructure. Therefore, avoid sending large amounts of data through query parameters.
    - URLs containing query parameters may be stored in browser history.
    - Query parameters should not be used for sensitive information, such as passwords, API keys, or secrets, because URLs can appear in browser history, logs, monitoring systems, and other places.
    
* Used When
    - you want to filter, sort, paginate, or modify results.
    - the parameters are optional or have default values.
    - they don't change the identity of the resource 


| Use Case                  | Examples                                      |
|---------------------------|-----------------------------------------------|
| Search / Filter products  | `/products?category=books&price=100`          |
| Pagination                | `/products?page=2&limit=20`                   |
| Sorting                   | `/products?sort=price_desc`                   |
| Optional parameters       | `/items?available=true`                       |
| Toggle or flag            | `/posts?include_comments=false`               |

--------------------------------------------------------------------
#### Requestbody 
--------------------------------------------------------------------
            - param will be outside of the request
            - applicable post, put, delete
            - no limit, can be used for large files 
            - browser will not store data in the history

--------------------------------------------------------------------
#### Path Vairable or Path Parameter
--------------------------------------------------------------------
* A Path parameter is a variable that is part of the URL path. it is used to identify a specific resource 
    - It is identified by '/' as part of the URL structure
    - It is commonly used to identify a specific resource.
    - Path parameters can be used with GET, POST, PUT, PATCH, DELETE, and other HTTP methods
    - There is no universal 1000-character limit for path parameters. The practical limit depends on the browser, web server, proxy, and other infrastructure.
    - Since the parameter is part of the URL, it may be stored in browser history, server logs, proxy logs, or monitoring systems.
    - Do not put sensitive information such as passwords, API keys, or secrets in path parameters.

* Used When:
    - you want to access a specific resource by its unique identifier
    - the daya is hierarchical or essential to the route

* Best for resource identification

| Use Case                | Examples                  |
|-------------------------|---------------------------|
| Get user details        | `/users/45`               |
| Get a product by ID     | `/products/1002`          |
| Fetch an order by ID    | `/orders/550`             |
| Nested resources        | `/users/5/orders/12`      |


#### Create Virtual environment in windows
* 
python -m venv .venv

#### Activate virtual environment in windows
source myvenv/Scripts/activate
.\.venv\Scripts\Activate.ps1   

#### Install fastapi
pip3 install fastapi
pip3 install fastapi uvicorn

python -m pip install -r requirements.txt
add valid package names:
fastapi
uvicorn

#### Run application
python -m pip install fastapi uvicorn
uvicorn <filenam.py>:app --reload
uvicorn main.py:app --reload
python -m uvicorn main:app --reload
python -m uvicorn main:app --reload


#### Pydantic Models
* A pydantic model is a class that inherits from baseModel(provided by the pydantic library). it allows you to define data shapes with type annotations, and automatically handles:
- validation
- Conversion
- Error reporting 
- Serialization/Deserialization

* Example:

```
from pydantic import BaseModel

class User(basemodel):
  name: str
  age: int

```
##### Why use Pydantic Models?
* Automatic validation: Ensure correct data types (e.g string, int, email,etc)
* Auto Error Responces in FastAPI: Shows clear error when wrong data is sent
* Swagger Interation: FastAPI reads model and shows it in the /docs UI
* Cleaner Code: No need to manually check inputs
* Serialization: Converts Python Objects into JSON and vice versa
* Nested Models: Models can include other models for complex data structures


##### CRUD Operations 
* Creat (POST)     --- @app.post: Create data
* Read (GET)       --- @app.get: Retrieve data
* Update (PUT/PATCH) --- @app.put / @app.patch: Update data
* Delete(DELETE)     --- @app.delete: Remove data


#### Compatible Databases
* FastAPI supports multiple databases using ORMs SQLAIchemy or SQLModel

- Popuiar supported databases:
  - SQLite
  - PostgreSQL
  - MySQL/MariaDB
  - Microsoft SQL Server
  - Oracle and more

* SQLModel simplefiles the management of database tables, API Requests, and responses - all within a single unified model

* **What is SQL Model?**
- SQLModel is a modern python library
- Combine the power of PYdantic and SQLALchemy
- Single model for DB, input and output
- Cleaner and easier data handling
- Seamless integration with FastAPI
* python -m pip install fastapi uvicorn sqlmodel



https://www.youtube.com/watch?v=SEGXgQrJLxI&list=PLfXWSguRXGuX3sEpyfb-A3JkBGnrYLfgQ&index=11

https://www.geeksforgeeks.org/python/creating-first-rest-api-with-fastapi/
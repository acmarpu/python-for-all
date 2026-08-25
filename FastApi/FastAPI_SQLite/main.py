from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from contextlib import asynccontextmanager
from typing import Annotated, Optional
from pydantic import BaseModel, Field, EmailStr
from models import User, CreateUser

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


@app.post("/createuser")
def create_user(user:CreateUser, session:SessionDep):
    new_user = User.model_validate(user)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.get("/user", response_model=list[User])
def get_users(session:SessionDep):
    users = session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")

    return users




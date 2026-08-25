from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Instance
app = FastAPI()

class otp(BaseModel):
    value: int


@app.get("/otpvalidation")
def otpvalidation(otp_obj:otp):
    
    """
    requestbody otp_obj is implemented ...

    """
    if otp_obj.value == 12345:
        return {"message": "OTP is fine"}

    else:
        return {"message": "OTP is not valid"}




# python -m uvicorn 05-requestbody:app --reload
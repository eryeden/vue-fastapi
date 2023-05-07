from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel
import os


app = FastAPI()


# root
@app.get("/")
async def root():
    return {"message": "This is the root."}


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

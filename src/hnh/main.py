from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from rightnow.time import now
import os

app = FastAPI()

@app.post("/predict/")
async def predict():
    result = "<<prediction result>>"
    return result

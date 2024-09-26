from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from typing import Union
from PIL import Image
import random
import os
import io

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "hotdog"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.get("/predict")
def hotdog():
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog") 
    return {"Hello": random.choice(["hotdog", "not hotdog"])}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    img = Image.open(io.BytesIO(img)) # img 바이트를 PIL 이미지로 변환
    predictions = model(img)

    return {"Hello": predictions}

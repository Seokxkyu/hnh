from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import Union
from transformers import pipeline
from hnh.utils import get_max_label
import os
import random

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.get("/predict")
def hotdog():
    pre = ("Not Hotdog", "Hotdog")
    return random.choice(pre)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img)) # 이미지 byte를 PIL 이미지로 변환
    p = model(img)
    # {'label': 'hot dog', 'score': 0.54}

    # if p 값이 배열과 같이 나오면 높은 확률의 값을 추출해서 리턴하기
    score = p[0]['score']
    if score >= 0.8:
        return {"prediction": p, "label": "hot dog"}
    else:
        return {"label": "not hot dog"}

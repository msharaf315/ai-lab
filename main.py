import os
from dotenv import load_dotenv
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO

from schema.predictions_res import PredictionRes
from service.parse_image_prediction import parse_image_prediction

app = FastAPI()


load_dotenv()
model_path = os.getenv("MODEL_PATH")
model = YOLO(model_path)


@app.post("/calculate-image-score/", response_model=PredictionRes)
async def create_file(
    image: Annotated[UploadFile, File()],
):
    file_location = f"uploaded_images/{image.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
        prediction = model(file_location)
        card_names, score, score_details = parse_image_prediction(prediction[0])
    os.remove(file_location)
    return PredictionRes(
        card_names=card_names, score=score, score_details=score_details
    )

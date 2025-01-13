FROM python:3.11.10

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./main.py /main.py
COPY ./schema /schema
COPY ./models /models 
COPY ./service /service
RUN mkdir uploaded_images

ENV MODEL_PATH='/models/15_epoch_individual_card_labels.pt'
EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]
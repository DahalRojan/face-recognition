FROM python:3.10.9-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install cmake build-essential libglib2.0-0 libgl1-mesa-glx -y

RUN pip install --upgrade pip  && pip install dlib
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app
RUN mkdir -p /app/temp && mkdir -p /app/assets/images
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9292"]


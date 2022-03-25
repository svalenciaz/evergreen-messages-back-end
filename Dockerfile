FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade setuptools

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./config /code/app/config
COPY ./models /code/app/models
COPY ./routes /code/app/routes
COPY ./schemas /code/app/schemas
COPY ./app.py /code/app/main.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
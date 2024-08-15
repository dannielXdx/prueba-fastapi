FROM python:3.12

COPY ./requirements.txt /app/requirements.txt
COPY ./app /app
COPY ./tests /tests

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

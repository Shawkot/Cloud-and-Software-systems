FROM python:3.10.8-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload"]
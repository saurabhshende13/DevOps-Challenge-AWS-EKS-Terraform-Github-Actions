FROM python:3.9-slim

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py", "--host=0.0.0.0", "--port=80"]

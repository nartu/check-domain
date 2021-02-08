FROM tiangolo/uvicorn-gunicorn-fastapi
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

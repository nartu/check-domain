from fastapi import FastAPI
from app import is_alive_host

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Try /healthz?hostname=semrush.com"}

@app.get("/healthz")
async def is_alive(hostname: str):
    return {"status": is_alive_host(hostname)}

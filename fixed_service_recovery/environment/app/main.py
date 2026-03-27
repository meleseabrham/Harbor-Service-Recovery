from fastapi import FastAPI
from app.routes import router

APP_VERSION = "2.0.0"

app = FastAPI()
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": APP_VERSION}

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

from fastapi import FastAPI

app = FastAPI()
@app.get("/test")
def index():
    return {"first API":"welcome to fast api"}

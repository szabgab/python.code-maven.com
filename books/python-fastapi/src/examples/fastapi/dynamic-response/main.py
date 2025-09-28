from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "date": datetime.datetime.now()}


import random
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# List of sheer images (add more here)
Sheer = [
    "images/sheer1.jpg",
    "images/sheer2.jpg",
    "images/sheer3.jpg"
]

@app.get("/")
def home():
    return {"message": "Welcome to sheer API! Go to /sheer to get a random sheer."}

@app.get("/sheer")
def get_sheer():
    Sheer = random.choice(sheer)
    return FileResponse(sheer)

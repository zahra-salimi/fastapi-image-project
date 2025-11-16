from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}


@app.post("/upload-image/")
async def create_upload_file(file: UploadFile):

    file_path = os.path.join("images", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"File '{file.filename}' saved at '{file_path}'"}



@app.get("/images/")
async def get_image(image_name: str):
    image_path = os.path.join("images", image_name)

    if os.path.exists(image_path):
        return FileResponse(image_path)

    return {"error": "Image not found"}


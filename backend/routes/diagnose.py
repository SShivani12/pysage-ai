from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/diagnose")
async def diagnose(file: UploadFile = File(...)):
    content = await file.read()

    return {
        "filename": file.filename,
        "content": content.decode("utf-8")
    }
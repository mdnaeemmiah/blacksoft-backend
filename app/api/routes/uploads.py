from __future__ import annotations

import os
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.upload import UploadResponse
from app.services.cloudinary_service import upload_image_to_cloudinary

router = APIRouter(prefix="/uploads", tags=["Uploads"])


@router.post("/image", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_image(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename or "")[1] or ".bin"
    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_path = temp_file.name
            content = await file.read()
            temp_file.write(content)

        result = upload_image_to_cloudinary(temp_path)
        return UploadResponse(
            url=result["url"],
            publicId=result["public_id"],
            secureUrl=result["secure_url"],
            originalFilename=file.filename,
        )
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Upload failed: {exc}") from exc
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

from __future__ import annotations

import cloudinary
import cloudinary.uploader

from app.core.config import get_settings


def configure_cloudinary() -> None:
    settings = get_settings()
    if not all([settings.cloudinary_cloud_name, settings.cloudinary_api_key, settings.cloudinary_api_secret]):
        return

    cloudinary.config(
        cloud_name=settings.cloudinary_cloud_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True,
    )


def upload_image_to_cloudinary(file_path: str, folder: str | None = None) -> dict:
    settings = get_settings()
    if not all([settings.cloudinary_cloud_name, settings.cloudinary_api_key, settings.cloudinary_api_secret]):
        raise RuntimeError("Cloudinary is not configured")

    target_folder = folder or settings.cloudinary_folder
    return cloudinary.uploader.upload(
        file_path,
        folder=target_folder,
    )

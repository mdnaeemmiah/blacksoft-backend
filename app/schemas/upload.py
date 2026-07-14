from pydantic import BaseModel, ConfigDict, Field


class UploadResponse(BaseModel):
    url: str
    public_id: str = Field(alias="publicId")
    secure_url: str = Field(alias="secureUrl")
    original_filename: str | None = Field(default=None, alias="originalFilename")
    model_config = ConfigDict(populate_by_name=True)

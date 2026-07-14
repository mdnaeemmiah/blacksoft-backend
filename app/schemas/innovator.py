from pydantic import BaseModel, ConfigDict, Field


class InnovatorBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    enabled: bool = True


class InnovatorCreate(InnovatorBase):
    pass


class InnovatorUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    enabled: bool | None = None


class InnovatorResponse(InnovatorBase):
    id: str = Field(alias="_id")
    model_config = ConfigDict(populate_by_name=True)

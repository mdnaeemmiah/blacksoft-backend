from pydantic import BaseModel, ConfigDict, Field


class CapabilityBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    icon: str = Field(default="AI", max_length=40)
    link: str = Field(default="#services", max_length=250)
    enabled: bool = True


class CapabilityCreate(CapabilityBase):
    pass


class CapabilityUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    icon: str | None = Field(default=None, max_length=40)
    link: str | None = Field(default=None, max_length=250)
    enabled: bool | None = None


class CapabilityResponse(CapabilityBase):
    id: str = Field(alias="_id")
    model_config = ConfigDict(populate_by_name=True)

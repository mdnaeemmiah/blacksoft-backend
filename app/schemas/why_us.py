from pydantic import BaseModel, ConfigDict, Field


class WhyUsBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    icon: str = Field(default="⚡", max_length=40)
    enabled: bool = True


class WhyUsCreate(WhyUsBase):
    pass


class WhyUsUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    icon: str | None = Field(default=None, max_length=40)
    enabled: bool | None = None


class WhyUsResponse(WhyUsBase):
    id: str = Field(alias="_id")
    model_config = ConfigDict(populate_by_name=True)

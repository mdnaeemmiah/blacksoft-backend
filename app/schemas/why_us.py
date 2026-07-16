from pydantic import BaseModel, ConfigDict, Field


class WhyUsBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    icon: str = Field(default="⚡", max_length=40)
    image_src: str = Field(default="", alias="imageSrc", max_length=500)
    image_alt: str = Field(default="", alias="imageAlt", max_length=200)
    enabled: bool = True

    model_config = ConfigDict(populate_by_name=True)


class WhyUsCreate(WhyUsBase):
    pass


class WhyUsUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    icon: str | None = Field(default=None, max_length=40)
    image_src: str | None = Field(default=None, alias="imageSrc", max_length=500)
    image_alt: str | None = Field(default=None, alias="imageAlt", max_length=200)
    enabled: bool | None = None

    model_config = ConfigDict(populate_by_name=True)


class WhyUsResponse(WhyUsBase):
    id: str = Field(alias="_id")
    model_config = ConfigDict(populate_by_name=True)

from pydantic import BaseModel, ConfigDict, Field


class EcommerceCardBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    image_src: str = Field(default="", alias="imageSrc", max_length=500)
    image_alt: str = Field(default="Ecommerce card image", alias="imageAlt", max_length=200)
    is_placeholder: bool = Field(default=False, alias="isPlaceholder")
    enabled: bool = True

    model_config = ConfigDict(populate_by_name=True)


class EcommerceCardCreate(EcommerceCardBase):
    pass


class EcommerceCardUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    image_src: str | None = Field(default=None, alias="imageSrc", max_length=500)
    image_alt: str | None = Field(default=None, alias="imageAlt", max_length=200)
    is_placeholder: bool | None = Field(default=None, alias="isPlaceholder")
    enabled: bool | None = None

    model_config = ConfigDict(populate_by_name=True)


class EcommerceCardResponse(EcommerceCardBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


class SolutionCardBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    category: str = Field(default="App", max_length=120)
    icon: str = Field(default="AI", max_length=40)
    link: str = Field(default="#solutions", max_length=250)
    enabled: bool = True


class AppWebsiteCardCreate(SolutionCardBase):
    pass


class AppWebsiteCardUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    category: str | None = Field(default=None, max_length=120)
    icon: str | None = Field(default=None, max_length=40)
    link: str | None = Field(default=None, max_length=250)
    enabled: bool | None = None


class AppWebsiteCardResponse(SolutionCardBase):
    id: str


class AiSolutionCardCreate(SolutionCardBase):
    pass


class AiSolutionCardUpdate(AppWebsiteCardUpdate):
    pass


class AiSolutionCardResponse(SolutionCardBase):
    id: str


class TechnologyStackCardBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    category: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    icon_key: str = Field(default="growth", alias="iconKey", max_length=40)
    enabled: bool = True

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackCardCreate(TechnologyStackCardBase):
    pass


class TechnologyStackCardUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    category: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    icon_key: str | None = Field(default=None, alias="iconKey", max_length=40)
    enabled: bool | None = None

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackCardResponse(TechnologyStackCardBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackSettingsBase(BaseModel):
    section_title: str = Field(min_length=1, max_length=120, alias="sectionTitle")
    section_subtitle: str = Field(min_length=1, max_length=500, alias="sectionSubtitle")

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackSettingsUpdate(BaseModel):
    section_title: str | None = Field(default=None, min_length=1, max_length=120, alias="sectionTitle")
    section_subtitle: str | None = Field(default=None, min_length=1, max_length=500, alias="sectionSubtitle")

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackSettingsResponse(TechnologyStackSettingsBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


class TeamMemberBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    role: str = Field(min_length=1, max_length=120)
    image_src: str = Field(default="", alias="imageSrc", max_length=500)
    image_alt: str = Field(default="Team member image", alias="imageAlt", max_length=200)
    logo: str = Field(default="", max_length=500)
    bio: str = Field(default="", max_length=1000)
    link: str = Field(default="", max_length=500)
    enabled: bool = True

    model_config = ConfigDict(populate_by_name=True)


class TeamMemberCreate(TeamMemberBase):
    pass


class TeamMemberUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    role: str | None = Field(default=None, min_length=1, max_length=120)
    image_src: str | None = Field(default=None, alias="imageSrc", max_length=500)
    image_alt: str | None = Field(default=None, alias="imageAlt", max_length=200)
    logo: str | None = Field(default=None, max_length=500)
    bio: str | None = Field(default=None, max_length=1000)
    link: str | None = Field(default=None, max_length=500)
    enabled: bool | None = None

    model_config = ConfigDict(populate_by_name=True)


class TeamMemberResponse(TeamMemberBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


class TeamSettingsBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    subtitle: str = Field(min_length=1, max_length=500)
    cta_label: str = Field(min_length=1, max_length=120, alias="ctaLabel")
    cta_link: str = Field(min_length=1, max_length=250, alias="ctaLink")

    model_config = ConfigDict(populate_by_name=True)


class TeamSettingsUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    subtitle: str | None = Field(default=None, min_length=1, max_length=500)
    cta_label: str | None = Field(default=None, min_length=1, max_length=120, alias="ctaLabel")
    cta_link: str | None = Field(default=None, min_length=1, max_length=250, alias="ctaLink")

    model_config = ConfigDict(populate_by_name=True)


class TeamSettingsResponse(TeamSettingsBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


class WhoWeAreSettingsBase(BaseModel):
    tag: str = Field(min_length=1, max_length=120)
    title: str = Field(min_length=1, max_length=500)
    description: str = Field(min_length=1, max_length=2000)
    
    highlight1_num: str = Field(min_length=1, max_length=50, alias="highlight1Num")
    highlight1_label: str = Field(min_length=1, max_length=120, alias="highlight1Label")

    highlight2_num: str = Field(min_length=1, max_length=50, alias="highlight2Num")
    highlight2_label: str = Field(min_length=1, max_length=120, alias="highlight2Label")

    highlight3_num: str = Field(min_length=1, max_length=50, alias="highlight3Num")
    highlight3_label: str = Field(min_length=1, max_length=120, alias="highlight3Label")

    model_config = ConfigDict(populate_by_name=True)


class WhoWeAreSettingsUpdate(BaseModel):
    tag: str | None = Field(default=None, min_length=1, max_length=120)
    title: str | None = Field(default=None, min_length=1, max_length=500)
    description: str | None = Field(default=None, min_length=1, max_length=2000)

    highlight1_num: str | None = Field(default=None, min_length=1, max_length=50, alias="highlight1Num")
    highlight1_label: str | None = Field(default=None, min_length=1, max_length=120, alias="highlight1Label")

    highlight2_num: str | None = Field(default=None, min_length=1, max_length=50, alias="highlight2Num")
    highlight2_label: str | None = Field(default=None, min_length=1, max_length=120, alias="highlight2Label")

    highlight3_num: str | None = Field(default=None, min_length=1, max_length=50, alias="highlight3Num")
    highlight3_label: str | None = Field(default=None, min_length=1, max_length=120, alias="highlight3Label")

    model_config = ConfigDict(populate_by_name=True)


class WhoWeAreSettingsResponse(WhoWeAreSettingsBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


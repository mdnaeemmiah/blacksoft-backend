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


class OtherLink(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=1000)
    url: str = Field(min_length=1, max_length=500)

    model_config = ConfigDict(populate_by_name=True)


class SolutionCardBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1, max_length=1000)
    category: str = Field(default="App", max_length=120)
    icon: str = Field(default="AI", max_length=40)
    link: str = Field(default="#solutions", max_length=250)
    image_src: str = Field(default="", alias="imageSrc", max_length=500)
    image_alt: str = Field(default="", alias="imageAlt", max_length=200)
    enabled: bool = True
    other_links: list[OtherLink] = Field(default_factory=list, alias="otherLinks")

    model_config = ConfigDict(populate_by_name=True)


class AppWebsiteCardCreate(SolutionCardBase):
    pass


class AppWebsiteCardUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    category: str | None = Field(default=None, max_length=120)
    icon: str | None = Field(default=None, max_length=40)
    link: str | None = Field(default=None, max_length=250)
    image_src: str | None = Field(default=None, alias="imageSrc", max_length=500)
    image_alt: str | None = Field(default=None, alias="imageAlt", max_length=200)
    enabled: bool | None = None
    other_links: list[OtherLink] | None = Field(default=None, alias="otherLinks")

    model_config = ConfigDict(populate_by_name=True)


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
    image_src: str = Field(default="", alias="imageSrc", max_length=500)
    image_alt: str = Field(default="", alias="imageAlt", max_length=200)
    enabled: bool = True

    model_config = ConfigDict(populate_by_name=True)


class TechnologyStackCardCreate(TechnologyStackCardBase):
    pass


class TechnologyStackCardUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    category: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    icon_key: str | None = Field(default=None, alias="iconKey", max_length=40)
    image_src: str | None = Field(default=None, alias="imageSrc", max_length=500)
    image_alt: str | None = Field(default=None, alias="imageAlt", max_length=200)
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
    linkedin: str = Field(default="", max_length=500)
    github: str = Field(default="", max_length=500)
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
    linkedin: str | None = Field(default=None, max_length=500)
    github: str | None = Field(default=None, max_length=500)
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


class StatsSettingsBase(BaseModel):
    stat1_value: str = Field(default="", max_length=50, alias="stat1Value")
    stat1_label: str = Field(default="", max_length=120, alias="stat1Label")
    stat1_description: str = Field(default="", max_length=500, alias="stat1Description")

    stat2_value: str = Field(default="", max_length=50, alias="stat2Value")
    stat2_label: str = Field(default="", max_length=120, alias="stat2Label")
    stat2_description: str = Field(default="", max_length=500, alias="stat2Description")

    stat3_value: str = Field(default="", max_length=50, alias="stat3Value")
    stat3_label: str = Field(default="", max_length=120, alias="stat3Label")
    stat3_description: str = Field(default="", max_length=500, alias="stat3Description")

    model_config = ConfigDict(populate_by_name=True)


class StatsSettingsUpdate(BaseModel):
    stat1_value: str | None = Field(default=None, max_length=50, alias="stat1Value")
    stat1_label: str | None = Field(default=None, max_length=120, alias="stat1Label")
    stat1_description: str | None = Field(default=None, max_length=500, alias="stat1Description")

    stat2_value: str | None = Field(default=None, max_length=50, alias="stat2Value")
    stat2_label: str | None = Field(default=None, max_length=120, alias="stat2Label")
    stat2_description: str | None = Field(default=None, max_length=500, alias="stat2Description")

    stat3_value: str | None = Field(default=None, max_length=50, alias="stat3Value")
    stat3_label: str | None = Field(default=None, max_length=120, alias="stat3Label")
    stat3_description: str | None = Field(default=None, max_length=500, alias="stat3Description")

    model_config = ConfigDict(populate_by_name=True)


class StatsSettingsResponse(StatsSettingsBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)


# ─── Contact Info Settings ────────────────────────────────────────────────────

class ContactInfoSettingsBase(BaseModel):
    location: str = Field(default="", max_length=300)
    email: str = Field(default="", max_length=200)
    phone: str = Field(default="", max_length=80)
    privacy_policy: str = Field(default="", alias="privacyPolicy", max_length=20000)

    model_config = ConfigDict(populate_by_name=True)


class ContactInfoSettingsUpdate(BaseModel):
    location: str | None = Field(default=None, max_length=300)
    email: str | None = Field(default=None, max_length=200)
    phone: str | None = Field(default=None, max_length=80)
    privacy_policy: str | None = Field(default=None, alias="privacyPolicy", max_length=20000)

    model_config = ConfigDict(populate_by_name=True)


class ContactInfoSettingsResponse(ContactInfoSettingsBase):
    id: str

    model_config = ConfigDict(populate_by_name=True)

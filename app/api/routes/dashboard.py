from __future__ import annotations

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from app.db.mongodb import get_db
from app.models.common import as_document_id
from app.core.security import require_dashboard_user
from app.schemas.capability import CapabilityCreate, CapabilityResponse, CapabilityUpdate
from app.schemas.innovator import InnovatorCreate, InnovatorResponse, InnovatorUpdate
from app.schemas.dashboard import (
    EcommerceCardCreate,
    EcommerceCardResponse,
    EcommerceCardUpdate,
    AppWebsiteCardCreate,
    AppWebsiteCardResponse,
    AppWebsiteCardUpdate,
    AiSolutionCardCreate,
    AiSolutionCardResponse,
    AiSolutionCardUpdate,
    TeamMemberCreate,
    TeamMemberResponse,
    TeamMemberUpdate,
    TeamSettingsResponse,
    TeamSettingsUpdate,
    TechnologyStackCardCreate,
    TechnologyStackCardResponse,
    TechnologyStackCardUpdate,
    TechnologyStackSettingsResponse,
    TechnologyStackSettingsUpdate,
    WhoWeAreSettingsResponse,
    WhoWeAreSettingsUpdate,
    StatsSettingsResponse,
    StatsSettingsUpdate,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

admin_router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
    dependencies=[Depends(require_dashboard_user)],
)


def serialize_document(document: dict) -> dict:
    result = dict(document)
    object_id = result.pop("_id", None)
    if isinstance(object_id, ObjectId):
        result["id"] = str(object_id)
    elif object_id is not None:
        result["id"] = str(object_id)
    return result


async def list_documents(collection_name: str) -> list[dict]:
    db = get_db()
    collection = getattr(db, collection_name)
    items: list[dict] = []
    async for document in collection.find().sort("_id", -1):
        items.append(serialize_document(document))
    return items


async def create_document(collection_name: str, payload: dict) -> dict:
    db = get_db()
    collection = getattr(db, collection_name)
    result = await collection.insert_one(payload)
    document = await collection.find_one({"_id": result.inserted_id})
    if document is None:
        raise HTTPException(status_code=500, detail=f"Failed to create item in {collection_name}")
    return serialize_document(document)


async def update_document(collection_name: str, item_id: str, payload: dict, not_found_detail: str) -> dict:
    db = get_db()
    collection = getattr(db, collection_name)
    try:
        object_id = as_document_id(item_id)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid {not_found_detail.lower()} id")

    update_data = {key: value for key, value in payload.items() if value is not None}
    if not update_data:
        document = await collection.find_one({"_id": object_id})
        if document is None:
            raise HTTPException(status_code=404, detail=not_found_detail)
        return serialize_document(document)

    result = await collection.update_one({"_id": object_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=not_found_detail)

    document = await collection.find_one({"_id": object_id})
    if document is None:
        raise HTTPException(status_code=404, detail=not_found_detail)
    return serialize_document(document)


async def delete_document(collection_name: str, item_id: str, not_found_detail: str) -> None:
    db = get_db()
    collection = getattr(db, collection_name)
    try:
        object_id = as_document_id(item_id)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid {not_found_detail.lower()} id")

    result = await collection.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=not_found_detail)


async def get_settings_document(collection_name: str, document_id: str, defaults: dict) -> dict:
    db = get_db()
    collection = getattr(db, collection_name)
    document = await collection.find_one({"_id": document_id})
    if document is None:
        await collection.insert_one(defaults)
        document = await collection.find_one({"_id": document_id})
    if document is None:
        raise HTTPException(status_code=500, detail=f"Failed to load settings for {collection_name}")
    return serialize_document(document)


async def upsert_settings_document(collection_name: str, document_id: str, payload: dict, defaults: dict) -> dict:
    db = get_db()
    collection = getattr(db, collection_name)
    existing = await collection.find_one({"_id": document_id})
    if existing is None:
        next_document = dict(defaults)
    else:
        next_document = dict(existing)

    next_document.update({key: value for key, value in payload.items() if value is not None})
    next_document["_id"] = document_id

    await collection.replace_one({"_id": document_id}, next_document, upsert=True)
    document = await collection.find_one({"_id": document_id})
    if document is None:
        raise HTTPException(status_code=500, detail=f"Failed to update settings for {collection_name}")
    return serialize_document(document)


@router.get("/summary")
async def dashboard_summary() -> dict[str, int]:
    db = get_db()
    return {
        "capabilities": await db.capabilities.count_documents({}),
        "innovators": await db.innovators.count_documents({}),
        "ecommerce_cards": await db.ecommerce_cards.count_documents({}),
        "app_websites": await db.app_website_cards.count_documents({}),
        "ai_solutions": await db.ai_solution_cards.count_documents({}),
        "technology_stack_cards": await db.technology_stack_cards.count_documents({}),
        "team_members": await db.team_members.count_documents({}),
    }


@router.get("/capabilities", response_model=list[CapabilityResponse])
async def list_capabilities():
    return await list_documents("capabilities")


@admin_router.post("/capabilities", response_model=CapabilityResponse, status_code=status.HTTP_201_CREATED)
async def create_capability(payload: CapabilityCreate):
    return await create_document("capabilities", payload.model_dump())


@admin_router.put("/capabilities/{capability_id}", response_model=CapabilityResponse)
async def update_capability(capability_id: str, payload: CapabilityUpdate):
    return await update_document("capabilities", capability_id, payload.model_dump(), "Capability not found")


@admin_router.delete("/capabilities/{capability_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_capability(capability_id: str):
    await delete_document("capabilities", capability_id, "Capability not found")
    return None


@router.get("/innovators", response_model=list[InnovatorResponse])
async def list_innovators():
    return await list_documents("innovators")


@admin_router.post("/innovators", response_model=InnovatorResponse, status_code=status.HTTP_201_CREATED)
async def create_innovator(payload: InnovatorCreate):
    return await create_document("innovators", payload.model_dump())


@admin_router.put("/innovators/{innovator_id}", response_model=InnovatorResponse)
async def update_innovator(innovator_id: str, payload: InnovatorUpdate):
    return await update_document("innovators", innovator_id, payload.model_dump(), "Innovator not found")


@admin_router.delete("/innovators/{innovator_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_innovator(innovator_id: str):
    await delete_document("innovators", innovator_id, "Innovator not found")
    return None


@router.get("/ecommerce/cards", response_model=list[EcommerceCardResponse])
async def list_ecommerce_cards():
    return await list_documents("ecommerce_cards")


@admin_router.post("/ecommerce/cards", response_model=EcommerceCardResponse, status_code=status.HTTP_201_CREATED)
async def create_ecommerce_card(payload: EcommerceCardCreate):
    return await create_document("ecommerce_cards", payload.model_dump())


@admin_router.put("/ecommerce/cards/{card_id}", response_model=EcommerceCardResponse)
async def update_ecommerce_card(card_id: str, payload: EcommerceCardUpdate):
    return await update_document("ecommerce_cards", card_id, payload.model_dump(), "Ecommerce card not found")


@admin_router.delete("/ecommerce/cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ecommerce_card(card_id: str):
    await delete_document("ecommerce_cards", card_id, "Ecommerce card not found")
    return None


@router.get("/app-websites/cards", response_model=list[AppWebsiteCardResponse])
async def list_app_website_cards():
    return await list_documents("app_website_cards")


@admin_router.post("/app-websites/cards", response_model=AppWebsiteCardResponse, status_code=status.HTTP_201_CREATED)
async def create_app_website_card(payload: AppWebsiteCardCreate):
    return await create_document("app_website_cards", payload.model_dump())


@admin_router.put("/app-websites/cards/{card_id}", response_model=AppWebsiteCardResponse)
async def update_app_website_card(card_id: str, payload: AppWebsiteCardUpdate):
    return await update_document("app_website_cards", card_id, payload.model_dump(), "App website card not found")


@admin_router.delete("/app-websites/cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_app_website_card(card_id: str):
    await delete_document("app_website_cards", card_id, "App website card not found")
    return None


@router.get("/ai-solutions/cards", response_model=list[AiSolutionCardResponse])
async def list_ai_solution_cards():
    return await list_documents("ai_solution_cards")


@admin_router.post("/ai-solutions/cards", response_model=AiSolutionCardResponse, status_code=status.HTTP_201_CREATED)
async def create_ai_solution_card(payload: AiSolutionCardCreate):
    return await create_document("ai_solution_cards", payload.model_dump())


@admin_router.put("/ai-solutions/cards/{card_id}", response_model=AiSolutionCardResponse)
async def update_ai_solution_card(card_id: str, payload: AiSolutionCardUpdate):
    return await update_document("ai_solution_cards", card_id, payload.model_dump(), "AI solution card not found")


@admin_router.delete("/ai-solutions/cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_solution_card(card_id: str):
    await delete_document("ai_solution_cards", card_id, "AI solution card not found")
    return None


@router.get("/technology-stack/cards", response_model=list[TechnologyStackCardResponse])
async def list_technology_stack_cards():
    return await list_documents("technology_stack_cards")


@admin_router.post("/technology-stack/cards", response_model=TechnologyStackCardResponse, status_code=status.HTTP_201_CREATED)
async def create_technology_stack_card(payload: TechnologyStackCardCreate):
    return await create_document("technology_stack_cards", payload.model_dump())


@admin_router.put("/technology-stack/cards/{card_id}", response_model=TechnologyStackCardResponse)
async def update_technology_stack_card(card_id: str, payload: TechnologyStackCardUpdate):
    return await update_document("technology_stack_cards", card_id, payload.model_dump(), "Technology stack card not found")


@admin_router.delete("/technology-stack/cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_technology_stack_card(card_id: str):
    await delete_document("technology_stack_cards", card_id, "Technology stack card not found")
    return None


@router.get("/technology-stack/settings", response_model=TechnologyStackSettingsResponse)
async def get_technology_stack_settings():
    return await get_settings_document(
        "technology_stack_settings",
        "technology_stack",
        {
            "_id": "technology_stack",
            "section_title": "Our Technology Stack",
            "section_subtitle": "Built on battle-tested frameworks and advanced cloud kernels.",
        },
    )


@admin_router.put("/technology-stack/settings", response_model=TechnologyStackSettingsResponse)
async def update_technology_stack_settings(payload: TechnologyStackSettingsUpdate):
    return await upsert_settings_document(
        "technology_stack_settings",
        "technology_stack",
        payload.model_dump(),
        {
            "_id": "technology_stack",
            "section_title": "Our Technology Stack",
            "section_subtitle": "Built on battle-tested frameworks and advanced cloud kernels.",
        },
    )


@router.get("/team-members/members", response_model=list[TeamMemberResponse])
async def list_team_members():
    return await list_documents("team_members")


@admin_router.post("/team-members/members", response_model=TeamMemberResponse, status_code=status.HTTP_201_CREATED)
async def create_team_member(payload: TeamMemberCreate):
    return await create_document("team_members", payload.model_dump())


@admin_router.put("/team-members/members/{member_id}", response_model=TeamMemberResponse)
async def update_team_member(member_id: str, payload: TeamMemberUpdate):
    return await update_document("team_members", member_id, payload.model_dump(), "Team member not found")


@admin_router.delete("/team-members/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_team_member(member_id: str):
    await delete_document("team_members", member_id, "Team member not found")
    return None


@router.get("/team-members/settings", response_model=TeamSettingsResponse)
async def get_team_settings():
    return await get_settings_document(
        "team_settings",
        "team_members",
        {
            "_id": "team_members",
            "title": "The Architects",
            "subtitle": "A team of visionaries, engineers, and researchers dedicated to the pursuit of super-intelligence.",
            "cta_label": "Full Team History",
            "cta_link": "#careers",
        },
    )


@admin_router.put("/team-members/settings", response_model=TeamSettingsResponse)
async def update_team_settings(payload: TeamSettingsUpdate):
    return await upsert_settings_document(
        "team_settings",
        "team_members",
        payload.model_dump(),
        {
            "_id": "team_members",
            "title": "The Architects",
            "subtitle": "A team of visionaries, engineers, and researchers dedicated to the pursuit of super-intelligence.",
            "cta_label": "Full Team History",
            "cta_link": "#careers",
        },
    )


@router.get("/who-we-are/settings", response_model=WhoWeAreSettingsResponse)
async def get_who_we_are_settings():
    return await get_settings_document(
        "who_we_are_settings",
        "who_we_are",
        {
            "_id": "who_we_are",
            "tag": "WHO WE ARE",
            "title": "We are a collective of digital engineers, designers, and systems architects.",
            "description": "At Blacksoft, we build high-fidelity software products, autonomous agent layers, and scalable cloud infrastructure for startups and modern companies.",
            "highlight1Num": "50+",
            "highlight1Label": "Intelligent Systems Shipped",
            "highlight2Num": "99.9%",
            "highlight2Label": "SLA System Availability",
            "highlight3Num": "24/7",
            "highlight3Label": "Continuous Optimization",
        },
    )


@admin_router.put("/who-we-are/settings", response_model=WhoWeAreSettingsResponse)
async def update_who_we_are_settings(payload: WhoWeAreSettingsUpdate):
    return await upsert_settings_document(
        "who_we_are_settings",
        "who_we_are",
        payload.model_dump(),
        {
            "_id": "who_we_are",
            "tag": "WHO WE ARE",
            "title": "We are a collective of digital engineers, designers, and systems architects.",
            "description": "At Blacksoft, we build high-fidelity software products, autonomous agent layers, and scalable cloud infrastructure for startups and modern companies.",
            "highlight1Num": "50+",
            "highlight1Label": "Intelligent Systems Shipped",
            "highlight2Num": "99.9%",
            "highlight2Label": "SLA System Availability",
            "highlight3Num": "24/7",
            "highlight3Label": "Continuous Optimization",
        },
    )


@router.get("/stats/settings", response_model=StatsSettingsResponse)
async def get_stats_settings():
    return await get_settings_document(
        "stats_settings",
        "stats",
        {
            "_id": "stats",
            "stat1Value": "",
            "stat1Label": "",
            "stat1Description": "",
            "stat2Value": "",
            "stat2Label": "",
            "stat2Description": "",
            "stat3Value": "",
            "stat3Label": "",
            "stat3Description": "",
        },
    )


@admin_router.put("/stats/settings", response_model=StatsSettingsResponse)
async def update_stats_settings(payload: StatsSettingsUpdate):
    return await upsert_settings_document(
        "stats_settings",
        "stats",
        payload.model_dump(),
        {
            "_id": "stats",
            "stat1Value": "",
            "stat1Label": "",
            "stat1Description": "",
            "stat2Value": "",
            "stat2Label": "",
            "stat2Description": "",
            "stat3Value": "",
            "stat3Label": "",
            "stat3Description": "",
        },
    )


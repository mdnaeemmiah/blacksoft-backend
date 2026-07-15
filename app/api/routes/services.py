from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from app.db.mongodb import get_db
from app.models.common import as_object_id, stringify_object_id
from app.core.security import require_dashboard_user
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate
from app.schemas.dashboard import WhoWeAreSettingsResponse

router = APIRouter(prefix="/services", tags=["Services"])


@router.get("", response_model=list[ServiceResponse])
async def list_services():
    db = get_db()
    items = []
    async for document in db.services.find().sort("_id", -1):
        items.append(stringify_object_id(document))
    return items


@router.post("", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_dashboard_user)])
async def create_service(payload: ServiceCreate):
    db = get_db()
    result = await db.services.insert_one(payload.model_dump())
    document = await db.services.find_one({"_id": result.inserted_id})
    if document is None:
        raise HTTPException(status_code=500, detail="Failed to create service card")
    return stringify_object_id(document)


@router.put("/{service_id}", response_model=ServiceResponse, dependencies=[Depends(require_dashboard_user)])
async def update_service(service_id: str, payload: ServiceUpdate):
    db = get_db()
    try:
        object_id = as_object_id(service_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid service id")

    update_data = {key: value for key, value in payload.model_dump().items() if value is not None}
    if not update_data:
        document = await db.services.find_one({"_id": object_id})
        if document is None:
            raise HTTPException(status_code=404, detail="Service not found")
        return stringify_object_id(document)

    result = await db.services.update_one({"_id": object_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Service not found")

    document = await db.services.find_one({"_id": object_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return stringify_object_id(document)


@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_dashboard_user)])
async def delete_service(service_id: str):
    db = get_db()
    try:
        object_id = as_object_id(service_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid service id")

    result = await db.services.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Service not found")
    return None


@router.get("/who-we-are/settings", response_model=WhoWeAreSettingsResponse)
async def get_public_who_we_are_settings():
    db = get_db()
    document = await db.who_we_are_settings.find_one({"_id": "who_we_are"})
    if document is None:
        return {
            "id": "who_we_are",
            "tag": "WHO WE ARE",
            "title": "We are a collective of digital engineers, designers, and systems architects.",
            "description": "At Blacksoft, we build high-fidelity software products, autonomous agent layers, and scalable cloud infrastructure for startups and modern companies.",
            "highlight1Num": "50+",
            "highlight1Label": "Intelligent Systems Shipped",
            "highlight2Num": "99.9%",
            "highlight2Label": "SLA System Availability",
            "highlight3Num": "24/7",
            "highlight3Label": "Continuous Optimization",
        }
    doc = dict(document)
    doc["id"] = str(doc.pop("_id"))
    return doc

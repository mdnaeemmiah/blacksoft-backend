from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from app.db.mongodb import get_db
from app.models.common import as_object_id, stringify_object_id
from app.schemas.why_us import WhyUsCreate, WhyUsResponse, WhyUsUpdate
from app.core.security import require_dashboard_user

router = APIRouter(prefix="/why-us", tags=["Why Us"])


@router.get("", response_model=list[WhyUsResponse])
async def list_why_us():
    db = get_db()
    items = []
    async for document in db.why_us.find().sort("_id", -1):
        items.append(stringify_object_id(document))
    return items


@router.post("", response_model=WhyUsResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_dashboard_user)])
async def create_why_us(payload: WhyUsCreate):
    db = get_db()
    result = await db.why_us.insert_one(payload.model_dump())
    document = await db.why_us.find_one({"_id": result.inserted_id})
    if document is None:
        raise HTTPException(status_code=500, detail="Failed to create Why Us card")
    return stringify_object_id(document)


@router.put("/{card_id}", response_model=WhyUsResponse, dependencies=[Depends(require_dashboard_user)])
async def update_why_us(card_id: str, payload: WhyUsUpdate):
    db = get_db()
    try:
        object_id = as_object_id(card_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid card id")

    update_data = {key: value for key, value in payload.model_dump().items() if value is not None}
    if not update_data:
        document = await db.why_us.find_one({"_id": object_id})
        if document is None:
            raise HTTPException(status_code=404, detail="Card not found")
        return stringify_object_id(document)

    result = await db.why_us.update_one({"_id": object_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Card not found")

    document = await db.why_us.find_one({"_id": object_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return stringify_object_id(document)


@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_dashboard_user)])
async def delete_why_us(card_id: str):
    db = get_db()
    try:
        object_id = as_object_id(card_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid card id")

    result = await db.why_us.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Card not found")
    return None

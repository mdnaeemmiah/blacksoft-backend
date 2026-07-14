from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from app.db.mongodb import get_db
from app.models.common import as_object_id, stringify_object_id
from app.schemas.capability import CapabilityCreate, CapabilityResponse, CapabilityUpdate
from app.core.security import require_dashboard_user

router = APIRouter(prefix="/capabilities", tags=["Capabilities"])


@router.get("", response_model=list[CapabilityResponse])
async def list_capabilities():
    db = get_db()
    items = []
    async for document in db.capabilities.find().sort("_id", -1):
        items.append(stringify_object_id(document))
    return items


@router.post("", response_model=CapabilityResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_dashboard_user)])
async def create_capability(payload: CapabilityCreate):
    db = get_db()
    result = await db.capabilities.insert_one(payload.model_dump())
    document = await db.capabilities.find_one({"_id": result.inserted_id})
    if document is None:
        raise HTTPException(status_code=500, detail="Failed to create capability")
    return stringify_object_id(document)


@router.put("/{capability_id}", response_model=CapabilityResponse, dependencies=[Depends(require_dashboard_user)])
async def update_capability(capability_id: str, payload: CapabilityUpdate):
    db = get_db()
    try:
        object_id = as_object_id(capability_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid capability id")

    update_data = {key: value for key, value in payload.model_dump().items() if value is not None}
    if not update_data:
        document = await db.capabilities.find_one({"_id": object_id})
        if document is None:
            raise HTTPException(status_code=404, detail="Capability not found")
        return stringify_object_id(document)

    result = await db.capabilities.update_one({"_id": object_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Capability not found")

    document = await db.capabilities.find_one({"_id": object_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Capability not found")
    return stringify_object_id(document)


@router.delete("/{capability_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_dashboard_user)])
async def delete_capability(capability_id: str):
    db = get_db()
    try:
        object_id = as_object_id(capability_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid capability id")

    result = await db.capabilities.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Capability not found")
    return None

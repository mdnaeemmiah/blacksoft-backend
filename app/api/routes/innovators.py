from fastapi import APIRouter, HTTPException, status

from app.db.mongodb import get_db
from app.models.common import as_object_id, stringify_object_id
from app.schemas.innovator import InnovatorCreate, InnovatorResponse, InnovatorUpdate

router = APIRouter(prefix="/innovators", tags=["Trusted Innovators"])


@router.get("", response_model=list[InnovatorResponse])
async def list_innovators():
    db = get_db()
    items = []
    async for document in db.innovators.find().sort("_id", -1):
        items.append(stringify_object_id(document))
    return items


@router.post("", response_model=InnovatorResponse, status_code=status.HTTP_201_CREATED)
async def create_innovator(payload: InnovatorCreate):
    db = get_db()
    result = await db.innovators.insert_one(payload.model_dump())
    document = await db.innovators.find_one({"_id": result.inserted_id})
    if document is None:
        raise HTTPException(status_code=500, detail="Failed to create innovator")
    return stringify_object_id(document)


@router.put("/{innovator_id}", response_model=InnovatorResponse)
async def update_innovator(innovator_id: str, payload: InnovatorUpdate):
    db = get_db()
    try:
        object_id = as_object_id(innovator_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid innovator id")

    update_data = {key: value for key, value in payload.model_dump().items() if value is not None}
    if not update_data:
        document = await db.innovators.find_one({"_id": object_id})
        if document is None:
            raise HTTPException(status_code=404, detail="Innovator not found")
        return stringify_object_id(document)

    result = await db.innovators.update_one({"_id": object_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Innovator not found")

    document = await db.innovators.find_one({"_id": object_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Innovator not found")
    return stringify_object_id(document)


@router.delete("/{innovator_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_innovator(innovator_id: str):
    db = get_db()
    try:
        object_id = as_object_id(innovator_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid innovator id")

    result = await db.innovators.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Innovator not found")
    return None

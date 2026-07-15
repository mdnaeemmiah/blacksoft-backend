from __future__ import annotations

import secrets
from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from app.core.security import require_dashboard_user
from app.db.mongodb import get_db
from app.schemas.booking import BookingCreate, BookingResponse, BookingStatusUpdate

router = APIRouter(prefix="/bookings", tags=["Bookings"])


def _serialize(doc: dict) -> dict:
    return {
        "id": str(doc["_id"]),
        # contact
        "name": doc["name"],
        "email": doc["email"],
        "phone": doc.get("phone"),
        "company": doc.get("company"),
        "country": doc.get("country"),
        # project
        "project_type": doc.get("project_type"),
        "budget_range": doc.get("budget_range"),
        "timeline": doc.get("timeline"),
        "tech_stack": doc.get("tech_stack"),
        "team_size": doc.get("team_size"),
        "has_design": doc.get("has_design"),
        # request
        "preferred_datetime": doc.get("preferred_datetime"),
        "how_heard": doc.get("how_heard"),
        "message": doc.get("message"),
        # meta
        "status": doc.get("status", "new"),
        "created_at": doc["created_at"],
    }


# ─── Public: submit a booking from the website ────────────────────────────────

@router.post("", status_code=status.HTTP_201_CREATED, response_model=BookingResponse)
async def create_booking(payload: BookingCreate):
    doc = {
        "_id": ObjectId(),
        # contact
        "name": payload.name.strip(),
        "email": payload.email.strip().lower(),
        "phone": payload.phone,
        "company": payload.company,
        "country": payload.country,
        # project
        "project_type": payload.project_type,
        "budget_range": payload.budget_range,
        "timeline": payload.timeline,
        "tech_stack": payload.tech_stack,
        "team_size": payload.team_size,
        "has_design": payload.has_design,
        # request
        "preferred_datetime": payload.preferred_datetime,
        "how_heard": payload.how_heard,
        "message": payload.message,
        # meta
        "status": "new",
        "created_at": datetime.now(timezone.utc),
    }
    await get_db().bookings.insert_one(doc)
    return _serialize(doc)


# ─── Protected: dashboard only ─────────────────────────────────────────────────

@router.get("", response_model=list[BookingResponse], dependencies=[Depends(require_dashboard_user)])
async def list_bookings():
    cursor = get_db().bookings.find().sort("created_at", -1)
    docs = await cursor.to_list(length=500)
    return [_serialize(d) for d in docs]


@router.patch("/{booking_id}", response_model=BookingResponse, dependencies=[Depends(require_dashboard_user)])
async def update_booking_status(booking_id: str, payload: BookingStatusUpdate):
    try:
        oid = ObjectId(booking_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid booking ID")

    result = await get_db().bookings.find_one_and_update(
        {"_id": oid},
        {"$set": {"status": payload.status}},
        return_document=True,
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return _serialize(result)


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_dashboard_user)])
async def delete_booking(booking_id: str):
    try:
        oid = ObjectId(booking_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid booking ID")

    result = await get_db().bookings.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")

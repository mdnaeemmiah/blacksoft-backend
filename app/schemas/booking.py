from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BookingCreate(BaseModel):
    # ── Contact info ──────────────────────────────────────────────
    name: str = Field(min_length=1, max_length=120)
    email: str = Field(min_length=3, max_length=320)
    phone: Optional[str] = Field(default=None, max_length=30)
    company: Optional[str] = Field(default=None, max_length=200)
    country: Optional[str] = Field(default=None, max_length=100)

    # ── Project details ───────────────────────────────────────────
    project_type: Optional[str] = Field(default=None, max_length=100)
    budget_range: Optional[str] = Field(default=None, max_length=50)
    timeline: Optional[str] = Field(default=None, max_length=50)
    tech_stack: Optional[str] = Field(default=None, max_length=300)
    team_size: Optional[str] = Field(default=None, max_length=50)
    has_design: Optional[str] = Field(default=None, max_length=50)

    # ── Request details ───────────────────────────────────────────
    preferred_datetime: Optional[str] = Field(default=None, max_length=50)
    how_heard: Optional[str] = Field(default=None, max_length=200)
    message: Optional[str] = Field(default=None, max_length=3000)


class BookingResponse(BaseModel):
    id: str
    # Contact
    name: str
    email: str
    phone: Optional[str]
    company: Optional[str]
    country: Optional[str]
    # Project
    project_type: Optional[str]
    budget_range: Optional[str]
    timeline: Optional[str]
    tech_stack: Optional[str]
    team_size: Optional[str]
    has_design: Optional[str]
    # Request
    preferred_datetime: Optional[str]
    how_heard: Optional[str]
    message: Optional[str]
    # Meta
    status: str          # "new" | "contacted" | "closed"
    created_at: datetime


class BookingStatusUpdate(BaseModel):
    status: str = Field(pattern=r"^(new|contacted|closed)$")

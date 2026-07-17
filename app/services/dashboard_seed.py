from __future__ import annotations
from app.db.mongodb import get_db

async def seed_dashboard_content() -> None:
    """
    Seeding is disabled since all production content is now managed dynamically
    via the administrator dashboard and persisted directly in the MongoDB cluster.
    """
    pass

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.dashboard import router as dashboard_router, admin_router as dashboard_admin_router
from app.api.routes.capabilities import router as capabilities_router
from app.api.routes.innovators import router as innovators_router
from app.api.routes.uploads import router as uploads_router
from app.api.routes.auth import router as auth_router
from app.api.routes.bookings import router as bookings_router
from app.api.routes.services import router as services_router
from app.api.routes.why_us import router as why_us_router
from app.core.config import get_settings
from app.db.mongodb import close_mongo_connection, connect_to_mongo
from app.services.cloudinary_service import configure_cloudinary
from app.services.dashboard_seed import seed_dashboard_content
from app.services.auth_service import create_admin_user, validate_auth_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup() -> None:
    validate_auth_settings()
    await connect_to_mongo()
    await create_admin_user()
    configure_cloudinary()
    await seed_dashboard_content()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await close_mongo_connection()


@app.get(f"{settings.api_prefix}/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}


app.include_router(capabilities_router, prefix=settings.api_prefix)
app.include_router(innovators_router, prefix=settings.api_prefix)
app.include_router(uploads_router, prefix=settings.api_prefix)
app.include_router(dashboard_router, prefix=settings.api_prefix)
app.include_router(dashboard_admin_router, prefix=settings.api_prefix)
app.include_router(auth_router, prefix=settings.api_prefix)
app.include_router(bookings_router, prefix=settings.api_prefix)
app.include_router(services_router, prefix=settings.api_prefix)
app.include_router(why_us_router, prefix=settings.api_prefix)

# MishiAi Backend

FastAPI backend for the MishiAi frontend.

## Features

- MongoDB-backed CRUD endpoints for capability cards and trusted innovators
- Cloudinary image upload endpoint
- Pydantic validation
- CORS configured for the frontend

## Run Locally

1. Copy `.env.example` to `.env`
2. Replace the MongoDB URI with your MongoDB Atlas connection string and fill in the Cloudinary values.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the API:

```bash
uvicorn app.main:app --reload
```

## API

- `GET /api/health`
- `GET /api/capabilities`
- `POST /api/capabilities`
- `PUT /api/capabilities/{id}`
- `DELETE /api/capabilities/{id}`
- `GET /api/innovators`
- `POST /api/innovators`
- `PUT /api/innovators/{id}`
- `DELETE /api/innovators/{id}`
- `POST /api/uploads/image`

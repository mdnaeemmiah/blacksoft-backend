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

The public frontend runs on port 3000 and the standalone dashboard runs on
port 3001. Both use `http://localhost:8000/api`; configure their respective
`.env` files from `.env.example` when using a different API host.

Dashboard access requires `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `JWT_SECRET`, and
working SMTP settings. Login first verifies the password, then sends a
single-use email code before issuing an expiring JWT session token. Password
reset uses the same SMTP code flow.

## Docker

Build and run the API image from this directory. Provide the environment
variables from `.env.example` through your deployment platform or `docker run`.

```bash
docker build -t mishiai-backend .
docker run --env-file .env -p 8000:8000 mishiai-backend
```

## Vercel

Vercel deploys the FastAPI application through `api/index.py`. Set the
following **Production** environment variables in the Vercel project before
deploying:

- `APP_ENV=production`
- `MONGODB_URI` and `MONGODB_DB`
- `ALLOWED_ORIGINS` with the deployed frontend and dashboard URLs, separated by commas
- `ADMIN_EMAIL`, `ADMIN_PASSWORD`, and a random `JWT_SECRET` of at least 32 characters
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `SMTP_FROM`, and `SMTP_USE_TLS`
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, and `CLOUDINARY_FOLDER` when image uploads are enabled

The MongoDB Atlas network access list must allow Vercel to connect. After
configuring the variables, redeploy and check `GET /api/health`.

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

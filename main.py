from fastapi import FastAPI
from app.api import subscriptions, ingestion, status

app = FastAPI(
    title="Webhook Delivery Service",
    description="Ingest, deliver, and track webhooks",
    version="1.0.0"
)

app.include_router(subscriptions.router, prefix="/api/subscriptions", tags=["Subscriptions"])
app.include_router(ingestion.router, prefix="/api", tags=["Webhook Ingestions"])
app.include_router(status.router, prefix="/api/status", tags=["Status"])

@app.get("/")
def read_root():
    return {"message": "Delivery service is running!"}


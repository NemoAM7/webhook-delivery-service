from fastapi import APIRouter

router = APIRouter()

@router.get("/ingestion/{subscription_id}")
def list_subscriptions(subscription_id: str):
    return {"message": f"Webhook recieved for subscription {subscription_id} (placeholder)"}

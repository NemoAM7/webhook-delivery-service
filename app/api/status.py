from fastapi import APIRouter

router = APIRouter()

@router.get("/delivery/{delivery_id}")
def list_subscriptions(delivery_id: str):
    return {"message": f"Status for delivery ID {delivery_id} (placeholder)"}

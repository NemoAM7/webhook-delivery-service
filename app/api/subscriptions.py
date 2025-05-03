from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_subscriptions():
    return {"message": f"List of all subscriptions (placeholder)"}

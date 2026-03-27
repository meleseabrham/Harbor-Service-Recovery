from fastapi import APIRouter
from app.database import get_db_status
router = APIRouter()
@router.get("/status")
def status(): return {"db": get_db_status()}

from fastapi import APIRouter

router = APIRouter(prefix="/", tags=["Examples"])


@router.get("")
def hello():
    return {"message": "Hello World", "status": "ok"}

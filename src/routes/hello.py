from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Examples"])


@router.get("/")
def hello():
    return {"message": "Hello World", "status": "ok"}

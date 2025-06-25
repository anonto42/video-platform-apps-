from server.app.modules.user import user_controller
from fastapi import APIRouter,Request

router = APIRouter()

@router.post("/")
async def register_user(
    req: Request
):
    return await user_controller.register_user(req)

@router.get("/")
async def get_user(
    req: Request
):
    return await user_controller.get_user(req)
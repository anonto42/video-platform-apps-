# import auth_controller
from fastapi import APIRouter,Request
from server.utils.send_res import send_response
from server.constants.http_status_code import HTTP_STATUS
from server.app.modules.auth import auth_controller

router = APIRouter()

@router.post("/login")
async def login(req: Request):
    return await auth_controller.login(req)
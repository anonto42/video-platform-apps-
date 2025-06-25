from server.app.modules.auth import auth_service
from fastapi import Request
from ....constants.http_status_code import HTTP_STATUS
from ....utils.send_res import send_response

async def login(req: Request):

    body = await req.json()

    # db = req.app.mongo.local.user.find()
    # print(db)

    result = await auth_service.login(body)

    return await send_response(
        True,
        "Login Successfull!",
        result,
        HTTP_STATUS.OK
    )
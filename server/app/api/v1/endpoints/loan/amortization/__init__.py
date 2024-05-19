# from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

# from app.core.container import Container
# from app.core.dependencies import get_current_super_user
# from app.core.security import JWTBearer
# from app.schema.base_schema import Blank
# from app.schema.user_schema import FindUser, FindUserResult, UpsertUser, User
# from app.services.user_service import UserService
# from app.api.v1.endpoints.user.user import get_user_now

router = APIRouter(prefix="loan/amortization", tags=["amortization"])


@router.get("/")
async def get_all_amortization():
    return


@router.get("/{username}")
async def get_all_amortization_per_user(username=None):
    return


@router.post("")
async def create_amortization():
    return ""


@router.patch("/{user_id}")
async def update_user(user_id: int):
    return ""


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return ""
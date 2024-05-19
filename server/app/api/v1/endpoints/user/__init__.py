# from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

# from app.core.container import Container
# from app.core.dependencies import get_current_super_user
# from app.core.security import JWTBearer
# from app.schema.base_schema import Blank
# from app.schema.user_schema import FindUser, FindUserResult, UpsertUser, User
# from app.services.user_service import UserService
from app.api.v1.endpoints.user.user import get_user_now

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/current_user")
async def get_current_user(user_id=None):
    return get_user_now(user_id or 'all is here')


@router.get("/{username}")
@router.get("")
async def get_users(username=None):
    return get_user_now(username)


@router.post("")
async def create_user():
    return ""


@router.patch("/{username}")
async def update_user(username=None):
    return ""


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return ""
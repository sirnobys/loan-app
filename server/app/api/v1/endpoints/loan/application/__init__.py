# from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

# from app.core.container import Container
# from app.core.dependencies import get_current_super_user
# from app.core.security import JWTBearer
# from app.schema.base_schema import Blank
# from app.schema.user_schema import FindUser, FindUserResult, UpsertUser, User
# from app.services.user_service import UserService
# from app.api.v1.endpoints.user.user import get_user_now

router = APIRouter(prefix="/loan/application", tags=["loan application"])


@router.get("")
@router.get("/{loan_application_id}")
async def get_loan_applications(loan_application_id=None):
    return


@router.get("/user/{username}")
async def get_loan_applications_by_user(username=None):
    return


@router.post("/apply")
async def create_loan_application():
    return ""


@router.patch("/{loan_application_id}")
async def update_loan_application(loan_application_id: int):
    return ""


@router.patch("/{loan_application_id}/cancel")
async def cancel_loan_application(loan_application_id: int):
    return ""


@router.delete("/{loan_application_id}/delete")
async def delete_loan_application(loan_application_id: int):
    return ""
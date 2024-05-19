# from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

# from app.core.container import Container
# from app.core.dependencies import get_current_super_user
# from app.core.security import JWTBearer
# from app.schema.base_schema import Blank
# from app.schema.user_schema import FindUser, FindUserResult, UpsertUser, User
# from app.services.user_service import UserService
# from app.api.v1.endpoints.user.user import get_user_now

router = APIRouter(prefix="/loan/payment", tags=["loan payment"])


@router.get("")
@router.get("/{loan_application_id}")
async def get_loan_applications(payment_id=None):
    return


@router.get("/user/{username}")
async def get_loan_applications_by_user(username=None):
    return


@router.post("/apply")
async def create_loan_application():
    return ""


@router.patch("/{payment_id}")
async def update_loan_application(loan_application_id: int):
    return ""


@router.patch("/{payment_id}/cancel")
async def cancel_loan_application(payment_id: int):
    return ""


@router.delete("/{payment_id}/delete")
async def delete_loan_application(loan_application_id: int):
    return ""
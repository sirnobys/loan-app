from fastapi import APIRouter

# from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.loan.application import router as loan_application_router
from app.api.v1.endpoints.loan.payment import router as loan_payment_router
from app.api.v1.endpoints.loan.loan import router as loans_router
from app.api.v1.endpoints.user import router as user_router

routers = APIRouter()
router_list = [user_router, loans_router, loan_application_router, loan_payment_router]

for router in router_list:
    # router.tags = routers.tags.append("v1")
    routers.include_router(router)
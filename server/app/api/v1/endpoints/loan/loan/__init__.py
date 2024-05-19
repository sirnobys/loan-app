from fastapi import APIRouter, Depends

router = APIRouter(prefix="/loan/type", tags=["loan"])


@router.get("/all")
async def get_all_loan_types():
    return ""


@router.get("/{loan_name}")
async def get_loan_type(
    loan_name: int):
    return ""


@router.post("/create", )
async def create_loan_type():
    return ""


@router.patch("/{loan_name}")
async def update_loan(user_id: int):
    return ""

@router.delete("/{loan_name}/delete")
async def delete_loan(user_id: int):
    return ""
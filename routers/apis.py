from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}},)



@router.get("/test")
async def read_items():
    return {"message": "Fetch working :-)"}

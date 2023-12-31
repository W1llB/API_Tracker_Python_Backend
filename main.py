# from typing import Annotated
from fastapi import FastAPI
from routers import apis
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000"
]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
]
app = FastAPI(middleware=middleware)

app.include_router(apis.router)

@app.get("/")
async def root():
    return {"message": "Hello there big man"}
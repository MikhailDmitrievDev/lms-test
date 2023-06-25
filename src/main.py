from fastapi import FastAPI

from auth.router import router as auth_router
app = FastAPI(
    title="LMS-PROJECT",
    version="0.1"
)

app.include_router(
    router=auth_router,
    prefix="/api/v1",
)

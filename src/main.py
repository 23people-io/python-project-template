from fastapi import FastAPI

from routes.hello import router as hello_router
from routes.users import router as users_router

app = FastAPI(
    title="Python Project Template API",
    version="1.0.0",
)

app.include_router(hello_router)
app.include_router(users_router)

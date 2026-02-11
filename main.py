from fastapi import FastAPI

from routes.examples import router as api_router

app = FastAPI(
    title="Python Project Template API",
    version="1.0.0",
)

app.include_router(api_router)

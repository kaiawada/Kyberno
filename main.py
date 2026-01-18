from fastapi import FastAPI
from app.api.endpoints import pump
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# 登録作業のみ
app.include_router(pump.router, prefix="/pump", tags=["Pump"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.risk.routes import router as risk_router
from app.reports.routes import router as report_router

app = FastAPI(title="Check Insurance Risk API", version="2.0")

app.include_router(auth_router, prefix="/api", tags=["Auth"])
app.include_router(risk_router, prefix="/api", tags=["Risk"])
app.include_router(report_router, prefix="/api", tags=["Reports"])

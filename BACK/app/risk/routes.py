from fastapi import APIRouter
from app.risk.schemas import RiskCheckRequest, RiskCheckResponse

router = APIRouter()

@router.post("/risk-check", response_model=RiskCheckResponse)
def risk_check(request: RiskCheckRequest):
    score = 72.5
    return RiskCheckResponse(
        risk_request_id=981,
        score=score,
        risk_level="ALTO",
        pep_matches=[{"source": "PEP_DB", "name": request.subject_name, "confidence": 0.91}],
        sanctions_matches=[{"list": "OFAC", "name": request.subject_name, "confidence": 0.78}],
        red_flags=["Exposição política (PEP)", "Match parcial em lista de sanções internacionais"]
    )

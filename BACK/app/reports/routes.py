from fastapi import APIRouter
from app.reports.schemas import ReportRequest, ReportResponse

router = APIRouter()

@router.post("/generate-report", response_model=ReportResponse)
def generate_report(request: ReportRequest):
    return ReportResponse(
        risk_request_id=request.risk_request_id,
        report_type="Premium v3",
        format=request.format,
        download_url=f"/files/reports/{request.risk_request_id}_premium_v3.{request.format}",
        generated_at="2025-10-25T20:18:00Z"
    )

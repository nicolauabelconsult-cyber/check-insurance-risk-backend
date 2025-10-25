from pydantic import BaseModel

class ReportRequest(BaseModel):
    risk_request_id: int
    format: str = "pdf"

class ReportResponse(BaseModel):
    risk_request_id: int
    report_type: str
    format: str
    download_url: str
    generated_at: str

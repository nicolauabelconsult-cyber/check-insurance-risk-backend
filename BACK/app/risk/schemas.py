from pydantic import BaseModel
from typing import List, Dict

class RiskCheckRequest(BaseModel):
    subject_name: str
    subject_doc_id: str | None = None
    subject_dob: str | None = None
    subject_type: str = "individual"
    extra_info: dict | None = None

class RiskCheckResponse(BaseModel):
    risk_request_id: int
    score: float
    risk_level: str
    pep_matches: List[Dict]
    sanctions_matches: List[Dict]
    red_flags: List[str]

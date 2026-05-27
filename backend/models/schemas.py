from pydantic import BaseModel
from typing import Optional, List


class DiagnosisResponse(BaseModel):
    error_type: Optional[str]
    probable_root_cause: str
    suggested_fixes: List[str]
    confidence: float
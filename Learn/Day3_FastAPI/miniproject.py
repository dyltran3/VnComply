from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class ScanType(str, Enum):
    privacy = "privacy"
    security = "security"

app = FastAPI()

# Giả lập Database
fake_db = []

# Định nghĩa Model
class ScanCreate(BaseModel):
    target_url: str
    scan_type: ScanType # privacy / security

class ScanResponse(BaseModel):
    id: int
    target_url: str
    scan_type: ScanType
    status: str="queued"



@app.post("/scans", response_model=ScanResponse)
def create_scan(scan: ScanCreate):
        new_scan = ScanResponse(
            id=len(fake_db) + 1,# tụ tăng id
            target_url=scan.target_url,
            scan_type=scan.scan_type,
            status="queued"
        )
        fake_db.append(new_scan)
        return new_scan

@app.get("/scans", response_model=List[ScanResponse])
def list_scans(status: Optional[str] = None):
        if status is None:
            return fake_db
        result = []
        for scan in fake_db:
            if scan.status == status:
                result.append(scan)
        return result
    
@app.get("/scans/{scan_id}", response_model=ScanResponse)
def get_scan(scan_id: int):
        for scan in fake_db:
            if scan.id == scan_id:
                return scan
        raise HTTPException(status_code=404, detail="Scan not found")
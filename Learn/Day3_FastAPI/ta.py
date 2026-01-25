from fastapi import FastAPI , HTTPException , Query
from pydantic import BaseModel, Field
from typing import List, Optional
import random
app = FastAPI()

fake_db =  [] 

class ScanCreate(BaseModel):
    target_url: str
    scan_type: str

class ScanResponse(BaseModel):
    id: int
    target_url: str
    scan_type: str
    status: str 

def generate_id():
    return random.randint(1000,9999)


@app.post("/scans", response_model=ScanResponse)
def create_scan (scan: ScanCreate):
    new_job = { 
        "id": generate_id(),
        "target_url": scan.target_url,
        "scan_type": scan.scan_type,
        "status": "queued"
    }
    fake_db.append(new_job)
    return new_job

@app.get("/scans", response_model = List[ScanResponse])
def get_scans (status: Optional[str] = Query(None)):
    if status:
        return [job for job in fake_db if job ["status"] == status ] 
    
    return fake_db

@app.get("/scans/{scan_id}", response_model= ScanResponse)
def get_scan(scan_id: int): 
    for job in fake_db:
        if job["id"] == scan_id:
            return job
    raise HTTPException(status_code=404 , detail="Scan Job Not Found")


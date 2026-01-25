from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello": "World"}

 # bai tap 1
@app.get("/health")
def health_check():
    return {"status": "active", "version": "1.0.0"}

 # bai tap 2 
@app.get("/users/{username}")
def read_user(username: str):
    return {"username": username, "role": "admin"}

# bai tap 3
@app.get("/scans")
def get_scans(scan_type:str,status:str="pending"):
    return {"scan_type": scan_type, "status": status}

# bai tap 4
from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register")
def register_user(user: UserCreate):
    return {"message": "Đăng ký thành công", "user": {"username": user.username, "email": user.email}}
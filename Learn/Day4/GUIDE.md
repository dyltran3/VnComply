# HƯỚNG DẪN TỰ HỌC - NGÀY 4: XÂY DỰNG HỆ THỐNG BACKEND CHUYÊN NGHIỆP

Chào mừng bạn đến với ngày thứ 4! Hôm nay chúng ta sẽ chuyển mình từ việc viết các script nhỏ lẻ sang việc xây dựng một hệ thống Backend hoàn chỉnh, có khả năng lưu trữ dữ liệu bền vững, bảo mật người dùng và sẵn sàng để triển khai thực tế.

---

## 🏗️ MODULE 1: DATABASE FUNDAMENTALS (CƠ SỞ DỮ LIỆU)

### 1.1 SQLAlchemy ORM: Cầu nối giữa Python và Database

**Khái niệm dễ hiểu:**
Trong lập trình Backend, ta có hai thế giới: thế giới **Đối tượng (Object)** của Python và thế giới **Bảng (Table)** của SQL.

- **ORM (Object-Relational Mapping)** là "người phiên dịch" giúp bạn thao tác với Database bằng code Python mà không cần viết các câu lệnh SQL thô (Raw SQL).

**Phân tích so sánh:**

- **Raw SQL (Cách cũ):** `cursor.execute("SELECT * FROM users WHERE id = 1")`. Khó quản lý, dễ lỗi chính tả câu lệnh SQL.
- **ORM (Cách mới):** `db.query(User).filter(User.id == 1).first()`. Code sạch, có gợi ý (Intellisense) và cực kỳ an toàn.

**Lợi ích:**

- **Type Safety:** Python hiểu rõ dữ liệu của bạn là số hay chữ.
- **Bảo mật:** Tự động ngăn chặn tấn công **SQL Injection** (hacker chèn lệnh độc hại).
- **Database Agnostic:** Dễ dàng đổi từ SQLite sang PostgreSQL mà không cần sửa lại code xử lý dữ liệu.

### 1.2 Định nghĩa Models (Xây dựng cấu trúc dữ liệu)

Models là nơi bạn vẽ ra "bản thiết kế" cho các bảng trong Database.

**Ví dụ thực tế (`Learn/Day4/examples/models.py`):**

```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users" # Tên bảng trong DB

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ One-to-Many: 1 User có nhiều ScanJob
    scans = relationship("ScanJob", back_populates="owner")

class ScanJob(Base):
    __tablename__ = "scan_jobs"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), nullable=False)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id")) # Khóa ngoại liên kết tới User

    # Liên kết ngược lại
    owner = relationship("User", back_populates="scans")
```

### 1.3 Engine & Session (Hệ thống điều hành)

- **Engine:** Trạm bơm kết nối tới Database.
- **Session:** Một phiên làm việc (giống như một giỏ hàng, bạn thêm bớt dữ liệu rồi bấm "Thanh toán" - Commit).

**Ví dụ cấu hình kết nối (`Learn/Day4/examples/database.py`):**

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./app.db" # Đơn giản cho việc học

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency: Giúp FastAPI tự động cấp/đóng DB cho mỗi Request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 🔄 MODULE 2: ALEMBIC MIGRATIONS (QUẢN LÝ PHIÊN BẢN DB)

**Giải thích dễ hiểu:**
Hãy coi Alembic như **Git cho Database**.
Khi bạn thêm một cột mới vào code Python (Model), Database thật sự chưa có cột đó. Alembic sẽ giúp bạn:

1. Tạo ra một file "kịch bản" (Migration script) mô tả sự thay đổi.
2. Chạy kịch bản đó để cập nhật Database mà không làm mất dữ liệu cũ.

**Lệnh quan trọng:**

- `alembic revision --autogenerate -m "Add avatar to user"`: Tự động tạo kịch bản thay đổi.
- `alembic upgrade head`: Áp dụng thay đổi mới nhất vào Database.

---

## 🔐 MODULE 3: AUTHENTICATION & AUTHORIZATION (BẢO MẬT)

### 3.1 Password Hashing (Mật mã hóa)

**QUY TẮC VÀNG:** Tuyệt đối không lưu mật khẩu thô vào Database.
Chúng ta thường dùng `bcrypt` – một thuật toán "băm" mật khẩu một chiều. (Trong phần code mẫu bên dưới, chúng tôi đơn giản hóa bằng một chuỗi tạm để bạn dễ nắm bắt luồng dữ liệu).

### 3.2 JWT (JSON Web Token)

**Ví dụ dễ hiểu:** Token giống như cái **Vòng tay của quán Buffet**.

1. Bạn đăng nhập thành công (Thanh toán tiền).
2. Server tặng bạn một cái Vòng tay (JWT).
3. Lần sau bạn đi lấy đồ ăn (Gọi API), bạn chỉ cần đưa Vòng tay ra, không cần phải trình lại CCCD (Username/Password) nữa.

---

## 🛡️ MODULE 4: SECURITY BEST PRACTICES (BẢO MẬT NÂNG CAO)

### 4.1 Environment Variables (.env)

Đừng bao giờ viết "bí mật" (Mật khẩu DB, Secret Key) trực tiếp vào code. Hãy lưu chúng trong file `.env`.
_Tại sao?_ Vì khi bạn đẩy code lên Github, file `.env` sẽ được bỏ qua (gitignore), bí mật của bạn sẽ an toàn.

### 4.2 CORS (Cross-Origin Resource Sharing)

Đây là "người gác cổng" của Browser. Nó quy định những website nào (ví dụ: `localhost:3000`) được phép gọi API tới Server của bạn.

---

## � MODULE 5: DOCKER & DEPLOYMENT (ĐÓNG GÓI & TRIỂN KHAI)

**Giải thích dễ hiểu:**
Docker giúp tạo ra một "chiếc hộp" chứa ứng dụng của bạn cùng tất cả những thứ nó cần (Python, thư viện, DB).

- **Lợi ích:** "Chạy tốt trên máy tôi thì cũng sẽ chạy tốt trên máy của khách hàng". Bạn không cần lo lắng về việc máy khác thiếu thư viện này hay cài sai phiên bản kia.

**File `Dockerfile` mẫu:**

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📂 MODULE 6: PROJECT STRUCTURE (CẤU TRÚC DỰ ÁN CHUẨN)

Một dự án chuyên nghiệp cần sự ngăn nắp:

- `app/api/`: Các đường dẫn API.
- `app/models/`: Cấu trúc Database.
- `app/schemas/`: Quy định dữ liệu đầu vào/đầu ra (Pydantic).
- `app/crud/`: Các hàm xử lý dữ liệu (Thêm, xóa, sửa).

---

## 🧪 MODULE 7: TESTING (KIỂM THỬ)

Đừng đợi đến lúc khách hàng báo lỗi mới đi sửa. Hãy viết code để "tự kiểm tra" code của mình bằng `pytest`. Việc này giúp bạn tự tin hơn mỗi khi thêm tính năng mới mà không sợ làm hỏng những thứ cũ.

---

## 🚀 MODULE 8: MINI PROJECT (XÂY DỰNG API THỰC TẾ)

Chúng ta sẽ kết hợp tất cả kiến thức trên để xây dựng ứng dụng **VnComply API**:

- Cho phép người dùng đăng ký/đăng nhập.
- Quản lý các phiên quét bảo mật (Scan Jobs).
- Lưu trữ kết quả quét vào Database.

### **File Ví dụ: `Learn/Day4/examples/main.py` hoàn chỉnh**

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# Khởi tạo DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="VnComply Professional API")

@app.get("/")
def read_root():
    return {"message": "Welcome to VnComply API"}

@app.post("/scans/", response_model=schemas.ScanResponse)
def create_new_scan(scan: schemas.ScanCreate, user_id: int, db: Session = Depends(get_db)):
    """API Tạo mới một phiên quét"""
    return crud.create_scan_job(db=db, scan=scan, user_id=user_id)
```

---

## � CHECKLIST CUỐI NGÀY

- [ ] Bạn đã hiểu tại sao phải dùng ORM chưa?
- [ ] Bạn đã chạy thử lệnh Alembic nào chưa?
- [ ] Bạn đã có file `.env` cho dự án của mình chưa?
- [ ] Bạn đã cài đặt Docker trên máy chưa?

---

## 📂 HƯỚNG DẪN SỬ DỤNG CÁC FILE VÍ DỤ

Để giúp bạn thực hành tốt nhất, tôi đã chuẩn bị sẵn bộ code mẫu hoàn chỉnh trong thư mục `examples/`. Các file này được thiết kế để hoạt động cùng nhau:

1.  **`database.py`**: Cấu hình kết nối SQLAlchemy (Cái ống dẫn).
2.  **`models.py`**: Định nghĩa cấu trúc các bảng (Bản thiết kế).
3.  **`schemas.py`**: Quy định kiểu dữ liệu Input/Output (Pydantic).
4.  **`crud.py`**: Các hàm xử lý dữ liệu Thêm, Đọc, Sửa, Xóa (Thao tác thực tế).
5.  **`main.py`**: File chạy chính của ứng dụng FastAPI (Trung tâm điều khiển).

**Cách chạy thử:**
Bạn mở terminal tại thư mục gốc dự án và gõ:

```bash
python -m uvicorn Learn.Day4.examples.main:app --reload
```

---

_Chúc bạn có một ngày học tập thật hiệu quả! Đừng ngần ngại đặt câu hỏi nếu có bất kỳ chỗ nào chưa rõ nhé. 🚀_

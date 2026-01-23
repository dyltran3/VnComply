# Hướng dẫn Học tập Ngày 1: Làm quen với FastAPI

Chào mừng bạn đến với ngày đầu tiên trong chuỗi bài học xây dựng nền tảng kỹ thuật cho dự án **VNComply**. Hôm nay, chúng ta sẽ tập trung vào **FastAPI** - framework được chọn để xây dựng Application Tier (Backend) cho hệ thống.

**Mục tiêu hôm nay:**

- Hiểu FastAPI là gì và tại sao chúng ta sử dụng nó.
- Cài đặt môi trường phát triển.
- Nắm vững các khái niệm cơ bản: Path Params, Query Params, Request Body.
- Sử dụng Pydantic để kiểm tra dữ liệu.
- **Micro-Project:** Xây dựng API đơn giản quản lý các "Scan Job" (tác vụ quét).

---

## 1. Giới thiệu về FastAPI

Theo tài liệu kiến trúc của VNComply (Mục VIII), hệ thống sử dụng **FastAPI Servers (Stateless)**.
FastAPI là một web framework hiện đại, hiệu năng cao để xây dựng API bằng Python 3.8+.

**Tại sao lại là FastAPI?**

1.  **Nhanh (High Performance):** Ngang ngửa với NodeJS và Go, nhờ sử dụng Starlette và Pydantic.
2.  **Dễ code:** Giảm thiểu bug, code ngắn gọn, trực quan.
3.  **Tự động tạo document:** Tự động sinh ra Swagger UI (`/docs`) và ReDoc - cực kỳ tiện lợi cho việc test và tích hợp với Frontend.
4.  **Async/Await:** Hỗ trợ lập trình bất đồng bộ (asynchronous) mặc định, rất quan trọng cho các tác vụ I/O heavy như gọi scan engine hay query DB.

---

## 2. Cài đặt Môi trường

Trước khi bắt đầu, hãy tạo một thư mục riêng cho code bài học này (bạn có thể code trực tiếp trong thư mục `Learn/Day1_FastAPI`).

### Bước 1: Tạo môi trường ảo (Virtual Environment)

Mở terminal tại thư mục `Learn/Day1_FastAPI` và chạy:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```

### Bước 2: Cài đặt thư viện

Chúng ta cần `fastapi` và `uvicorn` (server để chạy ứng dụng).

```bash
pip install fastapi uvicorn
```

---

## 3. Kiến thức Cốt lõi & Bài tập

### Phần 1: Hello World - API đầu tiên

Tạo file `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chào mừng đến với VNComply Learning"}
```

**Chạy server:**

```bash
uvicorn main:app --reload
```

_Ghi chú: `--reload` giúp server tự khởi động lại khi bạn sửa code._

Truy cập `http://127.0.0.1:8000` để thấy kết quả.
Truy cập `http://127.0.0.1:8000/docs` để xem giao diện Swagger UI.

**⚡ Bài tập nhỏ 1:**
Thêm một endpoint `GET /health` trả về JSON `{"status": "active", "version": "1.0.0"}`. Kiểm tra nó trên Swagger UI.

---

### Phần 2: Path Parameters (Tham số đường dẫn)

Dùng để lấy dữ liệu cụ thể, ví dụ lấy thông tin user theo ID.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

_Lưu ý: Khai báo `item_id: int` giúp FastAPI tự động validate. Nếu bạn nhập chữ vào ID, API sẽ báo lỗi tự động._

**⚡ Bài tập nhỏ 2:**
Viết endpoint `GET /users/{username}` trả về `{"username": username, "role": "admin"}`. Thử nhập một username bất kỳ trên trình duyệt.

---

### Phần 3: Query Parameters (Tham số truy vấn)

Là các tham số sau dấu `?` trên URL, thường dùng để lọc hoặc phân trang.

```python
# Ví dụ: GET /search?keyword=compliance&limit=10
@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}
```

**⚡ Bài tập nhỏ 3:**
Viết endpoint `GET /scans` nhận vào tham số `scan_type` (ví dụ: "privacy" hoặc "security") và `status` (mặc định là "pending"). Trả về JSON chứa các tham số đó.

---

### Phần 4: Request Body & Pydantic (Gửi dữ liệu lên)

Để gửi dữ liệu phức tạp (như thông tin tạo Scan mới), chúng ta dùng **Request Body**. FastAPI dùng **Pydantic** để định nghĩa model dữ liệu.

```python
from pydantic import BaseModel

class ScanRequest(BaseModel):
    url: str
    depth: int = 2
    scan_type: str

@app.post("/create-scan")
def create_scan(scan: ScanRequest):
    # Ở đây chúng ta sẽ xử lý logic tạo scan
    return {"message": "Đã nhận lệnh scan", "data": scan}
```

**⚡ Bài tập nhỏ 4:**
Tạo model `UserCreate` gồm `username`, `email`, và `password`. Viết một API `POST /register` nhận model này và trả về thông tin (nhớ đừng trả về password nhé!).

---

## 4. 🛠️ MINIPROJECT: Scan Job Manager (In-Memory)

**Mục tiêu:** Áp dụng tất cả kiến thức trên để xây dựng một API quản lý các lệnh quét (Scan Jobs) đơn giản cho VNComply. Vì chưa học Database, chúng ta sẽ lưu dữ liệu trong một list tạm thời (in-memory).

**Yêu cầu:**

1.  **Model:** Tạo Pydantic model `ScanJob` gồm:
    - `id`: int (tự tăng hoặc random)
    - `target_url`: str (bắt buộc)
    - `scan_type`: str (chỉ nhận "privacy" hoặc "security")
    - `status`: str (mặc định là "queued")
2.  **API Endpoints:**
    - `POST /scans`: Nhập url và scan_type, tạo job mới, lưu vào list, trả về job vừa tạo.
    - `GET /scans`: Lấy danh sách tất cả các job. Hỗ trợ lọc theo `status` (query param).
    - `GET /scans/{scan_id}`: Lấy chi tiết một job theo ID. Nếu không tìm thấy, trả về lỗi 404.

**Gợi ý cấu trúc code:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Giả lập Database
fake_db = []

# Định nghĩa Model
class ScanCreate(BaseModel):
    target_url: str
    scan_type: str # privacy / security

class ScanResponse(BaseModel):
    id: int
    target_url: str
    scan_type: str
    status: str

# Viết các API ở dưới...
```

**Thử thách thêm (Optional):**
Thêm module `enum` của Python để bắt buộc `scan_type` chỉ được là `ScanType.PRIVACY` hoặc `ScanType.SECURITY`.

---

**Tổng kết ngày 1:**
Bạn đã cài đặt xong môi trường, viết được API cơ bản, hiểu cách nhận và kiểm tra dữ liệu đầu vào. Đây là nền tảng để ngày mai chúng ta kết nối với **Database thật (PostgreSQL)** và lưu trữ dữ liệu lâu dài.

Chúc bạn code vui vẻ! 🚀

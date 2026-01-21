📚 PHẦN 1: PLAYWRIGHT LÀ GÌ? (30 phút)
1.1 Giới thiệu Playwright
Playwright là gì?
Playwright = Thư viện điều khiển trình duyệt tự động

Giống như bạn ngồi trước máy tính:
- Mở Chrome/Firefox
- Vào Google
- Gõ từ khóa tìm kiếm
- Click vào kết quả

Nhưng làm TỰ ĐỘNG bằng code!
Use cases thực tế:
✅ Web Scraping: Thu thập dữ liệu từ websites
✅ Testing: Kiểm thử tự động ứng dụng web
✅ Automation: Tự động hóa các tác vụ lặp đi lặp lại
✅ Monitoring: Giám sát website có hoạt động không
✅ Screenshot: Chụp màn hình tự động
✅ PDF Generation: Tạo PDF từ web pages


1.2 Cài đặt và Setup
Kiểm tra cài đặt:
bash# Kiểm tra Playwright đã cài chưa
python -c "import playwright; print('✅ Playwright installed')"

# Nếu chưa cài:
pip install playwright

# Install browsers (Chromium, Firefox, WebKit)
python -m playwright install

# Kiểm tra browsers đã cài
python -m playwright install --help



## 📝 PHẦN 2: PLAYWRIGHT BASICS - SYNC VERSION (60 phút)

### 2.1 Browser, Context, Page Architecture

**Hiểu kiến trúc:**
```
Playwright
    │
    └── Browser (Chrome/Firefox/Safari)
            │
            ├── Context 1 (Incognito Window 1)
            │       │
            │       ├── Page 1 (Tab 1)
            │       ├── Page 2 (Tab 2)
            │       └── Page 3 (Tab 3)
            │
            └── Context 2 (Incognito Window 2)
                    │
                    ├── Page 1 (Tab 1)
                    └── Page 2 (Tab 2)







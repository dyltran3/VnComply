from playwright.sync_api import sync_playwright

def demo_architecture():
    with sync_playwright() as p:
        # 1. Launch Browser (mở Chrome)
        browser = p.chromium.launch(headless=False)
        print("✅ Browser launched")
        
        # 2. Create Context (như mở cửa sổ ẩn danh)   
        context = browser.new_context()
        print("✅ Context created")
        
        # 3. Create Page (như mở tab mới)
        page = context.new_page()
        print("✅ Page created")
        
        # 4. Navigate
        page.goto('https://mydtu.duytan.edu.vn')
        print(f"✅ Navigated to: {page.url}")
        
        # 5. Get title
        title = page.title()
        print(f"📄 Title: {title}")
        
        # 6. Cleanup (QUAN TRỌNG!)
        context.close()
        browser.close()
        print("✅ Cleaned up")

demo_architecture()
from playwright.sync_api import sync_playwright
import time

def demo_github_search():
    """
    Demo: Search trên GitHub
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # slow_mo để thấy rõ
        page = browser.new_page()
        
        # 1. Vào GitHub
        page.goto('https://google.com')
        print("✅ Opened GitHub")
        
        # 2. Tìm search box bằng placeholder
        search_box = page.get_by_placeholder('Search GitHub')
        print("✅ Found search box")
        
        # 3. Click vào search box
        search_box.click()
        print("✅ Clicked search box")
        
        # 4. Type text
        search_box.fill('playwright python')
        print("✅ Typed search term")
        
        # 5. Press Enter
        search_box.press('Enter')
        print("✅ Pressed Enter")
        
        # 6. Đợi kết quả load
        page.wait_for_load_state('networkidle')
        print("✅ Search results loaded")
        
        # 7. Chụp screenshot
        page.screenshot(path='github_search.png')
        print("✅ Screenshot saved")
        
        time.sleep(3)  # Để xem kết quả
        browser.close()

demo_github_search()
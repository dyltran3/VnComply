from playwright.sync_api import sync_playwright

def demo_locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://playwright.dev')
        
        # 1. ✅ get_by_role - ƯU TIÊN CAO NHẤT
        # Tìm theo ARIA role (button, link, textbox...)
        get_started_link = page.get_by_role('link', name='Get started')
        print(f"✅ Found by role: {get_started_link}")
        
        # 2. ✅ get_by_text - Tìm theo text hiển thị
        docs_link = page.get_by_text('Docs')
        print(f"✅ Found by text: {docs_link}")
        
        # 3. ✅ get_by_label - Tốt cho form fields
        # page.get_by_label('Email')
        
        # 4. ✅ get_by_placeholder
        # page.get_by_placeholder('Search...')
        
        # 5. ✅ get_by_test_id - Nếu developer thêm data-testid
        # page.get_by_test_id('submit-button')
        
        # 6. ⚠️ CSS Selector - Dùng khi không còn cách nào khác 
        nav = page.locator('nav')
        print(f"⚠️  Found by CSS: {nav}")
        
        browser.close()

demo_locators()
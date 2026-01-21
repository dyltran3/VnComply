from playwright.sync_api import sync_playwright

def demo_interactions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto('https://the-internet.herokuapp.com/login')
        
        # 1. TYPE vào input
        username = page.get_by_label('Username')
        username.fill('tomsmith')  # Nhanh
        # hoặc username.type('tomsmith', delay=100)  # Chậm như người gõ
        print("✅ Filled username")
        
        # 2. TYPE vào password
        password = page.get_by_label('Password')
        password.fill('SuperSecretPassword!')
        print("✅ Filled password")
        
        # 3. CLICK button
        login_button = page.get_by_role('button', name='Login')
        login_button.click()
        print("✅ Clicked login")
        
        # 4. Đợi navigation
        page.wait_for_load_state('networkidle')
        
        # 5. Verify success message
        success_msg = page.locator('.flash.success').text_content()
        print(f"📄 Message: {success_msg.strip()}")
        
        browser.close()

demo_interactions()
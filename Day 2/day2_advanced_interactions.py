# day2_advanced_interactions.py
from playwright.sync_api import sync_playwright

def demo_advanced():
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)  # slow_mo để thấy rõ
        page = browser.new_page()
        
        # Demo checkboxes
        page.goto('https://the-internet.herokuapp.com/checkboxes')
        
        # 1. CHECK checkbox
        checkbox1 = page.locator('input[type="checkbox"]').first
        checkbox1.check()  # Tích vào
        print(f"✅ Checkbox 1 checked: {checkbox1.is_checked()}")
        
        # 2. UNCHECK checkbox
        checkbox2 = page.locator('input[type="checkbox"]').nth(1)
        checkbox2.uncheck()  # Bỏ tích
        print(f"✅ Checkbox 2 checked: {checkbox2.is_checked()}")
        
        # Demo dropdown
        page.goto('https://the-internet.herokuapp.com/dropdown')
        
        # 3. SELECT from dropdown
        dropdown = page.locator('#dropdown')
        dropdown.select_option('1')  # Select Option 1
        print("✅ Selected option 1")
        
        # 4. HOVER (di chuột qua element)
        page.goto('https://the-internet.herokuapp.com/hovers')
        image = page.locator('.figure').first
        image.hover()
        print("✅ Hovered over image")
        
        # 5. RIGHT CLICK
        page.goto('https://the-internet.herokuapp.com/context_menu')
        page.on('dialog', lambda dialog: dialog.accept())
        hot_spot = page.locator('#hot-spot')
        hot_spot.click(button='right')
        print("✅ Right clicked")
        
        browser.close()

demo_advanced()

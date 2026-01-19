# test_playwright.py
from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False để thấy browser
        page = browser.new_page()
        page.goto('https://playwright.dev')
        print(f"✅ Title: {page.title()}")
        browser.close()

test_playwright()
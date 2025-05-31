from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_selector('span:has-text("Admin")')
        page.click('span:has-text("Admin")')

        # Add User
        page.wait_for_selector('button:has-text("Add")')
        page.click('button:has-text("Add")')
        page.locator('.oxd-select-text').nth(0).click()
        page.click('div[role="option"]:has-text("Admin")')
        page.fill('input[placeholder="Type for hints..."]', 'Peter Mac Anderson')
        page.click('div[role="option"]:has-text("Peter Mac Anderson")')
        page.locator('.oxd-select-text').nth(1).click()
        page.click('div[role="option"]:has-text("Enabled")')

        username_input = page.locator('input[autocomplete="off"]').nth(0)
        password_input = page.locator('input[type="password"]').nth(0)
        confirm_password_input = page.locator('input[type="password"]').nth(1)

        username_input.fill("TestUser123")
        password_input.fill("Test@1234")
        confirm_password_input.fill("Test@1234")
        page.click('button:has-text("Save")')

        browser.close()

run()

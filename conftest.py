from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture(scope="function")
def page():
     with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless= False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        
        page.close()
        context.close()
        browser.close()

@pytest.fixture(autouse=True)
def auto_accept_cookies(page):
    page.add_locator_handler(
        page.get_by_role("button", name="Přijmout"),
        lambda locator: locator.click()
    )
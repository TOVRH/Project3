from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture(scope="function")
def page():
     with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless= False, slow_mo=3000)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        context.close()
        browser.close()

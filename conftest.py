from playwright.sync_api import Page, sync_playwright
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def page():
     with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless= False, slow_mo=50)
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

@pytest.fixture
def first_steps(page,click_when_visible):
    page.goto("https://ramen-brno.cz/")

    krenova_button = page.locator('a[href*="krenova"] > button')
    click_when_visible(krenova_button)

    pridat_button = page.locator("#category-631889ef9b12a970532c6ad9 .MenuItemInner_menu-item-right__j_JN0 button").first
    click_when_visible(pridat_button)
    
    sezam_button = page.locator('div.styles_listWrapper__axc40 div:has-text("SEZAM") button')
    click_when_visible(sezam_button)

    hulky_button = page.locator('div.styles_listWrapper__axc40 div:has-text("hůlky") button')
    click_when_visible(hulky_button)
    

    objednat_button = page.get_by_role("button", name="Objednat")
    click_when_visible(objednat_button)
    
    open_cart_button = page.locator(".open-cart-button-desktop")
    click_when_visible(open_cart_button)

    potvrdit_button = page.get_by_role("button",name="Potvrdit")
    click_when_visible(potvrdit_button)

@pytest.fixture
def click_when_visible():
    def _click(locator, timeout=5000):
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()
    return _click

    
    
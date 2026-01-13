from playwright.sync_api import Page
import pytest

def test_ramen(page: Page):
    page.goto("https://ramen-brno.cz/")

    page.get_by_role("button", name="Navštívit").nth(0).click()

    page.get_by_role("button", name="PŘIDAT").nth(0).click()

    page.locator(".styles_isRequired__ORXf6 button").nth(1).click()

    page.locator(".detailed-item-modal .styles_listWrapper__axc40 button").nth(2).click()

    page.get_by_role("button", name="Objednat").click()

    page.locator(".open-cart-button-desktop").click()

    page.get_by_role("button",name="Potvrdit").click()

    page.locator(".CartItem_contentRight__uO_MH .counter-remove").click()

    prazdny_kosik = page.locator("text=Položky nevybrány. Zatím jste nic neobjednali")
    assert prazdny_kosik.is_visible()








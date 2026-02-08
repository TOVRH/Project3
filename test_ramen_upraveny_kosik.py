from playwright.sync_api import Page
import pytest
from playwright.sync_api import expect
import re

def parse_price(text: str) -> float:
    return float(text.replace("Kč", "").replace(",", ".").strip())

def test_ramen(page: Page, auto_accept_cookies, first_steps, click_when_visible):
    upravit_button = page.get_by_role("button",name="Upravit")
    click_when_visible(upravit_button)
   
    chilli_button = page.locator('div.styles_listWrapper__axc40 div:has-text("CHILLI") button')
    click_when_visible(chilli_button)
    
    vidlicka_button = page.locator('div.styles_listWrapper__axc40 div:has-text("vidlička") button')
    click_when_visible(vidlicka_button)
    
    add_item_button = page.locator(".detailed-item-modal .counter-add")
    click_when_visible(add_item_button)
    
    confirm_button = page.locator(".detailed-item-modal .styles_bottom-container__XbPb0 > button")
    click_when_visible(confirm_button)

    vidlicka = page.locator("text=vidlička").first
    chilli = page.locator("text=CHILLI").first
    expect(vidlicka).to_be_visible(timeout=5000)
    expect(chilli).to_be_visible(timeout=5000)

    cart_items = page.locator(".check-order-items .check-order-item")
    expect(cart_items.first).to_be_visible(timeout=10000)
    total_calculated = 0.0

    for i in range(cart_items.count()):
        item = cart_items.nth(i)

        price_text = item.locator(".CartItem_price__s6QU2").inner_text()
        price = parse_price(price_text.splitlines()[0])

        name_text = item.locator('[class^="CartItem_name__"]').inner_text()
        match = re.search(r"(\d+)\s*×", name_text)
        qty = int(match.group(1)) if match else 1

        total_calculated += price * qty

    total_ui_locator = page.locator("text=Kč").last
    expect(total_ui_locator).to_be_visible(timeout=10000)
    total_ui_text = total_ui_locator.inner_text()
    total_ui = parse_price(total_ui_text)

    assert round(total_ui, 2) == round(total_calculated, 2)
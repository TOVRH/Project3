from playwright.sync_api import Page
import pytest
from playwright.sync_api import expect

def test_ramen(page: Page, auto_accept_cookies, first_steps, click_when_visible):
    cart_items = page.locator(".CartItem_contentRight__uO_MH")
    expect(cart_items.first).to_be_visible(timeout=5000)
    assert cart_items.count() > 0

    remove_item = page.locator(".CartItem_contentRight__uO_MH .counter-remove")
    click_when_visible(remove_item)

    empty_cart = page.locator("text=Položky nevybrány. Zatím jste nic neobjednali")
    expect(empty_cart).to_be_visible(timeout=5000)








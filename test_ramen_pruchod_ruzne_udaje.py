import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "name, phone, email, error_count",
    [   ("Jan Novak", "555555555", "jan@novak.cz", 0),
        ("", "", "", 2),
        ("Jan Novak", "999999999", "jannovak.cz", 1),
        ]
)

def test_ramen(page: Page, auto_accept_cookies, first_steps, click_when_visible, name: str, phone: str, email: str, error_count: int):
    pokracovat_button = page.get_by_role("button",name="Pokračovat")
    click_when_visible(pokracovat_button)
    
    name_input = page.locator('[data-element="order-customer-info_name-input"]')
    phone_input = page.locator('[data-element="order-customer-info_phone-input"]')
    email_input = page.locator('[data-element="order-customer-info_email-input"]')
    errors = page.locator(".styles_error__PL_mX, .styles_PhoneFieldError__jswNz")
    closed = page.get_by_text("Upozorňujeme, že momentálně neprovozujeme.")
    payment = page.get_by_text("Způsob platby")
    
    expect(name_input).to_be_visible()
    expect(phone_input).to_be_visible()
    expect(email_input).to_be_visible()

    name_input.fill(name)
    phone_input.fill(phone)
    email_input.fill(email)

    potvrdit_button = page.get_by_role("button", name="Potvrdit")
    click_when_visible(potvrdit_button)

    if error_count > 0:
        expect(errors).to_have_count(error_count, timeout=5000)
    else:
        expect(payment.or_(closed)).to_be_visible(timeout=5000)
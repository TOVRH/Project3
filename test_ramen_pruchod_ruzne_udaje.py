import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "name, phone, email, error_count",
    [   ("Jan Novak", "555555555", "jan@novak.cz", 0),
        ("", "", "", 2),
        ("Jan Novak", "999999999", "jannovak.cz", 1),
        ]
)

def test_ramen(page: Page, auto_accept_cookies, first_steps, name: str, phone: str, email: str, error_count: int):
    page.get_by_role("button",name="Pokračovat").click()

    closed = page.get_by_text("Upozorňujeme, že momentálně neprovozujeme.")
    name_input = page.locator('[data-element="order-customer-info_name-input"]')
    phone_input = page.locator('[data-element="order-customer-info_phone-input"]')
    email_input = page.locator('[data-element="order-customer-info_email-input"]')
    errors = page.locator(".styles_error__PL_mX, .styles_PhoneFieldError__jswNz")


    expect(name_input.or_(closed)).to_be_visible(timeout=5000)

    if closed.is_visible():
        return
    
    expect(name_input).to_be_visible()
    expect(phone_input).to_be_visible()
    expect(email_input).to_be_visible()

    name_input.fill(name)
    phone_input.fill(phone)
    email_input.fill(email)

    page.get_by_role("button", name="Potvrdit").click()
    
    if error_count > 0:
        expect(
            errors.or_(closed)
        ).to_be_visible(timeout=5000)

        if closed.is_visible():
            expect(closed).to_be_visible()
            return

        expect(errors).to_have_count(error_count, timeout=5000)

    else:
        expect(
            page.get_by_text("Způsob platby")
            .or_(closed)
        ).to_be_visible (timeout=5000)

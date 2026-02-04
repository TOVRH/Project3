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

    expect(page.locator('[data-element="order-customer-info_name-input"]')).to_be_visible(timeout=5000)
    page.fill('[data-element="order-customer-info_name-input"]', name)
    expect(page.locator('[data-element="order-customer-info_phone-input"]')).to_be_visible(timeout=5000)
    page.fill('[data-element="order-customer-info_phone-input"]', phone)
    expect(page.locator('[data-element="order-customer-info_email-input"]')).to_be_visible(timeout=5000)
    page.fill('[data-element="order-customer-info_email-input"]', email)

    page.get_by_role("button", name="Potvrdit").click()
    
    errors = page.locator(".styles_error__PL_mX, .styles_PhoneFieldError__jswNz")

    if error_count > 0:
        expect(errors).to_have_count(error_count, timeout=5000)
    else:
        expect(
            page.get_by_text("Způsob platby")
            .or_(page.get_by_text("Upozorňujeme, že momentálně neprovozujeme."))
        ).to_be_visible(timeout=5000)

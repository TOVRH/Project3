import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "jmeno, telefon, email, pocet_chyb",
    [   ("Jan Novak", "555555555", "jan@novak.cz", 0),
        ("", "", "", 2),
        ("Jan Novak", "999999999", "jannovak.cz", 1),
        ]
)

def test_ramen(page: Page, jmeno: str, telefon: str, email: str, pocet_chyb: int):
    page.goto("https://ramen-brno.cz/")

    page.get_by_role("button", name="Navštívit").nth(0).click()

    page.get_by_role("button", name="PŘIDAT").nth(0).click()

    page.locator(".styles_isRequired__ORXf6 button").nth(1).click()

    page.locator(".detailed-item-modal .styles_listWrapper__axc40 button").nth(2).click()

    page.get_by_role("button", name="Objednat").click()

    page.locator(".open-cart-button-desktop").click()

    page.get_by_role("button",name="Potvrdit").click()

    page.get_by_role("button",name=("Pokračovat")).click()

    page.fill('[data-element="order-customer-info_name-input"]', jmeno)
    page.fill('[data-element="order-customer-info_phone-input"]', telefon)
    page.fill('[data-element="order-customer-info_email-input"]', email)

    page.get_by_role("button", name="Potvrdit").click()
    
    errors = page.locator(".styles_error__PL_mX, .styles_PhoneFieldError__jswNz")

    if pocet_chyb > 0:
        expect(errors).to_have_count(pocet_chyb)
    else:
        expect(
            page.get_by_text("Způsob platby")
            .or_(page.get_by_text("Upozorňujeme, že momentálně neprovozujeme."))
        ).to_be_visible()

from playwright.sync_api import Page
import pytest

def test_ramen(page: Page):
    page.goto("https://ramen-brno.cz/")

    page.get_by_role("button", name="Přijmout").click()
    
    page.get_by_role("button", name="Navštívit").nth(0).click()
 
    page.get_by_role("button", name="Přijmout").click()

    page.get_by_role("button", name="PŘIDAT").nth(0).click()
   
    page.locator(".styles_isRequired__ORXf6 button").nth(0).click()

    page.locator(".detailed-item-modal .styles_listWrapper__axc40 button").nth(2).click()
    
    page.get_by_role("button", name="Objednat").click()
    
    page.locator(".open-cart-button-desktop").click()
   
    page.get_by_role("button",name="Potvrdit").click()
   
    page.get_by_role("button",name="Upravit").click()
   
    page.locator(".styles_isRequired__ORXf6 button").nth(1).click()
    
    page.locator(".detailed-item-modal .styles_listWrapper__axc40 button").nth(3).click()
    
    page.locator(".detailed-item-modal .counter-add").click()

    page.locator(".detailed-item-modal .styles_bottom-container__XbPb0 > button").click()

    vidlicka = page.locator("text=vidlička")
    chilli = page.locator("text=CHILLI")
    assert vidlicka.is_visible()
    assert chilli.is_visible()

    edamame_cena = 76
    hulky_cena = 1.90
    vidlicka_cena = 1.90
    mnozstvi = 2
    
    ocekavana_cena = (edamame_cena + hulky_cena + vidlicka_cena) * mnozstvi

    cena_text = page.locator("div.CartItem_price__s6QU2").inner_text()
    cena_ui = float(cena_text.splitlines()[0].replace(" Kč", "").strip())

    assert round(cena_ui, 2) == round(ocekavana_cena, 2)

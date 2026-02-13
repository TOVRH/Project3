# Project3
Tři automatizované testy na ramen-brno.cz

test_prazdny_kosik.py: Test kontroluje zda se po přidání povinných a nepovinných položek do košíku a následném zrušení povinné položky košík celý smaže. Po smazání položek test kontroluje informační hlášku "Položky nevybrány. Zatím jste nic neobjednali". Nadále kontroluje, jestli se košík opravdu vyprázdnil.

test_pruchod_ruzne_udaje.py: Test kontroluje průchod objednáváním položek až k případnému placení s použitím různých údajů. Stránka se chová jinak podle toho zda testy zadáváme v průběhu otevírací doby a po otevírací době.
Zadané možnosti jsou:
  správné údaje vedoucí k možnosti zaplacení objednávky
  údaje nejsou vyplněny. Stránka by měla zahlásit dvě chybové hlášky u povinných údajů (jméno, telefonní číslo).
  špatně vyplněné povinné telefoní číslo a nepovinný email. Měla by se zobrazit jedna chybová hláška (telefonní číslo).
Do testu je případně možné doplnit další kombinace správnych / nepsrávných údajů.

test_uprava_kosiku_cena.py: Test kontroluje přidání a následnou úpravu položek v košíku. Následně zkrontoluje zda stránka správně spočítala upravenou cenu položek.


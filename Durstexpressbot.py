from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import time


print("PLZ eingeben:")
plz = input()
print("Mate 0.5? Anzahl eingeben")
mate5 = input()
print("Mate 0.33? Anzahl eingeben")
mate33 = input()
print("Sterni? Anzahl eingeben")
sterni = input()
print("Fritz Cola 0.5? Anzahl eingeben")
fritzcola = input()
print("Fritz Mate? Anzahl eingeben")
fritzmate = input()
print("Sternburg Doppelkaramel? Anzahl eingeben")
dopcaram = input()
if (int(dopcaram) > 0):
    print("So etwas reudiges unterstütze ich nicht")
    sys.exit(0)
    
driver = webdriver.Firefox()
driver.get('https://www.durstexpress.de/')
time.sleep(7)
html_source = driver.page_source

def warenkorb(link, anzahl):
    anzbutton = 1
    driver.get(link)
    anzahl_feld = driver.find_element_by_xpath("//input[@id='qty']")
    anzahl_feld.clear()
    anzahl_feld.send_keys(anzahl)
    warenkorb = driver.find_element_by_xpath("//button[@id='product-addtocart-button']")
    warenkorb.submit()
    
def plzeingeben(plzeing):
    plz_input = driver.find_element_by_id('input_plz')
    plz_input.send_keys(plzeing)
    plz_input.submit()


if (int(mate5) > 0):
    warenkorb("https://www.durstexpress.de/berlin1/club-mate-20-fl-0-5-103959-20-0", mate5)
if (int(mate33) > 0):
    warenkorb("https://www.durstexpress.de/berlin1/club-mate-20-fl-0-33-107201-20-0", mate33)
if (int(sterni) > 0):
    warenkorb("https://www.durstexpress.de/berlin1/sternburg-export-20-fl-0-5-103571-20-0", sterni)
if (int(fritzcola) > 0):
    warenkorb("https://www.durstexpress.de/berlin1/fritz-kola-10-fl-0-5-113857-10-0", fritzcola)
if (int(fritzmate) > 0):
    warenkorb("https://www.durstexpress.de/berlin1/fritz-mate-10-fl-0-5-124337-10-0", fritzmate)


while "aktuellen hohen Bestellsituation haben wir uns dazu entschlossen, den Shop kurzfristig zu schließen" in html_source:
    time.sleep(30)
    driver.refresh()
    if "Bitte gib deine Lieferadresse ein:" in html_source:
        plzeingeben(plz)

driver.get('https://www.durstexpress.de/checkout/cart/')
time.sleep(7)
if "Bitte gib deine Lieferadresse ein:" in html_source:
        plzeingeben(plz)
driver.get('https://www.durstexpress.de/checkout/#shipping')
time.sleep(5)
if "Bitte gib deine Lieferadresse ein:" in html_source:
        plzeingeben(plz)

os.system('spd-say "Die Bestellung ist bereit"')


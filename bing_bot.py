from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# Chrome-Optionen (headless, damit kein Fenster angezeigt wird)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Entfernen, wenn du das Fenster sehen möchtest
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Pfad zu deinem Chromedriver (anpassen falls nötig)
chromedriver_path = '/pfad/zu/deinem/chromedriver'  # Zum Beispiel '/usr/local/bin/chromedriver'

# Dienst einrichten und Browser starten
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

search_terms = ["Auto", "Haus", "Kaffee", "Computer", "Berlin", "Fussball", "Technik", "Wetter", "Musik", "Reise"]

for i in range(35):  # Anzahl der Suchen
    term = random.choice(search_terms)  # Zufälligen Begriff wählen
    url = f"https://www.bing.com/search?q={term}"
    
    driver.get(url)  # Seite im Browser öffnen
    time.sleep(random.randint(4, 7))  # 4-7 Sekunden warten
    

    driver.execute_script("window.open('');")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


driver.quit()

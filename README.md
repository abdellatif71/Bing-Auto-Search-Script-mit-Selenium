Bing Auto-Search Script mit Selenium
Dieses Python-Skript automatisiert die Suche auf Bing, indem es zufällige Suchbegriffe verwendet und nach einer bestimmten Anzahl von Suchen das Browserfenster schließt und einen neuen Tab öffnet. Es nutzt Selenium WebDriver und ChromeDriver, um diese Aufgabe auszuführen.

Anforderungen
Python 3.x: Stelle sicher, dass Python 3 auf deinem System installiert ist.
Selenium: Installiere das Selenium-Paket, wenn es noch nicht installiert ist:
bash
Copier
Modifier
pip install selenium
Chrome/Chromium und ChromeDriver: Du musst Chrome oder Chromium sowie den entsprechenden ChromeDriver auf deinem System haben. Anleitungen zur Installation findest du weiter unten.
Funktionsweise
Headless Mode: Das Skript läuft im Headless-Modus, was bedeutet, dass der Browser im Hintergrund ohne Benutzeroberfläche ausgeführt wird. Du kannst den Headless-Modus deaktivieren, wenn du die Interaktionen im Browser sehen möchtest.
Zufällige Suchbegriffe: Das Skript führt eine festgelegte Anzahl von Suchen aus, indem es zufällig aus einer Liste von Suchbegriffen auswählt.
Tab schließen und neuen öffnen: Nach jeder Suche wird der aktuelle Tab geschlossen und ein neuer Tab geöffnet, um eine weitere Suche auszuführen.
Installation von Chrome/Chromium und ChromeDriver
Installiere Chromium:

bash
Copier
Modifier
sudo apt install chromium
sudo apt install chromium-driver
ChromeDriver manuell installieren (falls notwendig):

Lade den neuesten ChromeDriver herunter:
ChromeDriver Download
Entpacke das Archiv und verschiebe die Datei nach /usr/local/bin/ oder einem anderen Verzeichnis deiner Wahl.
Stelle sicher, dass der Pfad zu ChromeDriver korrekt ist:
Im Skript musst du den Pfad zu deinem chromedriver anpassen. Der Standardpfad im Skript lautet /pfad/zu/deinem/chromedriver.
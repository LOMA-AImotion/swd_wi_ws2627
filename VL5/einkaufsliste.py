# Erstelle Einkaufsliste durch interaktive Eingabe
# Frage Nutzer nach Eingabe, solange nicht nein, füge hinzu 

# leere Einkaufsliste
einkaufsliste = {} # dict kein Set

# solange nicht nein -> frage weiter
mehr_einfuegen = input("Möchten Sie mehr einfügen? (ja | nein)")

while mehr_einfuegen == "ja":
    artikel = input("Welchen Artikel?")
    anzahl = int(input("Wie viel davon?"))

    # ins dictionary einfügen
    einkaufsliste[artikel] = anzahl
    mehr_einfuegen = input("Möchten Sie mehr einfügen? (ja | nein)")

# gib Dictionary aus
print(einkaufsliste)
# die Schlüssel
print(einkaufsliste.keys())
# die Werte
print(einkaufsliste.values())
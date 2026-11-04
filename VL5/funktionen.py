def flaeche(breite : int, hoehe : int ) -> int:
    a = breite * hoehe
    print("Wird die Funktion ausgeführt?")
    return a 

print("Hier bin ich im Code")
# 5 und 10 sind die Argumente, die an die Parameter breite und hoehe 
# übergeben werden
print("Fläche mit Breite 5 und Höhe 10:", flaeche(5,10))
# Aufruf mit String klappt, obwohl wir eigentlich int wollen
print(flaeche("5", "10"))
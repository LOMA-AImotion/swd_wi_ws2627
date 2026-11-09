from hilfsfunktion import netto_zu_brutto

netto_preis = float(input("Welcher Preis ist Netto?"))
brutto_preis = netto_zu_brutto(netto_preis)
print("Brutto:", brutto_preis)

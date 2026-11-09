from hilfsfunktion import netto_zu_brutto

netto_preise = [10.0, 100.0, 1000.0]
brutto_preise = [netto_zu_brutto(p) for p in netto_preise]
print("Bruttopreise:", brutto_preise)
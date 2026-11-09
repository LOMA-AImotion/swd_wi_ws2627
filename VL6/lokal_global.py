def flaechen_preis(seiten_laenge: float) -> float:    
    ergebnis = seiten_laenge*seiten_laenge * qm_preis
    # qm_preis = 20 würde zu UnboundLocalError führen
    print("Ergebnis = ", ergebnis)
    print("QM-Preis = ", qm_preis)

    return ergebnis

qm_preis = 30
print(flaechen_preis(10))
print("QM-Preis = ", qm_preis)
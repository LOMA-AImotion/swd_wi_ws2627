from pathlib import Path
# __file__ ist der Pfad der aktuellen Datei (file_reader.py)
def zeilen_lesen(dateiname: str) -> list[str]:
	"""Liest eine Textdatei zeilenweise und gibt ihre Zeilen zurück."""
	dateipfad = Path(__file__).parent / dateiname
	with dateipfad.open(encoding="utf-8") as datei:
		return [zeile.rstrip("\n") for zeile in datei]

# with reserviert eine Ressource und gibt sie nach Verwendung automatisch frei
nomen = zeilen_lesen("nomen.txt")
adjektive = zeilen_lesen("adjektive.txt")

print("Nomen:", nomen)  
print("Adjektive:", adjektive)

# zähle alle Zahlen zwischen 1 und k, die gerade sind
k = int(input("Zahl k?"))

# Lösungsweg 1 - mit Modulo
for i in range(1, k+1):
    if i % 2 == 0: # Zahl ist gerade 
        print(i)

print("-"*20)

# Lösungsweg 2 - mit Schrittweite 
for i in range(2, k+1, 2): 
    print(i)
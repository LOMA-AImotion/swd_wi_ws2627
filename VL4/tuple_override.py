rgb_tupel = (255, 200, 150)

# ändere rot auf 50
# funktioniert nicht: rgb_tupel[0] = 50
rgb_neu = tuple(rgb_tupel[i] if i != 0 else 50 for i in range(len(rgb_tupel)))
print(rgb_neu)
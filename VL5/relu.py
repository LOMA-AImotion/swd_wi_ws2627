# Funktion definieren:
# ReLU(x) = 0 wenn x negativ
# Relu(x) = x wenn x positiv oder 0

def relu(x: float) -> float:
    if x < 0:
        return 0
    else:
        return x

# aufzählen von -10 bis +10
for i in range(-10, 11):
    print(f"ReLU({i}) = {relu(i)}")
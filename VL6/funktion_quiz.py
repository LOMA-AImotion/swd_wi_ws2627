def verdopple(x: int) -> int:
    def berechnung(x:int) -> int:
        return 2*x
    return berechnung(x)

print(verdopple(10))

import math
def quadrat_wurzel(x: float): 
    return -math.sqrt(x), math.sqrt(x)

print(quadrat_wurzel(9))
neg_wurzel, pos_wurzel = quadrat_wurzel(16)
print(pos_wurzel)
k = int(input("Welches k?"))

# gehe über alle Werte i zwischen 1 und k (inklusive)
# Baue jeweils das Tupel aus i und i Mal "x", z.B. (1, "x"), (2, "xx") usw
# Füge alle diese Tupel in eine Menge ein {}

menge = set() # hier wäre {} viel besser, Python ...
for i in range(1, k+1):
    neues_tupel = (i, "x"*i)
    menge.add(neues_tupel) # append wäre es bei einer Liste

print(menge)

print("-"*10)

# mit einer Set Comprehension
menge = {(i, "x"*i) for i in range(1, k+1)}
print(menge)
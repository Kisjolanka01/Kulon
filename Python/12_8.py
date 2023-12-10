import random
számok = []

for i in range(12):
    számok.append(random.randint(0, 9))

print(számok)

# 2. Lista elemei összegét írjuk ki
osszeg = 0
i = 0
while i < len(számok):
    osszeg += számok[i]
    i += 1

print(f"Összeg: {osszeg}")

# 3. Legkisebb elem helyét és értékét
minIndex = 0
min = számok[0]

i = 0
while i < len(számok):
    if számok[i] <= min:
        min = számok[i]
        minIndex = i
    i += 1

print(f"Legkisebb elem helye: {minIndex} értéke: {min}")

# 4. Van e a listában 6 ha van hol?
vanE = False
i = 0
while i < len(számok) and not(számok[i] == 6):
    i += 1

vanE = i < len(számok)
print("Van e a számok lista között 6-os?", vanE)

i = 0
while i < len(számok) and vanE and not(számok[i] == 6):
    i += 1

if(vanE):
    print(f"Van a listában {számok[i]} szám a {i}. helyen ")

# 5. Legnagyobb elem helyét és értékét
maxIndex = 0
max = számok[maxIndex]

for i in range(len(számok)):
    if számok[i] >= max:
        max = számok[i]
        maxIndex = i

print(f"Legnagyobb elem helye: {maxIndex} értéke: {max}")

# 6. Számoljuk meg hány páros szám van a listánkban.
db = 0

for elem in számok:
    if elem % 2 == 0:
        db += 1

print(f"{db}db páros szám van a listánkban.")
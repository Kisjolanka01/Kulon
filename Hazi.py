5#1.feladat
import random

szam = int(input("Add meg a hetek számát!"))

while szam < 1 or szam > 5:
    print("Hibás számot adtál meg próbáld újra!")
    szam = int(input("Add meg a hetek számát!"))
    print(szam)

#2.feladat

Támadások = []
for i in range(szam*7):
    Támadás = random.randint(3,9)
    Támadások.append(Támadás)

#3.feladat
for i in range(szam):
    print(f"{i+1}.hét: ", end="")
    for j in range(7):
        print(f"{Támadások[i*7+j]} ",end="")
    print()

#4.feladat

darab=0
for elem in Támadások:
    darab += elem
print(f"Összes támadás száma: {darab}darab")


#5.feladat

darab=0
for elem in Támadások:
    if elem >5 and elem <8:
        darab+=1

print(f"Feltételnek megfelelő napok száma: {darab}darab")

#6.feladat

napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
het_helye = 0
nap_helye = 0
legutolso_legtobb_tamadas_szama = 0

for i in range(szam):
    for j in range(7):
        if Támadások[i*7+j] >= legutolso_legtobb_tamadas_szama:
            legutolso_legtobb_tamadas_szama = Támadások[i*7+j]
            nap_helye = j
            het_helye = i

print(f"Egy napon megtörtént legtöbb támadás száma: {legutolso_legtobb_tamadas_szama} darab\nHelye: {het_helye+1}. hét, {napok[nap_helye]}")
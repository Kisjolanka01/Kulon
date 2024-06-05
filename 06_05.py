while True:
    lista_hossza=int(input("Adja meg a lista hosszat[10...25]"))
    if lista_hossza >=10 and lista_hossza <= 25:
        break
    print("hibás adatbevitel")

import random
elemek = []
for i in range(lista_hossza):
    elemek.append(random.randint(1,5))
print(f"A lista tartalma {elemek}")

#osszegzes
osszeg = 0
for i in elemek:
    osszeg += i
print(osszeg)

#maxert
maxert = elemek[0]
maxhely = 0
for i in range(len(elemek)):
    if maxert <= elemek[i]:
        maxert = elemek[i]
        maxhely = i
print(f"A legnagyobb szam:{maxert}, helye: {maxhely+1}")

#megszamlalas
db = 0
for i in range(len(elemek)):
    if elemek[i]%2 == 0:
        db += 1
print(f"2-vel oszthatok szama: {db}")

#kereses
keresett_szam = 3
for szam in elemek:
    if(szam == keresett_szam):
        print("Van benne")
    else:
        print("Nincs benne")




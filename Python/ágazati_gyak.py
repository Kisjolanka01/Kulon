'''
while True:
    listaméret = int(input("Adja meg a lsita méretét [10..25]"))
    if listaméret >=10 and listaméret <= 25:
        break
    print("Hibás adatbevitel probald ujra")

import random

elemek = []
for i in range(listaméret):
    elemek.append(random.randint(1,5))
print(f"A lista tartalma {elemek}")

osszeg = 0
for i in elemek:
    osszeg += i
print(osszeg)

maxert = elemek[0]
maxhely = 0
for i in range(1, len(elemek)):
    if maxert <= elemek[i]:
        maxert = elemek[i]
        maxhely = i
print(f"A legnagyobb szám: {maxert}")
print(f"A legnagyobb szám helye: {maxhely}")

db = 0
for i in range(len(elemek)):
    if elemek[i]%2==0:
        db+=1
print(f"Ennyi szám osztható 2-vel: {db}")



def adatokBeolvasasa(fajl):
    lista = []
    f = open(fajl, 'r', encoding="UTF-8")
    sorok = f.readlines()
    lista.append(sorok) 
    print(sorok)
    f.close()
    '''



while True:
    listameret = int(input("Adja meg a lista hosszát [10...25]"))
    if listameret >= 10 and listameret <= 25:
        break
    print("Hibás adatbevitel probald ujra!")

import random
elemek= []
for i in range(listameret):
    elemek.append(random.randint(1,5))
print(f"A lsita tartalma {elemek}")

osszeg = 0
for i in elemek:
    osszeg+=i
print(f"A lista összege {osszeg}")

maxert=elemek[0]
maxhely=0
for i in range(1,len(elemek)):
    if maxert<= elemek[i]:
        maxert=elemek[i]
        maxhely=i
print(f"A legnagyobb érték: {maxert}, helye: {maxhely}")


db = 0
for i in range(len(elemek)):
    if elemek[i]%2==0:
        db+=1
print(f"Kettővel oszthatók száma: {db}")









































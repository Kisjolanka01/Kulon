"""
import random

while True:
    lista = []
    szam = int(input("Adja meg a lista hosszat [10...20]"))
    if szam >= 10 and szam <= 20:
        break
    print("hibas adatbevitel probald ujra")
for i in range(szam):
    lista.append(random.randint(1,5))

print(lista)
    
osszeg = 0
for i in lista:
    osszeg += i
print(F"A lista osszege: {osszeg}")

db = 0
keresettszam = 1
for i in range(len(lista)):
    if lista[i] == 1:
        db += 1
print(f"{db} egyes van a listaban")

maxert = lista[0]
maxhely = 0
for i in range(len(lista)):
    if maxert < lista[i]:
        maxert = lista[i]
        maxhely = i
print(f"A lista legnagyobb eleme: {maxert}, helye: {maxhely + 1}")


minert = lista[0]
minhely = 0
for i in range(len(lista)):
    if minert > lista[i]:
        minert = lista[i]
        minhely = i
print(f"A lista legkisebb eleme: {minert}, helye: {minhely + 1}")

def adatbeolvasas(filename):
    lista = []
    f = open(filename, 'r', encoding="UTF-8")
    for sor in f:
        sor = sor.replace("\n","").strip().split()
        f.close()
        for szam in sor:
            lista.append(int(sor))
        print(lista)"""















lista = [4, 4, 0, 0, 5, 6, 6, 5, 0, 0, 0, 4]

for i in range(len(lista)):
    if lista[i] == 0:
        print(F"{i + 1}. szék: ures")
    else:
        print(F"{i + 1}. szék: foglalt")
    
ures = 0
for i in range(len(lista)):
    if lista[i] == 0:
        ures += 1
print(f"Az 1-es teremben lévő üres helyek száma: {ures}")

while True:
    alapar = int(input("Add meg az alapárat [1000...5000]:"))
    if alapar >= 1000 and alapar <= 5000:
        break
    print("Hibás adatbevitel! Próbáld újra...")

bevetel = 0
for i in range(len(lista)):
    bevetel += lista[i] * alapar
print(f"Az 1-es terem bevétele: {alapar}")

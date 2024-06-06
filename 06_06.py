#a)

inyenc = [7, 0, 0, 10, 5]

#b)
nincstej = 0
for i in range(len(inyenc)):
    if inyenc[i] == 0:
        nincstej += 1
    print(f"{i + 1}. sor: {inyenc[i]} db tej")

print(f"Az inyenc kuckoban osszesen {nincstej} olyan sor van ahol nincs tej")


while True:
    tejar = int(input("add meg a tej arat 150...300: "))
    if tejar >= 150 and tejar <=300:
        break
    print("Hibas adatbevitel probald ujra")

bevetel = 0
for i in range(len(inyenc)):
    bevetel += inyenc[i] * tejar
print(f" az inyenc kucko bevetele: {bevetel} FT")


def adatokbeolvasa(filename):
    lst = []
    f = open(filename, 'r', encoding="UTF-8")
    for sor in f:
        lst.append(sor.replace("\n","").strip().split())
        f.close()

    for i in range(len(lst)):
        for j in range(len(list[i])):
            lst[i][j] = int(lst[i][j])
    return lst
sarki = adatokbeolvasa("sk.txt")

def megszamlalas():
    print("Oszlopok")
    maxert = sarki[0][0]
    maxhely = 0
    for i in range(6):
        dboszlop = 0
        for j in range(len(sarki)):
            dboszlop += sarki[j][i]
        if dboszlop > maxert:
            maxert = dboszlop
            maxhely = i
            print(f"{i + 1}. oszlop {dboszlop} tej")
        print(f"a legtobb tej: {maxhely + 1} oszlop")



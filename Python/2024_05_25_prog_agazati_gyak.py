"""
Ágazati gyakorló felkészítő feladatsor 2024. május 25.
"""

"""
1. feladat:
a) A példában látható módon kérjen be a felhasználótól 1 és 10 között egy számot és tárolja el a "bekértSzám" nevezetű
változóba! Ha a felhasználó a megadott intervallumon kívül ad meg egy számot, kérjen be újra addig, amíg nem ad meg egy
megfelelő számot!
PÉLDA:
Add meg a lista méretét [1...10]: 15
Hibás adatbevitel! Próbálja meg újra...
Add meg a lista méretét [1...10]: 8

b) Készítsen egy "számok" nevezetű listát és töltse fel annyi véletlen számmal 1 és 5 között, amennyit a felhasználó az a)
feladatban adott meg, majd írja ki a lista tartalmát a példában látható módon!
PÉLDA:
A lista tartalma: [1, 5, 2, 3, ..., 5, 1, 1]
"""
#a)
while True:
    bekértSzám = int(input("Add meg a lista méretét [1...10]: "))
    if bekértSzám >= 1 and bekértSzám <= 10:
        break
    print("Hibás adatbevitel! Próbálja meg újra...")

#b)
import random
számok = []
i = 0
while i < bekértSzám:
    számok.append(random.randint(1, 5))
    i += 1
print(f"A lista tartalma: {számok}")

"""
2. feladat:
a) Számolja meg az előbb létrehozott lista összegét, majd írja ki a példában látható módon.
Figyelem! A feladat megoldása során ne használja a pythonba beépített sum() függvényt.
PÉLDA:
A listában lévő elemek összege: 27

b) Keresse meg a legkisebb elemet és a pozícióját, majd írja ki a példában látható módon!
PÉLDA:
A legkisebb elem: 1, helye: 3. pozíció
"""
#a)
összeg = 0
i = 0
while i < len(számok):
    összeg += számok[i]
    i += 1
print(f"A listában lévő elemek összege: {összeg}")

#b)
minÉrték = számok[0]
minHely = 0
i = 0
while i < len(számok):
    if számok[i] < minÉrték:
        minÉrték = számok[i]
        minHely = i
    i += 1
print(f"A legkisebb elem: {minÉrték}, helye: {minHely + 1}. pozíció")

"""
3. feladat:
a) Készítsen egy "cimek.txt" nevezetű fájlt, amely tartalmazza a példában látható adatokat!
PÉLDA:
Gyöngyike_utca 5 21 8 42 39
Szemafor_utca 12 27 18 0 1
Práter_utca 0 0 3 16 6
Vágóhíd_utca 52 15 16 82 0

b) Készítsen egy függvényt "adatBeolvasás" néven, amelyben beolvassa a "cimek.txt" nevezetű fájlt és tárolja el a beolvasott adatokat egy "címek" listába!
PÉLDA:
címek = adatBeolvasás("cimek.txt")

c) Készítsen egy függvényt "teljesítmény" néven, amelyben megnézi, hogy hány olyan nap van, amikor volt teljesítmény (Teljesítmény: Ha az érték nem 0!), majd
írja ki a példában látható módon!
PÉLDA:
Az adatbázisban 16 db olyan nap volt, amikor volt teljesítménye a futárszolgálatnak.
"""
#a)

#b)
def adatBeolvasás(fájlNév):
    # Fájl beolvasása
    f = open(fájlNév, "r", encoding="UTF-8")
    lst = []
    for sor in f:
        lst.append(sor.replace("\n", "").strip().split())
    f.close()

    # Konvertálás
    i = 0
    while i < len(lst):
        j = 1
        while j < len(lst[i]):
            lst[i][j] = int(lst[i][j])
            j += 1
        i += 1
    return lst

címek = adatBeolvasás("cimek.txt")

#c)
def teljesítmény():
    db = 0
    i = 0
    while i < len(címek):
        j = 1
        while j < len(címek[i]):
            if címek[i][j] > 0:
                db += 1
            j += 1
        i += 1
    return db

teljesítményDb = teljesítmény()
print(f"Az adatbázisban {teljesítményDb} db olyan nap volt, amikor volt teljesítménye a futárszolgálatnak.")

"""
4. feladat:
a) Készítsen egy "szamhalmaz.txt" nevezetű fájlt, amely tartalmazza a példában látható adatokat!
PÉLDA:
0 0 2 5 4
3 3 0 1 0
0 0 1 1 0
6 4 6 8 1
9 4 2 5 2
0 0 0 0 0

b) Készítsen egy függvényt "adatBeolvasás" nevű függvényt, amelyben beolvassa az "szamhalmaz.txt"-t, és
egy "számhalmaz" nevű listában tároljuk el a beolvasott adatokat!
PÉLDA:
számhalmaz = adatBeolvasás("szamhalmaz.txt")

c) Nézze meg, hogy hány hatékony nap van, majd írja ki a példa alapján! Egy hatékony nap
annak számít, hogy egy sorban 3-nál több 0 elem szerepel!
PÉLDA:
Hatékony napok száma: 2
"""
#a)

#b)
def adatBeolvasás(fájlNév):
    # Fájl beolvasása
    f = open(fájlNév, "r", encoding="UTF-8")
    lst = []
    for sor in f:
        lst.append(sor.replace("\n", "").strip().split())
    f.close()

    # Konvertálás
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            lst[i][j] = int(lst[i][j])
            j += 1
        i += 1
    return lst

számhalmaz = adatBeolvasás("szamhalmaz.txt")

#c)
def hatékonyNapok():
    teljesDb = 0
    i = 0
    while i < len(számhalmaz):
        j = 0
        db = 0
        while j < len(számhalmaz[i]):
            if számhalmaz[i][j] == 0:
                db += 1
            j += 1
        if db > 3:
            teljesDb += 1
        i += 1
    return teljesDb

hatékonyDb = hatékonyNapok()
print(f"Hatékony napok száma: {hatékonyDb}")
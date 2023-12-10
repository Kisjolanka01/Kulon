#osszegzes

osszeg = 0
lista = [2, 4, 1, 5, 2]

for elem in lista:
    osszeg += elem
print(osszeg)


#megszámlálás

db = 0

for elem in lista:
    if (elem %2 == 0):
        db += 1
print(db)


#kiválasztás
index = 0
while(index < len(lista) & lista[index] !=5):
    index+= 1
print("helye:", index, "Érték:", lista(index))

#eldontés
i = 0 
while i < len(lista) & lista[i] == 5:
    i +=1

vanE = i < len(lista)
print("van-e 5-os a listában?" +vanE)

i = 0
while i < len(lista) & lista[i] %2 == 0:
    i += 1

vanE = i == len(lista)
print("osszes eleme osztahato 1-el?" + str(vanE))


#max

max = lista(0)
min = lista(0)
for elem in lista:
    if (elem > max):
        max = elem
    if (elem < min):
        min = elem

print(max)
print(min)

#keresés

vanE = False
i = 0
while i < len(lista) & lista[i] !=5:
    i +=1
vanE = i  < len(lista)

i = 0
while i < len(lista) & vanE & lista[i] !=5:
    i += 1
print(""+ str(vanE))


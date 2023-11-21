lista = [2, 3, 4, 5, 600, 7, 8, 9, 10, 201]

max = lista[0]
maxIndex = 0

volt = False
i = 0
while i < len(lista) and not(volt):
    if lista[i] > 200:
        volt = True
        max = lista[i]
        maxIndex = i

    i += 1

print(f"Szám: {max} helye: {maxIndex}")
    
 
matrix= [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for sor in matrix:
    print(sor[1])

hetijelentés=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for i in range(len(hetijelentés)):
    osszesen=0
    for elem in hetijelentés[i]:
        osszesen += elem
        print(f"{i+1}, hét összes eladása: {osszesen}")



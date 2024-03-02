file=open('python/input.txt')
sorok=file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(sorok[i].strip())

osszeg=[]
for i in range(len(szamok)):
    osszeg+=szamok[i]
atlag = osszeg/len(szamok)
print(f'elso file atlaga: {atlag}')

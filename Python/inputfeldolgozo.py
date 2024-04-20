file=open('Python/input.txt')
sorok=file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip))

osszeg=0
for i in range(len(szamok)):
     osszeg+=szamok[i]
atlag=osszeg/len(szamok)
print(F"az elso file atlaga: {atlag}")
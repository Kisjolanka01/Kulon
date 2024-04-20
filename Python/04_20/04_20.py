filename="input.txt"
lista=[]
file=open(filename,'r'encoding="utf-8")
sorok=file.readlines()
file.close()


for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
    lista.append(sorok[i].split(';'))
    for i in range(len(lista)):
        for x in range(len(lista[i])):
            lista[i][x]=int(lista[i][x])

def max():
    maxoszlop=None
maxért=lista[1][1]
maxindsor=None
for i in range(1,len([i])):
    if maxért <= lista[i][x]:
        maxért=lista[i][x]
        maxindsor=i+1
        maxoszlop=x+i

return maxért,maxindsor,maxoszlop


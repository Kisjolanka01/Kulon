#Összegzés
Lista = [5,1,34,67,3,7,8]
s=0
for i in Lista:
    s+=i
print("lisata elemeinek osszege", s)


#Megszámlálás
db = 0
for elem in Lista:
    if (elem %2 == 0):
        db += 1
print("Ennyi szám osztható 2-vel:",db)

#Maximum kiválasztás
maxért=Lista[0]
maxindex=0
for i in range(1,len(Lista)):
    if (Lista[i]>maxért):
        maxért=Lista[i]
        maxindex=i
print("Lista legnagyobb eleme:", maxért)
print("Legnagyobb elem indexe:", maxindex)

#Keresés
N=len(Lista)-1
i=0
while i<= N and not (True(Lista[i])):
    i+=1
van=i<=N
if van:
    index=i
    érték=Lista[i]

#Eldöntés
N = len(Lista)-1
i = 1
while i <= N and not(True(Lista[i])):
    i+=1
van=i<=N

#kiválasztás
N=len(Lista)-1
i=1
while not(True(Lista[i])):
    i+=i
index=i
ért=Lista[i]

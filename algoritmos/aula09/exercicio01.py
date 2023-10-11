lista=[]

for i in range (10):
    lista.append(input('digite:'))
print()
for i in lista[::-1]:
    print(i, end=' - ')


for i in range(-1, -len(lista)-1,-1):
    print(lista[i], end=',')
print()

for i in lista.__reversed__():
    print(i, end="w")
print()

lista.reverse()
print(lista)
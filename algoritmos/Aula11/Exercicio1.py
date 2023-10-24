lista = []
i = 0
while i < 10:
    x = int(input("Digite um número: "))
    lista.append(x)
    i = i + 1

tupla = tuple(lista)
print(tupla)
print(tupla[::-1])
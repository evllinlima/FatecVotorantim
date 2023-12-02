def ehPrimo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def qntPrimos(num):
    qnts = 0
    if num >= 0:
        for i in range(0, num + 1):
            if ehPrimo(i):
                lista.append(i)
                qnts += 1
    return qnts

Y = 30
lista = []
qntPrimos(Y * 2 + 5)
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]
print(f'Y*2+5: {Y * 2 + 5}, Valor da Soma de Todos os Números: {soma}')

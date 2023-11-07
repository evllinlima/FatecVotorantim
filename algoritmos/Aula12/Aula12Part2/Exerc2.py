
def ehprimo(n):
    for i in range(2,n): #testa todas possibilidades menos % 1 e % ele msm. O QUE NÃO É PRIMO O RESULTADO É 0
        if (n % i) == 0:
            return False
    return True

valor = int(input("Digite um valor: "))
if ehprimo(valor):
    print(f"O número {valor} é primo!")
else:
    print((f"O número {valor} não é primo!"))
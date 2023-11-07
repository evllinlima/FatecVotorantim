
def ehpar(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False

x = int(input("Digite um valor: "))
if ehpar(x):
    print("O número é par!")
else:
    print("O número é impar!")
digito = int(input('Informe um número inteiro: '))

def quantidadeDigitos(digito):
    if (digito == 0):
        return 0
    return 1 + quantidadeDigitos(int(digito / 10))


print(f'O número {digito} possui {quantidadeDigitos(digito)} digitos.')
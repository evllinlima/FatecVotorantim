def verifica_numero(valor):
    if (valor > 0):
        return 'P'
    else:
        return 'N'

num = int(input('Informe um número: '))
print(f'Resultado: {verifica_numero(num)}')
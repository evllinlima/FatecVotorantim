peso_medio = 0
altura_media = 0
maior_imc = 0
menor_imc = 0

for i in range(1, 6):
    peso = float(input(f"Entre com o peso {i}: "))
    altura = float(input(f"Entre com a altura {i}: "))
    peso_medio = peso_medio + peso
    altura_media = altura_media + altura
    imc = peso / (altura ** 2)
    print("Valor do IMC é: ", imc)

    if imc > maior_imc:
        maior_imc = imc

    if menor_imc == 0 or imc < menor_imc:
        menor_imc = imc


print(f"O peso médio é {peso_medio / 5:.2f}")
print(f"A altura média é {altura_media / 5:.2f}")
print(f"O maior IMC é: {maior_imc:.2f}")
print(f"O menor IMC é: {menor_imc:.2f}")




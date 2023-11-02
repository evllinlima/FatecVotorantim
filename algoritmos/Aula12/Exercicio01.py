d = {}
maior_idade = 0

for i in range(5):
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    d[sobrenome] = idade

for sobrenome, idade in d.items():
    if idade > maior_idade:
        maior_idade = idade
        maior_sobrenome = sobrenome

print(f"O sobrenome {maior_sobrenome} possui a maior idade {maior_idade}")
ano_de_nasc = int(input("Entre com a data de nascimento: "))
ano_atual = int(input("Entre com ano atual: "))
idade_anos = ano_atual - ano_de_nasc
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 53

print("Idade em anos", idade_anos)
print("Idade em meses", idade_meses)
print("Idade em dias", idade_dias)
print("Idade em semanas", idade_semanas)



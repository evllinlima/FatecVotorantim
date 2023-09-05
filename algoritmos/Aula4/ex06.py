salario = float(input("Entre com salário: R$ "))
percentual = float(input("Entre com percentual de aumento "))
novo_salario = salario + (salario * percentual) / 100

print(f"Novo salário: R$ {novo_salario:8.2f}")

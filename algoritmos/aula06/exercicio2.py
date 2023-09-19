valor_produto = float(input("Valor do produto: "))

if (valor_produto <= 1000) :
    desconto = valor_produto * 0.10

elif (valor_produto > 1000) and (valor_produto <= 5000) :
    desconto = valor_produto * 0.20

else:
    desconto = valor_produto * 0.30

    print(f"Se o valor for {valor_produto <= 1000}, o desconto será de {valor_produto * 0.10}")
    print(f"Se o valor for {valor_produto > 1000}, o desconto será de {valor_produto * 0.20}")
    print(f"Se o valor for {valor_produto <= 5000}, o desconto será de {valor_produto * 0.30}")
    print(f"O valor total do produto será de {valor_produto - desconto}")

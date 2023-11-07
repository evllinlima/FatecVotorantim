from math import pow, pi

def calcula_volume(raio):
    return ((4 / 3) * pi * pow(raio,3))

r = float(input("Entre com o digito: "))
print(f"O valor da esfera {calcula_volume(r):.3f}")
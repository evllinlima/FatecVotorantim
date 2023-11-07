
def segundo(hora, minutos, segundos):
    return (hora * 3600 * minutos * 60 * segundos)

hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

print(f"Corresponde a {segundo(hora, minutos, segundos)} segundos!")

def valida_CPF(cpf):

    cpf = input("cpf:")

    if len(cpf) == 14:

        n1 = int(cpf[0])
        n2 = int(cpf[1])
        n3 = int(cpf[2])
        n4 = int(cpf[4])
        n5 = int(cpf[5])
        n6 = int(cpf[6])
        n7 = int(cpf[8])
        n8 = int(cpf[9])
        n9 = int(cpf[10])
        dig1 = int(cpf[12])
        dig2 = int(cpf[13])

        soma1 = (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
        resto1 = soma1 % 11

        if resto1 < 2:
            dig1 = 0
        else:
            dig1 = 11 - resto1

        soma2 = (n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (
                    dig1 * 2)
        resto2 = soma2 % 11

        if resto2 < 2:
            dig2 = 0

        else:
            dig2 = 11 - resto2

        while dig1 != int(cpf[12]) or dig2 != int(cpf[13]):
            print("CPF inválido")

            cpf = input(f"Insira seu CPF: (formato xxx.xxx.xxx-xx): ")
            n1 = int(cpf[0])
            n2 = int(cpf[1])
            n3 = int(cpf[2])
            n4 = int(cpf[4])
            n5 = int(cpf[5])
            n6 = int(cpf[6])
            n7 = int(cpf[8])
            n8 = int(cpf[9])
            n9 = int(cpf[10])
            dig1 = int(cpf[12])
            dig2 = int(cpf[13])

            soma1 = (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
            resto1 = soma1 % 11
            if resto1 < 2:
                dig1 = 0
            else:
                dig1 = 11 - resto1

            soma2 = (n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (
                    dig1 * 2)
            resto2 = soma2 % 11
            if resto2 < 2:
                dig2 = 0

            else:
                dig2 = 11 - resto2
        return True
    else:
        return False



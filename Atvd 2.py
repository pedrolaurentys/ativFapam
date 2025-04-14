print(50*"-")
print("Bem vindo ao seu definidor de par/ímpar!")
print(50*"-")

resp = input("Gostaria de usar o sistema? (S/N) ")

while resp.upper()=="S":

        tipo = input("Digite o tipo de número que quer escrever: (P/I) ")

        if resp.upper() != "S" and resp.upper():
            print("Este não é um tipo válido!")
            resp = input("Gostaria de corrigir? ")
            continue

        limite = input("Digite um número inteiro: ")
        if not limite.isdigit():
            print("Este não é um número válido!")
            resp = input("Gostaria de corrigir? (S/N) ")
            continue

        limite=int(limite)    
        numero = 0

        if tipo.upper()=="P":
            print(f"Números pares de 0 até {limite}:")
            while numero <= limite:
                if numero % 2 == 0:
                    print(numero, end=", " if numero < limite - (limite % 2) else "") #custei a fazer isso funcionar, lembrei da Fran usando 1 linha só pra vários "if"
                numero += 1
            

        elif tipo.upper()=="I":
            print(f"Números ímpares de 0 até {limite}:")
            while numero <= limite:
                if numero % 2 != 0:
                    print(numero, end=", " if numero < limite - ((limite + 1) % 2) else "") #custei a fazer isso funcionar, lembrei da Fran usando 1 linha só pra vários "if"
                numero += 1

        else:
            print("Este não é um tipo válido de número!")
        
        resp = input("\nAlguma outra definição? ")


if resp.upper()=="N":
    print("Obrigado por usar nosso sistema!")
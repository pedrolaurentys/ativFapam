print(50*"-")
print("Bem vindo ao seu contador de número par!")
print(50*"-")

resp = input("Gostaria de usar o sistema? ")

while resp.upper() =="S":

    limite = int(input("Digite um número inteiro: "))
    numero = 0

    print(f"Números pares de 0 até {limite}:")
    while numero <= limite:
        if numero % 2 == 0:
            print(numero, end=", " if numero < limite - 1 else "")
        numero +=1
    
    resp = input(" \nGostaria de usar o sistema? ")

    if resp.upper() == "N":
        print("Obrigado por escolher nosso sistema!")    
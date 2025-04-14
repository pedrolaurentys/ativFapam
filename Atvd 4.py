print(50*"-")
print("Bem vindo ao seu definidor de número primo!")
print(50*"-")

resp= input("Gostaria de usar a função agora? (S/N) ")

while resp.upper()=="S":

    limite= input("Digite o número que quer descobrir: \n")
    if not limite.isdigit():
        print("Este não é um número válido!")
        raise SystemExit    

    resto = int(limite) % 2
    restoprimo = resto/2
    limiteI = int(limite)

    if limite=="2":
        print("Este é um número primo!")
        resp = input("Gostaria de informar outro número? (S/N) \n")
        continue

    if resto !=0:
        if restoprimo % 2 != 0:
            print("Este é um número primo!")
            resp = input("Gostaria de informar outro número? (S/N) \n")    
    
    if resto == 0 and limite!=2:
        if restoprimo % 2 == 0:
            print("Este não é um número primo!")
            resp = input("Gostaria de informar outro número? (S/N) \n")    

if resp.upper()=="N":
    print("Obrigado por usar nosso sistema!")
print(50*"-")
print("Bem vindo ao seu definidor de par/ímpar!")
print(50*"-")

tipo = input("Digite o tipo de número que quer escrever: (P/I) ")

while tipo.upper()!="P" and tipo.upper()!="I":
    print("Este não é um tipo de número válido! ")
    tipo=input("Por favor, digite outro: ")

limite = input("Digite um número inteiro: ")

if not limite.isdigit:
    print("Este não é um número válido!")
    raise SystemExit
    
numero = 0

if tipo.upper()=="P":
    print(f"Números pares de 0 até {limite}:")

elif tipo.upper()=="I":
    print(f"Números ímpares de 0 até {limite}:")

else:
    print("Este não é um tipo válido de número!")

while numero <= int(limite):

    limitei=int(limite)
    
    if tipo.upper()=="P":
        if numero % 2 == 0:
            print(numero, end=", " if numero < limitei - 1 else " ") #custei a fazer isso funcionar, lembrei da Fran usando 1 linha só pra vários "if"
        numero += 1

    elif tipo.upper()=="I":
        if numero % 2 != 0:
            print(numero, end=", " if numero < limitei - 1 else " ") #custei a fazer isso funcionar, lembrei da Fran usando 1 linha só pra vários "if"

        numero += 1
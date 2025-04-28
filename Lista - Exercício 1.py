import os
import platform

def limpar():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

limpar()

#os.system('cls' if os.name == 'nt' else 'clear') se não importar platform 

print(50*"-")
print("Bem-vindo ao calculador de média")
print(50*"-")

notas=[0, 0, 0, 0]
soma = 0
x=0

resp = input("Gostaria de informar a nota? (S/N) \n")
if resp.upper()=="S":

    while x<4:
    
        notas[x] = input(f"Digite a {x+1}ª nota: ")  #usando f-strings porque é o padrão mais atual
    
        if not notas[x].replace(".", "", 1).isdigit():
            print("Nota inválida!")
            cont=input("Gostaria de informar outra nota? (S/N) \n")
            if cont.upper()=="S":
                continue
            else:
                print("Obrigado por usar nosso sistema!")
                raise SystemExit
            continue
    
        notas[x] = float(notas[x])
        int=["0 " + '- ' + '10']
    
        if notas[x]<0 or notas[x]>10:
            cont=input(f"Nota fora do intervalo!{int} Gostaria de informar outra nota? (S/N) \n")
            if cont.upper()=="S":
                continue
            else:
                print("Obrigado por usar nosso sistema!")
                raise SystemExit
            continue

        soma+=notas[x]
        x+=1
        
else:
    print("Obrigado por usar nosso sistema!")
    raise SystemExit

limpar()

print(50*"-")
print("Notas informadas e média:")
print(50*"-")

x=0

while x<4:
    print(f"A {x+1}ª nota é: {notas[x]:5.2f}")
    x+=1

print(f"\nA média é: {soma/x:5.2f}")
print(50*"-")
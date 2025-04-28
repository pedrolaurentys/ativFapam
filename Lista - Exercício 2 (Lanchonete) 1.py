import os
import platform
import time

def limpar():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

print(50*"-")
print("      Bem-vindo ao Lanchonete Cobra!")
print(50*"-")

prod = []
beb = []
qntdBeb = []
qntdProd = []
valorProd = []
valorBeb = []

resp = str(input("Você quer pedir agora? (S/N) "))

while resp.upper() == "S":
    limpar()
    
    print(50*"-")
    print("SEU PEDIDO ATUAL:")
    total = 0.0
    print(50*"-")
    
    if len(prod) > 0:
        x = 0
        while x < len(prod):
            print(prod[x] + " x" + str(qntdProd[x]) + " - R$" + "{:.2f}".format(valorProd[x]).replace(".", ","))
            total += valorProd[x]
            x += 1
    
    if len(beb) > 0:
        x = 0
        while x < len(beb):
            print(beb[x] + " x" + str(qntdBeb[x]) + " - R$" + "{:.2f}".format(valorBeb[x]).replace(".", ","))
            total += valorBeb[x]
            x += 1
    
    print(50*"-")
    print("TOTAL: R$" + "{:.2f}".format(total).replace(".", ","))
    print(50*"-")
    
    print("              CARDÁPIO:")
    print("1 - COXUDA................R$10,70")
    print("2 - ENROLADO DE PÍTON:....R$15,00")
    print("3 - BOLOVO:...............R$12,00")
    print("4 - EMPANADO:.............R$17,50")
    print("5 - REMOVER ÚLTIMO ITEM")
    print("6 - FINALIZAR PEDIDO")
    print(50*"-")

    pedido = input("Escolha uma opção: ")

    if pedido == "1":
        qntdP = input("De quantas coxudas você gostaria? ")
        if not qntdP.isdigit() or int(qntdP) <= 0:
            print("Este não é um valor aceito.")
            redo = input("Você gostaria de tentar novamente? (S/N) ")
            if redo.upper() == "N":
                print("Obrigado por escolher nossa lanchonete!")
                break
            continue
        prod.append("Coxuda")
        qntdProd.append(int(qntdP))
        valorProd.append(int(qntdP) * 10.70)

    elif pedido == "2":
        qntdP = input("De quantos enrolados de píton você gostaria? ")
        if not qntdP.isdigit() or int(qntdP) <= 0:
            print("Este não é um valor aceito.")
            redo = input("Você gostaria de tentar novamente? (S/N) ")
            if redo.upper() == "N":
                print("Obrigado por escolher nossa lanchonete!")
                break
            continue
        prod.append("Enrolado de Píton")
        qntdProd.append(int(qntdP))
        valorProd.append(int(qntdP) * 15.00)

    elif pedido == "3":
        qntdP = input("De quantos bolovos você gostaria? ")
        if not qntdP.isdigit() or int(qntdP) <= 0:
            print("Este não é um valor aceito.")
            redo = input("Você gostaria de tentar novamente? (S/N) ")
            if redo.upper() == "N":
                print("Obrigado por escolher nossa lanchonete!")
                break
            continue
        prod.append("Bolovo")
        qntdProd.append(int(qntdP))
        valorProd.append(int(qntdP) * 12.00)

    elif pedido == "4":
        qntdP = input("De quantos empanados você gostaria? ")
        if not qntdP.isdigit() or int(qntdP) <= 0:
            print("Este não é um valor aceito.")
            redo = input("Você gostaria de tentar novamente? (S/N) ")
            if redo.upper() == "N":
                print("Obrigado por escolher nossa lanchonete!")
                break
            continue
        prod.append("Empanado")
        qntdProd.append(int(qntdP))
        valorProd.append(int(qntdP) * 17.50)

    elif pedido == "5":
        if len(prod) > 0 or len(beb) > 0:
            if len(beb) > 0:
                beb.pop()
                qntdBeb.pop()
                valorBeb.pop()
            elif len(prod) > 0:
                prod.pop()
                qntdProd.pop()
                valorProd.pop()
            print("Último item removido!")
            time.sleep(1)
            continue
        else:
            print("Não há itens para remover!")
            time.sleep(1)
            continue

    elif pedido == "6":
        if len(prod) > 0 or len(beb) > 0:
            limpar()
            print("PEDIDO FINALIZADO:")
            print(50*"-")
            total = 0.0
            
            if len(prod) > 0:
                x = 0
                while x < len(prod):
                    print(prod[x] + " x" + str(qntdProd[x]) + " - R$" + "{:.2f}".format(valorProd[x]).replace(".", ","))
                    total += valorProd[x]
                    x += 1
            
            if len(beb) > 0:
                x = 0
                while x < len(beb):
                    print(beb[x] + " x" + str(qntdBeb[x]) + " - R$" + "{:.2f}".format(valorBeb[x]).replace(".", ","))
                    total += valorBeb[x]
                    x += 1
            
            print(50*"-")
            print("TOTAL: R$" + "{:.2f}".format(total).replace(".", ","))
            print(50*"-")
            print("Obrigado por escolher nossa lanchonete!")
            break
        else:
            print("Adicione itens antes de finalizar!")
            time.sleep(1)
            continue

    bebida = input("Gostaria de algo para beber? (S/N) ")

    if bebida.upper() == "S":
        print("\n1 - REFRI LATA............R$ 5,70")
        print("2 - REFRI 1 LITRO.........R$10,00")
        print("3 - REFRI 2 LITROS........R$15,00")
        print("4 - SUCO JARRA............R$17,50")
        print("5 - REMOVER ÚLTIMO ITEM")
        print("6 - FINALIZAR PEDIDO")
        print(50*"-")

        escBebida = input("Qual bebida deseja? ")
        
        if escBebida == "1":
            qntdB = input("De quantos refris lata você gostaria? ")
            if not qntdB.isdigit() or int(qntdB) <= 0:
                print("Este não é um valor aceito.")
                redo = input("Você gostaria de tentar novamente? (S/N) ")
                if redo.upper() == "N":
                    print("Obrigado por escolher nossa lanchonete!")
                    break
                continue
            beb.append("Refri Lata")
            qntdBeb.append(int(qntdB))
            valorBeb.append(int(qntdB) * 5.70)

        elif escBebida == "2":
            qntdB = input("De quantos refris 1 litro você gostaria? ")
            if not qntdB.isdigit() or int(qntdB) <= 0:
                print("Este não é um valor aceito.")
                redo = input("Você gostaria de tentar novamente? (S/N) ")
                if redo.upper() == "N":
                    print("Obrigado por escolher nossa lanchonete!")
                    break
                continue
            beb.append("Refri 1 Litro")
            qntdBeb.append(int(qntdB))
            valorBeb.append(int(qntdB) * 10.00)

        elif escBebida == "3":
            qntdB = input("De quantos refris 2 litros você gostaria? ")
            if not qntdB.isdigit() or int(qntdB) <= 0:
                print("Este não é um valor aceito.")
                redo = input("Você gostaria de tentar novamente? (S/N) ")
                if redo.upper() == "N":
                    print("Obrigado por escolher nossa lanchonete!")
                    break
                continue
            beb.append("Refri 2 Litros")
            qntdBeb.append(int(qntdB))
            valorBeb.append(int(qntdB) * 15.00)

        elif escBebida == "4":
            qntdB = input("De quantos sucos de jarra você gostaria? ")
            if not qntdB.isdigit() or int(qntdB) <= 0:
                print("Este não é um valor aceito.")
                redo = input("Você gostaria de tentar novamente? (S/N) ")
                if redo.upper() == "N":
                    print("Obrigado por escolher nossa lanchonete!")
                    break
                continue
            beb.append("Suco Jarra")
            qntdBeb.append(int(qntdB))
            valorBeb.append(int(qntdB) * 17.50)

        elif escBebida == "5":
            if len(prod) > 0 or len(beb) > 0:
                if len(beb) > 0:
                    beb.pop()
                    qntdBeb.pop()
                    valorBeb.pop()
                elif len(prod) > 0:
                    prod.pop()
                    qntdProd.pop()
                    valorProd.pop()
            print("Último item removido!")
            time.sleep(1)
            continue
        else:
            print("Não há itens para remover!")
            time.sleep(1)
            continue

    elif escBebida == "6":
        if len(prod) > 0 or len(beb) > 0:
            limpar()
            print("PEDIDO FINALIZADO:")
            print(50*"-")
            total = 0.0
            
            if len(prod) > 0:
                x = 0
                while x < len(prod):
                    print(prod[x] + " x" + str(qntdProd[x]) + " - R$" + "{:.2f}".format(valorProd[x]).replace(".", ","))
                    total += valorProd[x]
                    x += 1
            
            if len(beb) > 0:
                x = 0
                while x < len(beb):
                    print(beb[x] + " x" + str(qntdBeb[x]) + " - R$" + "{:.2f}".format(valorBeb[x]).replace(".", ","))
                    total += valorBeb[x]
                    x += 1
            
            print(50*"-")
            print("TOTAL: R$" + "{:.2f}".format(total).replace(".", ","))
            print(50*"-")
            print("Obrigado por escolher nossa lanchonete!")
            break
        else:
            print("Adicione itens antes de finalizar!")
            time.sleep(1)
            continue
        

    resp = str(input("Você quer fazer outro pedido? (S/N) "))
    if resp.upper() == "N":
        if len(prod) > 0 or len(beb) > 0:
            limpar()
            print("PEDIDO FINALIZADO:")
            print(50*"-")
            total = 0.0
            
        if len(prod) > 0:
            x = 0
            while x < len(prod):
                print(prod[x] + " x" + str(qntdProd[x]) + " - R$" + "{:.2f}".format(valorProd[x]).replace(".", ","))
                total += valorProd[x]
                x += 1
            
        if len(beb) > 0:
            x = 0
            while x < len(beb):
                print(beb[x] + " x" + str(qntdBeb[x]) + " - R$" + "{:.2f}".format(valorBeb[x]).replace(".", ","))
                total += valorBeb[x]
                x += 1
            
            print(50*"-")
            print("TOTAL: R$" + "{:.2f}".format(total).replace(".", ","))
            print(50*"-")
            print("Obrigado por escolher nossa lanchonete!")
            break
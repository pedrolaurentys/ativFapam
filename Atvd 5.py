print(50*"-")
print("      Bem-vindo ao Lanchonete Cobra!")

print(50*"-")
print("              CARDÁPIO:")
print("1 - COXUDA................R$10,70")
print("2 - ENROLADO DE PÍTON:....R$15,00")
print("3 - BOLOVO:...............R$12,00")
print("4 - EMPANADO:.............R$17,50")
print(50*"-")

resp = str(input("Você quer pedir agora? (S/N) "))

while resp.upper()=="S":
    pedido = input("O que gostaria de comer hoje? ")

    if pedido == "1":
        qntdP = input("De quantas %s você gostaria? " % "coxudas")
        if not qntdP.isdigit():
            print("Este não é um valor aceito.")
            raise SystemExit
        valorReal = int(qntdP) * 10.70
        valorFormat = "{:.2f}".format(valorReal).replace ("." , ",")
        pedidoN = "Coxuda(s)"

    elif pedido == "2":
        qntdP = input("De quantas %s você gostaria? " % "enrolados de píton")
        if not qntdP.isdigit():
            print("Este não é um valor aceito.")
            raise SystemExit
        valorReal = int(qntdP) * 15.00
        valorFormat = "{:.2f}".format(valorReal).replace ("." , ",")
        pedidoN = "Enrolado(s) de píton"

    elif pedido == "3":
        qntdP = input("De quantas %s você gostaria? " % "bolovos")
        if not qntdP.isdigit():
            print("Este não é um valor aceito.")
            raise SystemExit
        valorReal = int(qntdP) * 12.00
        valorFormat = "{:.2f}".format(valorReal).replace ("." , ",")
        pedidoN = "Bolovo(s)"

    elif pedido == "4":
        qntdP = input("De quantas %s você gostaria? " % "empanados")
        if not qntdP.isdigit():
            print("Este não é um valor aceito.")
            raise SystemExit
        valorReal = int(qntdP) * 17.50
        valorFormat = "{:.2f}".format(valorReal).replace ("." , ",")
        pedidoN = "Empanado(s)"

    bebida = input("Gostaria de algo para beber? (S/N) ")

    if bebida.upper() == "S":
        print("1 - REFRI LATA............R$ 5,70")
        print("2 - REFRI 1 LITRO.........R$10,00")
        print("3 - REFRI 2 LITROS........R$15,00")
        print("4 - SUCO JARRA............R$17,50")

        escBebida = input("Qual bebida deseja? ")
        if escBebida == "1":
            qntdB = input("De quantos %s você gostaria? " % "refris lata")
            if not qntdB.isdigit():
                print("Este não é um valor aceito.")
                raise SystemExit
            valorRealB = int(qntdB) * 5.70
            valorConj = valorRealB + valorReal
            valorFormatB = "{:.2f}".format(valorConj).replace(".", ",")
            bebidaN = "Refri(s) lata"
            print("O seu pedido é: ", qntdB, "%s" % (bebidaN), "E", qntdP, "%s" % (pedidoN))
            print("O valor total é de R$: %s" % valorFormatB)

        elif escBebida == "2":
            qntdB = input("De quantos %s você gostaria? " % "refris 1 litro")
            if not qntdB.isdigit():
                print("Este não é um valor aceito.")
                raise SystemExit
            valorRealB = int(qntdB) * 12.00
            valorConj = valorRealB + valorReal
            valorFormatB = "{:.2f}".format(valorConj).replace(".", ",")
            bebidaN = "Refri(s) 1 litro"
            print("O seu pedido é: ", qntdB, "%s" % (bebidaN), "E", qntdP, "%s" % (pedidoN))
            print("O valor total é de R$: %s" % valorFormatB)

        elif escBebida == "3":
            qntdB = input("De quantos %s você gostaria? " % "refris 2 litro")
            if not qntdB.isdigit():
                print("Este não é um valor aceito.")
                raise SystemExit
            valorRealB = int(qntdB) * 15.00
            valorConj = valorRealB + valorReal
            valorFormatB = "{:.2f}".format(valorConj).replace(".", ",")
            bebidaN = "Refri(s) 2 litros"
            print("O seu pedido é: ", qntdB, "%s" % (bebidaN), "E", qntdP, "%s" % (pedidoN))
            print("O valor total é de R$: %s" % valorFormatB)

        elif escBebida == "4":
            qntdB = input("De quantos %s você gostaria? " % "jarras de suco")
            if not qntdB.isdigit():
                print("Este não é um valor aceito.")
                raise SystemExit
            valorRealB = int(qntdB) * 17.50
            valorConj = valorRealB + valorReal
            valorFormatB = "{:.2f}".format(valorConj).replace(".", ",")
            bebidaN = "Jarra(s) de suco"
            print("O seu pedido é: ", qntdB, "%s" % (bebidaN), "E", qntdP, "%s" % (pedidoN))
            print("O valor total é de R$: %s" % valorFormatB)
     
    elif bebida.upper == "N":
        print("Este valor não é aceito")
        raise SystemExit
    
    if resp.upper() == "N":
        print("Obrigado por escolher nossa lanchonete!")
    
    resp = str(input("Você quer fazer outro pedido? (S/N) "))
   

print("Obrigado por escolher nossa lanchonete!")
menu = """

    BEM VINDO, DIGITE A OPÇÃO DESEJADA
                1 - DEPOSITAR
                2 - SACAR
                3 - EXTRATO
                0 - SAIR

"""

saldo = 0
limite_valor_por_saque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Insira o valor que deseja depositar:"))
        if valor < 1:
            print("Valor inválido, digite número inteiros e positivos.")
            
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor}  \n"
            print(f"Você depositou R${valor} com sucesso!")
            

    elif opcao == 2:
        if numero_saque >= 3:
            print("Limite de saques atingidos, tente novamente amanhã")
            
        else:
            valor = float(input("Insira o valor que deseja sacar:"))

            if valor > 500:
                print("Valor do saque maior que o permitido")
            
            elif valor < saldo:
                numero_saque += 1
                saldo -= valor
                extrato += f"Saque: R$ {valor}  \n"

                print("Saque efetuado com sucesso")

            elif valor > saldo:
                print("Saldo insuficiente!")
            
        
    elif opcao == 3:
        print(extrato)
        print (f"Saldo Atual: R$: {saldo}")

    elif opcao == 0:
        print("Obrigado por usar nossos sistemas")
        break

    else:
        print("Opção inválida, tente novamente")


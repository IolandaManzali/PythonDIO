# Desafio Bootcamp NTT Data - Enegenharia de Dados
# Criando um Sistema bancário com Pyhton

Menu = """
[1]Saque
[2]Depósito
[3]Extrato
[0]Sair

Digite aqui:
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    opção = input(Menu)

    if opção == "1":
        valor = float(input("Qual valor você deseja sacar?"))

        sem_saldo = valor > saldo
        sem_limite = valor > limite
        sem_saque = numero_saque >= limite_saque

        if sem_saldo:
            print("Saldo insuficiente para realizar essa operação")
        
        elif sem_limite:
            print(f"O valor solicitado ultrapassa o limite de saque por operação de R${limite}")
        
        elif sem_saque:
            print(f"Você ultrapassou o seu limite de saque diário de {limite_saque} por dia.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou. O valor informado é inválido.")



    elif opção == "2":
        valor = float(input("Qual valor você deseja depositar?"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido.")

    

    elif opção == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opção == "0":
        print("Volte sempre!")
        break

    else:
        print("Opção inválida. Por favor, escolha novamente:")
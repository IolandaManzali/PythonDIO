menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        # print("Depósito")

        valor = float(input("Qual valor você deseja depositar? R$ "))

        if  valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        
        else:
            print("Valor inválido. Por favor, tente novamente.")

    
    elif opcao =="s":
        # print("Saque")
        valor = float(input("Qual valor você deseja sacar? R$ "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor  > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente para realizar esse saque.")
        
        elif  excedeu_limite:
            print("Você excedeu o limite de saque. Por favor, tente novamente.")
        
        elif  excedeu_saques:
            print("Você excedeu o limite de saques. Por favor, tente novamente.")
        
        elif  valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou!. Por favor, tente novamente.")

    elif opcao == "e":
        # print("Extrato")
        print("\n===================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("\n=========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação  inválida. Tente novamente.")

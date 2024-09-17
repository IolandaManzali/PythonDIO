menu = """
      --------Bem Vindo(a) --------
      [1] - Depositar
      [2] - Sacar
      [3] - Extrato
      [0] - Sair
      -----------------------------
      -- """
saldo = 0
LIMITE_DIARIO = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} realizado com sucesso\n"
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite_diario = valor > LIMITE_DIARIO
        excedeu_saques_diarios = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite_diario:
            print("\nOperação falhou! O valor do saque excede o limite diário.")
        elif excedeu_saques_diarios:
            print("\nOperação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n--------------EXTRATO--------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------------")

    elif opcao == "0":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

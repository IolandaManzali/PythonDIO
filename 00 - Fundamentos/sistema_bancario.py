menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[p] Pix
[q] Sair

=> """

saldo = 0
limite = 500
limite_pix = 1000
extrato = ""
numero_saques = 0
numero_pix_enviados = 0
LIMITE_SAQUES = 5
LIMITE_PIX_ENVIADOS = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso! Retire o valor!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "p":
        valor = float(input("Informe o valor do pix a ser enviado: "))

        excedeu_saldo_pix = valor > saldo

        excedeu_limite_pix = valor > limite_pix

        excedeu_pix_enviados = numero_pix_enviados >= LIMITE_PIX_ENVIADOS

        if excedeu_saldo_pix:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_pix:
            print("Operação falhou! O valor da operação excede o limite de valor pix.")

        elif excedeu_pix_enviados:
            print("Operação falhou! Número máximo de envios pix excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Pix: R$ {valor:.2f}\n"
            numero_pix_enviados += 1
            print("Pix enviado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

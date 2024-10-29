menu = """\033[32m

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> \033[m"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\033[36mInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\033[31mOperação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("\033[36mInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\033[31mOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\033[31mOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\033[31mOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\033[31mOperação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\033[36m\n================ EXTRATO ================")
        print("\033[36mNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\033[36m\nSaldo: R$ {saldo:.2f}")
        print("\033[36m==========================================")

    elif opcao == "q":
        break

    else:
        print("\033[31mOperação inválida, por favor selecione novamente a operação desejada.")
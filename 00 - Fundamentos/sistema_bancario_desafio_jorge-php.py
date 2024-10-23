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

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite):
    if valor <= 0:
        print("Operação falhou! Valor inválido.")
    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print(f"Operação falhou! Limite máximo de saque é de R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Valor do depósito: R$ "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Valor do saque: R$ "))
        saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato)

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida! Tente novamente.")

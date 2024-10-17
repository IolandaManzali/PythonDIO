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

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
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
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        except ValueError:
            print("Operação falhou! Valor inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        except ValueError:
            print("Operação falhou! Valor inválido.")

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

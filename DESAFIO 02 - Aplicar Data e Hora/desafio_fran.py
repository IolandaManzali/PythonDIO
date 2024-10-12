from datetime import datetime

menu = """
Bem vinda, Fran! O que deseja?

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
quantidade_transacoes = []
LIMITE_TRANSACOES = 3

def numero_transacoes(quantidade_transacoes, tipo, valor):

    if len(quantidade_transacoes) >= LIMITE_TRANSACOES:
        print("Operação falhou! Número máximo de transações diárias excedidas.")
        return quantidade_transacoes, False
    else:
        data_hora = datetime.now().strftime("%d/%m/%Y %a %H:%M:%S")
        quantidade_transacoes.append(f"{tipo}: R$ {valor:.2f} em {data_hora}")
        return quantidade_transacoes, True

def depositar(saldo, extrato, quantidade_transacoes):
    
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        quantidade_transacoes, sucesso = numero_transacoes(quantidade_transacoes, "Depósito", valor)
        if sucesso:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} em {datetime.now().strftime("%d/%m/%Y %a %H:%M:%S")}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, quantidade_transacoes

def sacar(saldo, extrato, numero_saques, quantidade_transacoes):
        
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
        data_hora = datetime.now().strftime("%d/%m/%Y %a %H:%M:%S")
        quantidade_transacoes.append(f"Saque: R$ {valor:.2f} em {data_hora}")
        extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques, quantidade_transacoes

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)
    if opcao == "d":
        saldo, extrato, quantidade_transacoes = depositar(saldo, extrato, quantidade_transacoes)
    elif opcao == "s":
        saldo, extrato, numero_saques, quantidade_transacoes = sacar(saldo, extrato, numero_saques, quantidade_transacoes)
    elif opcao == "e":
        mostrar_extrato(saldo, extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

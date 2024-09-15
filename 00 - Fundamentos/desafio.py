'''
Desafio banco

implementar 3 operações básicas
    saque
    depósito
    extrato
'''

MENU = """
----------------------
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
----------------------
=> """

saldo = 0
extrato = []

numero_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500

def escolha_operacao():
    '''recebe entrada do usuário'''
    opcao = input(MENU)
    return opcao

def depositar():
    '''deposita valores float positivos ao saldo, ainda nao trata exceções'''
    global saldo
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:6.2f}\n")

    else:
        print("Operação falhou! O valor deve ser maior que zero.")

def sacar():
    '''subtrai valores do saldo, limite de 500'''

    global numero_saques
    global saldo

    saque = float(input("Informe o valor do saque: "))

    if saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif saque > LIMITE:
        print("Operação falhou! O valor do saque excede o limite.")

    elif saque > 0:
        saldo -= saque
        extrato.append(f"Saque:    R$ {saque:6.2f}\n")
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

def resumo():
    '''imprime extrato na tela'''
    print("\n**************** EXTRATO ****************\n")

    if len(extrato) > 0:
        for movimentacao in extrato:
            print(movimentacao)
    else:
        print("Não foram realizadas movimentações.")

    print(f"\nSaldo:    R$ {saldo:.2f}")
    print("*******************************************")

def operacao_banco():
    '''loop de execucao do programa'''
    while True:
        opcao = escolha_operacao()
        if opcao == "1":
            depositar()

        elif opcao == "2":
            #global numero_saques
            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                sacar()

        elif opcao == "3":
            resumo()

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# executa o programa
operacao_banco()

from datetime import datetime
import textwrap

menu = """
Bem vinda, Fran! O que deseja?
[d] Depositar
[s] Sacar
[e] Extrato
[cc] Criar Cliente
[ccc] Criar Conta Corrente
[q] Sair

=> """

LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
quantidade_transacoes = []
clientes = []
contas = []

# Funções de Cliente e Conta Corrente
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n Cliente já está cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

def criar_conta_corrente(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente})
        print("\n=== Conta corrente criada com sucesso! ===")
    else:
        print("\n Cliente não encontrado, criação de conta encerrada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Funções do Sistema Bancário
def numero_transacoes(quantidade_transacoes, tipo, valor):
    if len(quantidade_transacoes) >= LIMITE_TRANSACOES:
        print("Operação falhou! Número máximo de transações diárias excedidas.")
        return quantidade_transacoes, False
    else:
        data_hora = datetime.now().strftime("%d/%m/%Y %a %H:%M:%S")
        quantidade_transacoes.append(f"{tipo}: R$ {valor:.2f} em {data_hora}")
        return quantidade_transacoes, True

# positional only
def depositar(saldo, extrato, quantidade_transacoes, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        quantidade_transacoes, sucesso = numero_transacoes(quantidade_transacoes, "Depósito", valor)
        if sucesso:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %a %H:%M:%S')}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, quantidade_transacoes

# keywords only
def sacar(*, saldo, extrato, numero_saques, quantidade_transacoes):
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
        quantidade_transacoes, sucesso = numero_transacoes(quantidade_transacoes, "Saque", valor)
        if sucesso:
            extrato += f"Saque: R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %a %H:%M:%S')}\n"
            numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques, quantidade_transacoes

# positional only and keywords only
def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Loop do Menu
numero_conta = 1
while True:
    opcao = input(menu)
    if opcao == "d":
        saldo, extrato, quantidade_transacoes = depositar(saldo, extrato, quantidade_transacoes)
    elif opcao == "s":
        saldo, extrato, numero_saques, quantidade_transacoes = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, quantidade_transacoes=quantidade_transacoes)
    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
    elif opcao == "cc":
        criar_cliente(clientes)
    elif opcao == "ccc":
        criar_conta_corrente(AGENCIA, numero_conta, clientes)
        numero_conta += 1
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

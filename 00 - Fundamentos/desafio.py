import datetime

# Função para exibir o título do programa
def mostrar_titulo(txt):
    print('-' * 30)
    print(txt.center(30))
    print('-' * 30)

# Função para cadastrar cliente
def cadastrar_cliente(clientes):
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente (somente números): ")
    
    # Cadastro do cliente sem endereço
    cliente = {"nome": nome, "cpf": cpf}
    clientes.append(cliente)
    print(f"\nCliente cadastrado com sucesso!")
    print(f"Nome: {nome}\nCPF: {cpf}\n")

# Função para cadastrar conta bancária
def cadastrar_conta(contas, clientes):
    cpf_cliente = input("Informe o CPF do cliente que deseja cadastrar a conta: ")

    cliente_encontrado = next((cliente for cliente in clientes if cliente["cpf"] == cpf_cliente), None)

    if cliente_encontrado:
        numero_conta = input("Informe o número da conta: ")
        conta = {
            "numero_conta": numero_conta, 
            "cpf": cpf_cliente, 
            "saldo": 0, 
            "limite": 500, 
            "extrato": "", 
            "numero_saques": 0,
            "numero_transacoes": 0,  # Contador de transações
            "limite_transacoes": 10  # Limite de transações
        }
        contas.append(conta)

        # Mostrar os dados do cliente e da conta cadastrada
        print(f"\nConta cadastrada com sucesso para o cliente {cliente_encontrado['nome']}:")
        print(f"Nome: {cliente_encontrado['nome']}\nCPF: {cliente_encontrado['cpf']}\nNúmero da Conta: {numero_conta}\n")
    else:
        print("Cliente não encontrado. Por favor, cadastre o cliente primeiro.\n")

# Função para realizar depósito
def depositar(conta, valor):
    if conta["numero_transacoes"] >= conta["limite_transacoes"]:
        print("Você excedeu o limite de 10 transações!")
        return

    if valor > 0:
        conta["saldo"] += valor
        data_hora_atual = datetime.datetime.now()
        conta["extrato"] += f"Depósito: R$ {valor:.2f} | Data: {data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')}\n"
        conta["numero_transacoes"] += 1  # Incrementa o número de transações
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar saque
def sacar(conta, valor):
    if conta["numero_transacoes"] >= conta["limite_transacoes"]:
        print("Você excedeu o limite de 10 transações!")
        return

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= 3

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["numero_saques"] += 1
        conta["numero_transacoes"] += 1  # Incrementa o número de transações
        data_hora_atual = datetime.datetime.now()
        conta["extrato"] += f"Saque: R$ {valor:.2f} | Data: {data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para exibir extrato
def mostrar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Função para selecionar uma conta
def selecionar_conta(contas):
    numero_conta = input("Informe o número da conta: ")
    conta_encontrada = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)

    if conta_encontrada:
        return conta_encontrada
    else:
        print("Conta não encontrada.")
        return None

# Função principal
def main():
    clientes = []
    contas = []

    mostrar_titulo("Bem Vindo ao Banco")
    
    while True:
        print("""
[1] Cadastrar Cliente
[2] Cadastrar Conta Bancária
[3] Depositar
[4] Sacar
[5] Exibir Extrato
[0] Sair
""")
        opcao = input("-> ")

        if opcao == "1":
            cadastrar_cliente(clientes)

        elif opcao == "2":
            cadastrar_conta(contas, clientes)

        elif opcao == "3":
            conta_selecionada = selecionar_conta(contas)
            if conta_selecionada:
                valor = float(input("Informe o valor do depósito: "))
                depositar(conta_selecionada, valor)

        elif opcao == "4":
            conta_selecionada = selecionar_conta(contas)
            if conta_selecionada:
                valor = float(input("Informe o valor do saque: "))
                sacar(conta_selecionada, valor)

        elif opcao == "5":
            conta_selecionada = selecionar_conta(contas)
            if conta_selecionada:
                mostrar_extrato(conta_selecionada)

        elif opcao == "0":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Iniciando o programa
if __name__ == "__main__":
    main()

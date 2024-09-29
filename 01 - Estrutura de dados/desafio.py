menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    return usuario

def criar_conta(agencia, numero_conta, usuario):
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0
    }
    contas.append(conta)
    return conta

def depositar(valor, conta, extrato):
    if valor > 0:
        conta["saldo"] += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato

def sacar(valor, conta, extrato, numero_saques):
    if valor > conta["saldo"]:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato, numero_saques

def exibir_extrato(conta, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        extrato = depositar(valor, contas[0], extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        extrato, numero_saques = sacar(valor, contas[0], extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(contas[0], extrato)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        usuario = usuarios[0] if usuarios else criar_usuario(
            input("Nome: "),
            input("Data de nascimento: "),
            input("CPF: "),
            input("Endereço: ")
        )
        conta = criar_conta("0001", numero_conta, usuario)
        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")

    elif opcao == "lc":
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

    elif opcao == "nu":
        criar_usuario(
            input("Nome: "),
            input("Data de nascimento: "),
            input("CPF: "),
            input("Endereço: ")
        )
        print("Usuário criado com sucesso!")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

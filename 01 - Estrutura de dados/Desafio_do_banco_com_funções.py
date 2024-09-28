def menu():
    menu = """\n
      --------Bem Vindo(a) --------
      [1] - Depositar
      [2] - Sacar
      [3] - Extrato
      [4] - Nova Conta
      [5] - Listar Contas
      [6] - Novo usuário
      [0] - Sair
      -----------------------------
      --- """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} realizado com sucesso\n"
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, LIMITE_DIARIO, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_diario = valor > LIMITE_DIARIO
    excedeu_saques_diarios = numero_saques >= limite_saques

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
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n--------------EXTRATO--------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Usuário criado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta Criada com Sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            """
        print("-" * 100)
        print(linha)

def main():
    AGENCIA = "0001"
    saldo = 0
    LIMITE_DIARIO = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("\nInforme o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                LIMITE_DIARIO=LIMITE_DIARIO,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()

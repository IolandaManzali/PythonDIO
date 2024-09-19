import textwrap

def menu():
    menu = """
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nc]Nova conta
            [lc]Listar contas
            [nu]Novo usuário
            [q] Sair
           """  
    return input(textwrap.dedent(menu))


def depositar(saldo, valor_deposito, extrato, /):
    if(valor_deposito > 0):
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito}\n"
        print("Depósito realizado com sucesso.")
        print("Saldo atual: R$", saldo)

    else:
        print("Valor inválido")

    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if(valor_saque > saldo):
        print("Saldo insuficiente para realizar o saque.")

    elif(valor_saque > limite):
        print("Valor excede o limite.")

    elif(numero_saques >= LIMITE_SAQUES):
        print("Limite de saques diários excedido.")
    
    elif(valor_saque > 0):
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque}\n"
        print("Saque realizado com sucesso.")
        print("Saldo atual: R$", saldo)
        numero_saques += 1

    else:
        print("Valor inválido")

    return saldo, extrato


def extrato(saldo, /, *, extrato):
        print("\n-----------------------------------------")
        print("\t\tExtrato")
        print("-----------------------------------------\n")
        if(extrato == ""):
            print("Não foram realizadas movimentações.")
        print("Saldo: R$", saldo)
        print("\n-----------------------------------------")


def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nEste CPF já está cadastrado.")
        return

    nome = input("Informe o nome completo: ")

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com êxito!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = []

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com êxito!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado!")


def listar_contas(contas):

    print("\n---------------------------------------")
    print("\t\tContas")
    print("---------------------------------------\n")

    for conta in contas:
        linha = f"""\
            ---------------------------------------
            \tAgência:\t{conta['agencia']}
            \tC/C:\t\t{conta['numero_conta']}
            \tTitular:\t{conta['usuario']['nome']}
            ---------------------------------------
        """

        print(textwrap.dedent(linha))

    print("---------------------------------------")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            '''
            Operação de depósito
            
            Deve ser possível depositar valores positivos para a minha
            conta bancária. A v1 do projeto trabalha apenas com 1
            usuário, dessa forma não precisamos nos preocupar em
            identificar qual é o número da agência e conta bancária. Todos
            os depósitos devem ser armazenados em uma variável e
            exibidos na operação de extrato.
            '''

            valor_deposito = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            '''
            Operação de saque

            O sistema deve permitir realizar 3 saques diários com limite
            máximo de R$ 500,00 por saque. Caso o usuário não tenha
            saldo em conta, o sistema deve exibir uma mensagem
            informando que não será possível sacar o dinheiro por falta de
            saldo. Todos os saques devem ser armazenados em uma
            variável e exibidos na operação de extrato.
            '''

            valor_saque = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, 
                                   valor_saque=valor_saque, 
                                   extrato=extrato, 
                                   limite=limite, 
                                   numero_saques=numero_saques, 
                                   LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            '''
            Operação de extrato

            Essa operação deve listar todos os depósitos e saques
            realizados na conta. No fim da listagem deve ser exibido o
            saldo atual da conta. Se o extrato estiver em branco, exibir a
            mensagem: Não foram realizadas movimentações.
            Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
            exemplo:
            1500.45 = R$ 1500.45
            '''

            extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            '''
            Criar Usuário (cliente)

            O programa deve armazenar os usuários em uma lista, um
            usuário é composto por: nome, data de nascimento, cpf e
            endereço. O endereço é uma string com o formato: logradouro,
            cidade/sigla estado. Deve ser armazenado
            bairro
            nro
            somente os números do CPF. Não podemos cadastrar 2
            usuários com o mesmo CPF.
            '''

            criar_usuario(usuarios)

        elif opcao == "nc":
            '''
            Criar conta corrente

            O programa deve armazenar contas em uma lista, uma conta é
            composta por: agência, número da conta e usuário. O número
            da conta é sequencial, iniciando em 1. O número da agência é
            fixo: "0001". O usuário pode ter mais de uma conta, mas uma
            conta pertence a somente um usuário.
            '''

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida.")
        
main()
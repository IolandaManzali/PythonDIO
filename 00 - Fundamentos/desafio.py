'''
Desafio banco

implementar 3 operações básicas
    saque
    depósito
    extrato

desafio 2 - melhorar o sistema

usuario > nome, data de nascimento, cpf e endereço
endereço > rua, numero, bairro, cidade, estado.
so eh possivel cadastrar um cpf 
'''

def ler_valor():
    valor = float(input("Informe o valor: "))
    return valor

def escolha_operacao():
    '''recebe entrada do usuário'''
    MENU = """
    --------------------------
    ESCOLHA A OPÇÃO DESEJADA
    --------------------------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Criar conta
    [6] Listar contas
    [7] Listar usuarios
    [0] Sair
    --------------------------
=> """
    opcao = input(MENU)
    return opcao

def criar_usuario(usuarios):
    '''loop de execucao do programa'''
    cpf = input("digite apenas os numeros do CPF: ")
    if filtrar_usuario(cpf, usuarios):
        pass

    else:
        nome = input("digite o nome completo: ")
        data_nascimento = input("digite sua dada de nascimento, apenas numeros: ")
        endereco = input("digite o endereco completo, rua, numero, bairro, cidade e estado: ")
        usuarios[cpf] = {"nome": nome, "CPF": cpf, "Data de nascimento": data_nascimento, "endereço": endereco}

def criar_conta(agencia, numero_da_conta, usuarios):
    '''loop de execucao do programa'''
    cpf = input("informe o CPF do usuario: ")
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": usuario}
    else:
        print("O CPF informado não existe no sistema")

def listar_contas(contas):
    if bool(contas):
        for conta in contas:
            print(conta)
    else:
        print("ainda nao existem contas cadastradas")

def listar_usuarios(usuarios):
    if bool(usuarios):
        for usuario in usuarios:
            print(usuarios[usuario])
    else:
        print("ainda nao existem usuarios cadastrados")

def filtrar_usuario(cpf, usuarios):
    if cpf in usuarios:
        print ("usuario ja cadastrado")
        return usuarios[cpf]

def depositar(saldo, valor, extrato, /):
    '''deposita valores float positivos ao saldo, ainda nao trata exceções'''
    saldo = saldo
    valor = valor
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:6.2f}\n"
        print("Deposito realizado com sucesso!.")

    else:
        print("Operação falhou! O valor deve ser maior que zero.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite,numero_saques, limite_saques ):
    '''subtrai valores do saldo, limite de 500'''

    print(numero_saques)
    print(limite_saques)
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Você atingiu o limite diário de saques.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:6.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    '''imprime extrato na tela'''
    print("\n**************** EXTRATO ****************\n")

    print(extrato)
    # if len(extrato) > 0:
    #     for movimentacao in extrato:
    #         print(movimentacao)
    # else:
    #     print("Não foram realizadas movimentações.")

    print(f"\nSaldo:    R$ {saldo:.2f}")
    print("*******************************************")

def main():
    '''loop de execucao do programa'''

    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = {} # chave = CPF, valor = nome
    contas = []

    while True:
        opcao = escolha_operacao()
        if opcao == "1":
            valor = ler_valor()
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = ler_valor()
            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                saldo, extrato, numero_saques = sacar(saldo = saldo,
                      valor = valor,
                      extrato = extrato,
                      limite = LIMITE,
                      numero_saques = numero_saques,
                      limite_saques=LIMITE_SAQUES,)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_da_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == "7":
            listar_usuarios(usuarios)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# executa o programa
main()


# Desafio Bootcamp NTT Data - Enegnharia de Dados
# Implementando Data e Hora no Sistema bancário com Pyhton

import textwrap #entender o que é esse textwrap depois


def Menu ():
    Menu = """
    [1]Saque
    [2]Depósito
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuário
    [0]Sair


    Digite aqui:
"""
    return input(textwrap.dedent(Menu))


def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
        sem_saldo = valor > saldo
        sem_limite = valor > limite
        sem_saque = numero_saque >= limite_saque

        if sem_saldo:
            print("Saldo insuficiente para realizar essa operação")
        
        elif sem_limite:
            print(f"O valor solicitado ultrapassa o limite de saque por operação de R${limite}")
        
        elif sem_saque:
            print(f"Você ultrapassou o seu limite de saque diário de {limite_saque} por dia.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou. O valor informado é inválido.")

        return saldo, extrato


def deposito(saldo, valor, extrato,/):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido.")

        return saldo, extrato

def exibir_extrato (saldo, /,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = Menu()

        if opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )

        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "3":
            exibir_extrato (saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
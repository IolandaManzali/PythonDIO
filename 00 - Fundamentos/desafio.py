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

        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito}\n"
            print("Depósito realizado com sucesso.")
            print("Saldo atual: R$", saldo)

        else:
            print("Valor inválido")

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

        print("\n-----------------------------------------")
        print("\t\tExtrato")
        print("-----------------------------------------\n")
        if(extrato == ""):
            print("Não foram realizadas movimentações.")
        print("Saldo: R$", saldo)
        print("\n-----------------------------------------")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

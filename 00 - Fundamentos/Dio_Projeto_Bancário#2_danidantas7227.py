menu = """
Escolha a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] (Cadastro de Usuário)
[5] (Cadastro de conta Bancária)
[0] Sair

 => """

saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3
usuarios = []
contas_bancárias = [] 
agencia = str("0001")



def deposito(saldo, extrato, /):
    print("\n***Operação de Depósito selecionada***") 

    valor = float(input("\nInforme o valor do Depósito: "))
        
    if valor > 0: 

            saldo += valor 
            print("\nValor depositado com sucesso!")    
            extrato = extrato + f"Depósito de {valor:.2f} efetuado.\n"

    else: print("Valor insuficiente para depósito!")

    return saldo, extrato



def saque(*, saldo, extrato, limite, numeros_saque, LIMITE_SAQUE):
    print("\n***Operação de Saque selecionada***")   

    valor = float(input("\nInforme o valor do Saque: "))

    if valor > saldo:
            print("Saque inválido devido: Saldo insuficiente!")          
        
    elif numeros_saque >= LIMITE_SAQUE:
            print("Saque inválido devido: Limite de Saque diário excedido!")
            
    elif valor > limite:
            print("Saque inválido devido: Valor superior a 500 reais!")

    else: 
            saldo -= valor
            numeros_saque += 1
            print("Saque efetuado com sucesso!")
            extrato = extrato + f"Saque de {valor:.2f} efetuado.\n" 

    return saldo, extrato, numeros_saque



def histórico(saldo, /, *, extrato):
    print("\n***Operação de Extrato selecionada***\n")  
        
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo Atual: R$ {saldo:.2f}")  


def cadastrar_usuario(usuarios):
    print("\n***Operação de Cadastro de Cliente Selecionada***\n")

    nome = input("\nInforme seu nome completo:")
    data_nascimento = input("Informe sua data de nascimento:")
    cpf = input("Informe seu CPF(Somente números):")    
    endereço = input("Informe seu endereço:")
    

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nCPF já cadastrado! Tente novamente:\n")  
        return cadastrar_usuario(usuarios)



    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereço": endereço})
    print("Cliente cadastrado com sucesso!\n")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def cadastrar_conta(agencia, usuario, numero_conta):
    cpf = input("\nPara a criação de uma nova conta, Informe seu CPF:")
     
    verificacao = filtrar_usuario(cpf, usuarios) 

    if verificacao:
        print("\nUsuário encontrado. Conta criada com sucesso!")
        print(f"\nSua Agência: {agencia}\nNúmero da conta: {numero_conta}\nSeu Usuário: {usuario}\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else: print("\nErro ao tentar criar conta, Usuário não cadastrado!!")

while True:

    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "2":    
        saldo, extrato, numeros_saque = saque(extrato= extrato, limite= limite, LIMITE_SAQUE= LIMITE_SAQUE, saldo= saldo, numeros_saque= numeros_saque)

    elif opcao == "3":
        histórico(saldo, extrato= extrato)    
          
    elif opcao == "4":
        cadastrar_usuario(usuarios)          
            
    
    elif opcao == "5":      
        print("\n***Operação de Cadastro de Conta bancária Selecionado***")
       
        numero_conta = len(contas_bancárias) + 1 
        contas = cadastrar_conta(agencia= agencia, numero_conta= numero_conta, usuario= usuarios)

        if contas:
            contas_bancárias.append(contas)


    elif opcao == "0":
        print("Saindo...")
        break

    else: print("\nOperação inválida! Tente novamente.")        
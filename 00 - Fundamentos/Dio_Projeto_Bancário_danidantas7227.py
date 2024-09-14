menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3

while True:

    opção = input(menu)

    if opção == "1":
        print("\n***Operação de Depósito selecionada***") 

        valor = float(input("\nInforme o valor do Depósito: "))
        
        if valor > 0: 

            saldo += valor 
            print("\nValor efetuado com sucesso!")    
            extrato = extrato + f"Depósito de {valor:.2f} efetuado.\n"

        else: print("Valor insuficiente para depósito!") 



    elif opção == "2":    
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



    elif opção == "3":

        print("\n***Operação de Extrato selecionada***\n")  
        
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo Atual: R$ {saldo:.2f}")


    elif opção == "0":
        print("Saindo...")
        break

    else: print("\nOperação inválida! Tente novamente.")        
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
quantidade_depositos = 0
total_saque = 0

while True:
    opcao = input(menu)

    if opcao == "d":
      
      deposito = int(input("informe o valor que deseja depositar: "))
      if deposito > 0:
          saldo += deposito
          quantidade_depositos += 1
          print("Deposito realizado com sucesso!")
          extrato += f"Desposito: {deposito:.2f}\n"
      else:
          print("Informe um valor positivo para deposito")    
      
    elif opcao == "s":
     
      if numero_saques < LIMITE_SAQUE:    
           saque = int(input("Informe o valor que deseja sacar: "))
           
           if saque <= limite:
               if saque <= saldo:
                   print(f"Saque no valor R$ {saque:.2f} realizado com sucesso!")
                   saldo -= saque
                   total_saque += saque
                   numero_saques += 1
                   extrato += f"Saque R${saque:.2f}\n"
               else:
                   print(f"Você não possue saldo suficiente para sacar R${saque}! seu saldo atual: R${saldo} ")              
           else:
                print("Você atingiu o limite diárdio de saques!")        
      else:
          print("Você atngiu a quantidade de saques...")     
              
    
    elif opcao == "e":
        print("\n++++++++++++++++++++ Extrato ++++++++++++++++++++")
        print("Não foi realizado nenhuma operação" if not extrato else extrato)
        print("...................................................")
        print(f"Depositos realizados {quantidade_depositos}\nQuantidade saques {numero_saques}\nValor total de saque R${total_saque:.2f} \nSaldo em conta R$:{saldo:.2f}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    elif opcao == "q":
        print("Encerrando sistema...")
        break
    else:
        print("Opcao invalidade, tente outra opção!")
            
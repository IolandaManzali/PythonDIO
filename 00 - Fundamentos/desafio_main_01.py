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
limite_saques = 3

while True:
  opcao = input(menu) 

  if opcao == "d":
    valor = float(input("Informe o valor do deposito: R$ "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
      print("Operação falhou! O valor é inválido.")
    
  
  elif opcao == "s":
    valor = float(input("Informe o valor de saque: R$ "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
      print("Operação falou! Você não tem saldo suficiente.")
    elif excedeu_limite:
      print("Operação falou! O valor excede o limite de saque.")
    elif excedeu_saques:
      print("Operação falhou! Você excedeu a quantidade de saques do dia.")
    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
    else:
      print("Operação falhou! O valor informado é inválido.")

  
  elif opcao == "e":
    print(f"\n{'='*10} EXTRATO {'='*10}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print(f"\n {'=' *20}")
  
  elif opcao == "q":
    break
  
  else:
    print("Operação Invalida, por favor selecione novamente a operação desejada.")
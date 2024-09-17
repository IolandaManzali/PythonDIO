##DESAFIO Banco##

menu=(
  """
  ========Menu=========
  
  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [0] - Sair
  
  ======================
  """
)
saldo, limite_diario_saque, numero_saques = 0, 500, 0
extrato, LIMITE_SAQUES = "", 3

while True:
  opcoes = input(menu)
  
               ### DEPOSITAR###
  if opcoes == "1":
    valor = float(input("Qual o valor do deposito?\n\n"))
    if valor > 0:
      saldo += valor
      extrato += f"Desposito na c/c R${valor:.2f}\n"
      
      print(f"Valor depositado foi de: R${valor}")
    else:
      print('O valor informado não é válido')
      
    
              ### SACAR###
  elif  opcoes == "2":
      valor = float(input("Qual o valor do saque?\n\n"))
      limite_excedeu = valor > limite_diario_saque
      saldo_excedeu = valor > saldo
      saque_numeros =  numero_saques >= LIMITE_SAQUES
      
     
      
      if limite_excedeu:   
        print(f'Limite de saque por dia excedido R$ ',{limite_diario_saque})
        
      elif saldo_excedeu:   
        print(f'Saldo insuficiente R$ ',{saldo})
        
      elif saque_numeros:   
        print(f'Ultrapassou o limite de saque por dia:',{numero_saques})
       
            
      elif  valor > 0:
        saldo  -= valor    
        extrato += f"Saque na c/c R${valor:.2f}\n"
        numero_saques += 1
        print(f"Valor sacado foi de: R${valor}")
        
      else:
        print('O valor informado não é válido')
        
         ### EXTRATO###
  elif opcoes == "3":
    print("\n========EXTRATO=============")
    print("Sem Movimentações" if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("\n============================")
  
  elif opcoes == "0":
    break
  
  else:
    print('Opção inválida digite uma das opçoes: 1, 2, ou 3')     
          
    

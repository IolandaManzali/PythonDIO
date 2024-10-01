import os

LIMITE_NUM_SAQUES = 3
LIMITE_VALOR_SAQUES = 500
numero_de_saques = 0
saldo = 0
extrato = ""

status_msg = "Seja bem-vindo!"

menu = """
================= MENU =================

    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    
========================================="""

def limpar_tela():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

while True:       
      
    limpar_tela()
            
    print(f"\n{status_msg.center(40," ")}")
    
    print(menu)    
    
    selecao = input("Escolha uma operação ou [q] para sair: ")     
    
    if selecao.lower() == "d": 
        valor = float(input("Digite o valor do depósito: "))        
        if valor >= 0:        
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"
            status_msg = "Desósito realizado com sucesso!"                        
        else:
            status_msg = "Operação falhou! O valor informado é inválido."
        
    elif selecao.lower() == "s": 
        valor = float(input("Digite o valor do saque: "))
                
        excedeu_saldo = valor > saldo    
        excedeu_limite = numero_de_saques >= LIMITE_NUM_SAQUES        
        excedeu_valor = valor > LIMITE_VALOR_SAQUES 
    
        if excedeu_limite:
            status_msg = ("Você excedeu limite diário de saque!")
        elif excedeu_valor:
            status_msg = "Você excedeu valor diário de saque!"       
        elif excedeu_saldo:
            status_msg = "Operação falhou! Você não tem saldo suficiente."
        else:                                    
            extrato += f"Saque R$ {valor:.2f}\n"
            saldo -= valor
            numero_de_saques += 1                        
            status_msg = "Saque realizado com sucesso!"
            
    #extrato
    elif selecao.lower() == "e": 
        print(" EXTRATO ".center(40,"="))
        print(" Não foram realizadas movimentações." if not extrato else extrato)        
        print(f"\n\n Saldo R$ {saldo:.2f}")
        print("".center(40,"="))        
        input('Pressione "Enter" para voltar ao menu! ')            
        status_msg = "Bem-vindo de volta!"
    
    #sair     
    elif selecao.lower() == "q":
        print("Obrigado, volte sempre!")
        break    
    else:
        status_msg = "Operação inválida, por favor selecione novamente a operação desejada."
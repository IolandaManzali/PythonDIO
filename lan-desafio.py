import os
import time

def centralizar_texto(texto, largura=50, caractere_preenchimento=' '):
    texto_centralizado = texto.center(largura, caractere_preenchimento)
    return texto_centralizado

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    limpar_tela()
    print(centralizar_texto(" NTT BANK ", caractere_preenchimento='*'))
    print(centralizar_texto(" OPERAÇÕES BÁSICAS ", caractere_preenchimento='*'))
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Qual operação deseja realizar?
=> """
    return input(menu).lower()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(centralizar_texto(" OBRIGADA POR USAR O NTT BANK ", caractere_preenchimento='*'))
        else:
            print("Operação falhou! O valor informado é inválido.")
        time.sleep(2)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        time.sleep(2)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        print(centralizar_texto(" OBRIGADA POR USAR O NTT BANK ", caractere_preenchimento='*'))

        time.sleep(5)

    elif opcao == "q":
        print("Saindo do sistema...")
        print(centralizar_texto(" OBRIGADA POR USAR O NTT BANK ", caractere_preenchimento='*'))

        time.sleep(2)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        time.sleep(2)

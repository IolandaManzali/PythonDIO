from datetime import date
import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

from datetime import datetime

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f} em {data_formatada}\n"
            print(extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. (R$ 500,00 por saque)")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. (3 por dia)")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} em {data_formatada}\n"
            numero_saques += 1
            print(extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f} em {data_formatada}")
        print("==========================================")

    elif opcao == "x":
        print("Agradecemos por utilizar nossos serviços! Até logo!" )
        break


    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
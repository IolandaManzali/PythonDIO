# Desafio Bootcamp NTT Data - Enegnharia de Dados
# Modelando o Sistema Bancário em POO com Python

import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente para realizar essa operação")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou. O valor informado é inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Operação falhou. O valor informado é inválido.")
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super(). __init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "saque"])

        excedeu_saque = numero_saques > self.limite_saque
        excedeu_limite = valor > self.limite

        if excedeu_saque:
            print (f"você excedeu o seu número de {self.limite_saque} por dia.")
        elif excedeu_limite:
            print (f"Erro na operação. Seu limite de saque diário é de R${self.limite} por dia.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class saque(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class deposito(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def Menu ():
    Menu = """
    \t ====== Para acessar os serviços, escolha uma das opções abaixo ======
    [1]Depósito
    [2]Saque
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuário
    [0]Sair
    \t
    Digite aqui:
"""
    return input(textwrap.dedent(Menu))


def procurar_cliente (cpf, clientes):
    clientes_procurados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_procurados[0] if clientes_procurados else None

def cliente_sem_conta(cliente):
    if not cliente.contas:
        print("Você não possui conta")
        return None
    return cliente.contas[0]

def depositar (cliente):
    cpf = input ("Qual o número do seu CPF?")
    cliente = procurar_cliente(cpf, cliente)

    if not cliente:
        print ("CPF não encontrado. Para criar uma nova conta, por favor escolha a opção 6. Caso contrário, entre em contato com o seu gerente.")
        return
    
    valor = float(input("informe o valor para depósito:"))
    transacao = deposito (valor)

    conta = cliente_sem_conta(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar (cliente):
    cpf = input ("Qual o número do seu CPF?")
    cliente = procurar_cliente(cpf, cliente)

    if not cliente:
        print ("Essa conta não existe. Por favor, entre em contato com o seu gerente.")
        return
    
    valor = float(input("informe o valor para saque:"))
    transacao = saque (valor)

    conta = cliente_sem_conta(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def extrato(clientes):
    cpf = input("Qual o número do seu CPF?")
    cliente = procurar_cliente(cpf, clientes)

    if not cliente:
        print("Essa conta não existe. Por favor, entre em contato com o seu gerente.")
        return
    
    conta = cliente_sem_conta(cliente)
    if not conta:
        print("Cliente não possui conta. Por favor entre em contato com o seu gerente")
        return
    
    print("\n=== EXTRATO ===")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}:\tR$ {transacao['valor']:.2f} em {transacao['data']}\n"

    print(extrato)
    print(f"Saldo atual:\tR$ {conta.saldo:.2f}")

def nova_conta (clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = procurar_cliente(cpf, clientes)

    if cliente:
        print("Erro na operação. Já existe cliente com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Rua, número - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = procurar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []


    while True:
        opcao = Menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            extrato(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            nova_conta(clientes)

        elif opcao == "0":
            print("Volte sempre!")
            break

        else:
            print("Opção inválida")

main()
from datetime import datetime
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })

class Conta(ABC):
    def __init__(self, cliente, numero):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

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

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido.")
        else:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n Operação falhou! O valor informado é inválido.")
        return False

    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        Conta Corrente:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """

class Banco:
    agencia = "0001"
    numero_conta = 1
    clientes = []
    contas = []

    @classmethod
    def criar_cliente(cls, nome, data_nascimento, cpf, endereco):
        cliente_existente = cls.filtrar_cliente(cpf)
        if cliente_existente:
            print("Cliente já cadastrado.")
            return None

        cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
        cls.clientes.append(cliente)
        print("Cliente criado com sucesso!")
        return cliente

    @classmethod
    def criar_conta_corrente(cls, cliente):
        conta = ContaCorrente(cls.numero_conta, cliente)
        cliente.adicionar_conta(conta)
        cls.contas.append(conta)
        cls.numero_conta += 1
        print("Conta corrente criada com sucesso!")
        return conta

    @classmethod
    def filtrar_cliente(cls, cpf):
        for cliente in cls.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    @staticmethod
    def listar_contas():
        for conta in Banco.contas:
            print(f"Agência: {conta.agencia} | C/C: {conta.numero} | Titular: {conta.cliente.nome}")

# Loop de execução do sistema bancário
menu = """Bem vinda, Fran! O que deseja?
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[cc] Cadastrar Cliente
[q] Sair

=> """

banco = Banco()

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        cpf = input("Informe o CPF do cliente: ")
        cliente = banco.filtrar_cliente(cpf)
        if cliente:
            valor = float(input("Informe o valor do depósito: "))
            conta = cliente.contas[0]  # Supondo que o cliente tenha apenas uma conta
            cliente.realizar_transacao(conta, Deposito(valor))
        else:
            print("Cliente não encontrado.")
    
    elif opcao == 's':
        cpf = input("Informe o CPF do cliente: ")
        cliente = banco.filtrar_cliente(cpf)
        if cliente:
            valor = float(input("Informe o valor do saque: "))
            conta = cliente.contas[0]  # Supondo que o cliente tenha apenas uma conta
            cliente.realizar_transacao(conta, Saque(valor))
        else:
            print("Cliente não encontrado.")
    
    elif opcao == 'e':
        cpf = input("Informe o CPF do cliente: ")
        cliente = banco.filtrar_cliente(cpf)
        if cliente:
            conta = cliente.contas[0]  # Supondo que o cliente tenha apenas uma conta
            conta.mostrar_extrato()
        else:
            print("Cliente não encontrado.")
    
    elif opcao == 'nc':
        cpf = input("Informe o CPF do cliente: ")
        cliente = banco.filtrar_cliente(cpf)
        if cliente:
            banco.criar_conta_corrente(cliente)
        else:
            print("Cliente não encontrado.")
    
    elif opcao == 'lc':
        banco.listar_contas()
    
    elif opcao == 'cc':
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")
        banco.criar_cliente(nome, data_nascimento, cpf, endereco)
    
    elif opcao == 'q':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

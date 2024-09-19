from datetime import date, datetime 
from Códigos_Python.Desafio_Projeto_Bancário_3_danidantas7227 import Cliente, Transacao, Historico
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

class Conta:
    def __init__(self, _numero: int, _cliente: Cliente,):
        self._saldo = 0
        self._numero = _numero
        self._agencia = "29018"
        self._cliente = _cliente
        self._historico= Historico()
    
    @property
    def saldo(self):
        return self.saldo
    
    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return Conta

    @property
    def sacar(self, valor: float):
        saldo = self.saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print("Saldo insuficiente!!")

        elif valor > 0:
            self.saldo -= valor
            print("Saque realizado com sucesso!!!")
            return True

        else: print("Valor inválido para a operação!!")
        return False    


    @property
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")

        else: 
            print("Valor inválido para a operação") 
            return False           
        
        return True



class Conta_Corrente(Conta):
    def __init__(self, _numero: int, _cliente: Cliente, _limite = float, _limite_saques = int):
        super().__init__(_numero, _cliente)
        self._limite = _limite
        self._limite_saques = _limite_saques

    @property
    def sacar(self, valor: float):
        saldo = self.saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print("Saldo insuficiente!!")

        elif valor > 0:
            self.saldo -= valor
            print("Saque realizado com sucesso!!!")
            return True

        else: print("Valor inválido para a operação!!")
        return False    


    @property
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")

        else: 
            print("Valor inválido para a operação") 
            return False           
        
        return True    



class Cliente:
    def __init__(self, _endereco: str, _contas: list):
        self._endereco = _endereco
        self._contas = _contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
   
    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)



class Pessoa_Fisica(Cliente):
    def __init__(self, _endereco: str, _contas: list, _cpf: str, _nome: str, _data_nascimento: date):
        super().__init__(_endereco, _contas)
        self._cpf = _cpf
        self._nome = _nome
        self._data_nascimento = _data_nascimento



class Historico():
    def __init__(self):
        self.transacoes = []    

    @abstractmethod
    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append({f"Tipo: {transacao.__class__.__name__}\nValor: {transacao.valor}\nData: {datetime.now()}"})



class Transacao(ABC):    
    @abstractclassmethod
    def registrar(self, conta: Conta):
        pass
    
    @property
    @abstractproperty
    def valor(self):
        pass



class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        conta._historico.adicionar_transacao(self)   



class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        conta._historico.adicionar_transacao(self)    
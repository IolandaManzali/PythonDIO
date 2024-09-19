import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Usuario):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, usuario):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, usuario, numero):
        return cls(numero, usuario)

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
    def usuario(self):
        return self._usuario

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor_saque):

        if(valor_saque > self._saldo):
            print("Saldo insuficiente para realizar o saque.")

        # elif(valor_saque > self.limites["saque"]):
        #     print("Valor excede o limite.")
        
        elif(valor_saque > 0):
            self._saldo -= valor_saque
            # extrato += f"Saque: R$ {valor_saque}\n"
            print("Saque realizado com êxito.")
            print("Saldo atual: R$", self._saldo)

        else:
            print("Valor inválido")

        return False

    def depositar(self, valor_deposito):

        if(valor_deposito > 0):
            self._saldo += valor_deposito
            # extrato += f"Depósito: R$ {valor_deposito}\n"
            
            print("Depósito realizado com sucesso.")
            print("Saldo atual: R$", self.saldo)

        else:
            print("Valor inválido")
            return False

        return True
    

class ContaCorrente(Conta):
    def __init__(self, numero, usuario, limite=500, limite_saques=3):
        super().__init__(numero, usuario)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if(valor > self._limite):
            print("\nO valor do saque excede o limite!")

        elif(numero_saques >= self._limite_saques):
            print("\nNúmero máximo de saques excedido!")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.usuario.nome}
        """
    

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
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
        validar_transacao = conta.sacar(self.valor)

        if validar_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        validar_transacao = conta.depositar(self.valor)

        if validar_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nc]Nova conta
            [lc]Listar contas
            [nu]Novo usuário
            [q] Sair\n
           """  
    return input(textwrap.dedent(menu))


def depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)
    
def sacar(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)


def extrato(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nCliente não encontrado!")
        return
    
    conta = recuperar_conta_usuario(usuario)

    if not conta:
        return

    print("\n-----------------------------------------")
    print("\t\tExtrato")
    print("-----------------------------------------")
    transacoes = conta.historico.transacoes
    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")

    print("\n-----------------------------------------")


def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nEste CPF já está cadastrado.")
        return

    nome = input("Informe o nome completo: ")

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    usuarios.append(usuario)

    print("Usuário criado com êxito!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado!")
        return
    
    conta = ContaCorrente.nova_conta(usuario=usuario, numero=numero_conta)
    contas.append(conta)
    usuario.contas.append(conta)

    print("Conta criada com êxito!")

def recuperar_conta_usuario(usuario):
    if not usuario.contas:
        print("\nUsuário não possui conta.")
        return

    # FIXME: não permite usuário escolher a conta
    return usuario.contas[0]

def listar_contas(contas):

    print("\n---------------------------------------")
    print("\t\tContas")
    print("---------------------------------------\n")

    for conta in contas:
        # linha = f"""\
        #     ---------------------------------------
        #     \tAgência:\t{conta['agencia']}
        #     \tC/C:\t\t{conta['numero_conta']}
        #     \tTitular:\t{conta['usuario']['nome']}
        #     ---------------------------------------
        # """

        # print(textwrap.dedent(linha))

        print(textwrap.dedent(str(conta)))

    print("---------------------------------------")


def main():
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            '''
            Operação de depósito
            
            Deve ser possível depositar valores positivos para a minha
            conta bancária. A v1 do projeto trabalha apenas com 1
            usuário, dessa forma não precisamos nos preocupar em
            identificar qual é o número da agência e conta bancária. Todos
            os depósitos devem ser armazenados em uma variável e
            exibidos na operação de extrato.
            '''

            depositar(usuarios)

        elif opcao == "s":
            '''
            Operação de saque

            O sistema deve permitir realizar 3 saques diários com limite
            máximo de R$ 500,00 por saque. Caso o usuário não tenha
            saldo em conta, o sistema deve exibir uma mensagem
            informando que não será possível sacar o dinheiro por falta de
            saldo. Todos os saques devem ser armazenados em uma
            variável e exibidos na operação de extrato.
            '''

            sacar(usuarios)

        elif opcao == "e":
            '''
            Operação de extrato

            Essa operação deve listar todos os depósitos e saques
            realizados na conta. No fim da listagem deve ser exibido o
            saldo atual da conta. Se o extrato estiver em branco, exibir a
            mensagem: Não foram realizadas movimentações.
            Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
            exemplo:
            1500.45 = R$ 1500.45
            '''

            extrato(usuarios)

        elif opcao == "nu":
            '''
            Criar Usuário (usuario)

            O programa deve armazenar os usuários em uma lista, um
            usuário é composto por: nome, data de nascimento, cpf e
            endereço. O endereço é uma string com o formato: logradouro,
            cidade/sigla estado. Deve ser armazenado
            bairro
            nro
            somente os números do CPF. Não podemos cadastrar 2
            usuários com o mesmo CPF.
            '''

            criar_usuario(usuarios)

        elif opcao == "nc":
            '''
            Criar conta corrente

            O programa deve armazenar contas em uma lista, uma conta é
            composta por: agência, número da conta e usuário. O número
            da conta é sequencial, iniciando em 1. O número da agência é
            fixo: "0001". O usuário pode ter mais de uma conta, mas uma
            conta pertence a somente um usuário.
            '''

            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida.")
        
main()
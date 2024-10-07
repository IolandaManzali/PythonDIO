import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    """
    Classe base que representa um cliente do sistema bancário.
    Cada cliente possui um endereço e pode ter várias contas.
    """

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Inicializa uma lista de contas associadas ao cliente

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta específica.

        :param conta: Conta na qual a transação será realizada.
        :param transacao: Transação a ser registrada na conta.
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.

        :param conta: Conta a ser adicionada.
        """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Classe que representa um cliente do tipo Pessoa Física.
    Extende a classe Cliente com informações adicionais como nome, data de nascimento e CPF.
    """

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe pai
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """
    Classe base que representa uma conta bancária.
    Cada conta possui um número, agência, cliente associado, saldo e um histórico de transações.
    """

    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial
        self._numero = numero
        self._agencia = "0001"  # Agência padrão
        self._cliente = cliente
        self._historico = Historico()  # Inicializa o histórico de transações

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Método de classe para criar uma nova conta.

        :param cliente: Cliente associado à nova conta.
        :param numero: Número da nova conta.
        :return: Instância da nova conta.
        """
        return cls(numero, cliente)

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self._saldo

    @property
    def numero(self):
        """Retorna o número da conta."""
        return self._numero

    @property
    def agencia(self):
        """Retorna a agência da conta."""
        return self._agencia

    @property
    def cliente(self):
        """Retorna o cliente associado à conta."""
        return self._cliente

    @property
    def historico(self):
        """Retorna o histórico de transações da conta."""
        return self._historico

    def sacar(self, valor):
        """
        Realiza um saque na conta, se o valor for válido e o saldo for suficiente.

        :param valor: Valor a ser sacado.
        :return: True se o saque for bem-sucedido, False caso contrário.
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        """
        Realiza um depósito na conta, se o valor for válido.

        :param valor: Valor a ser depositado.
        :return: True se o depósito for bem-sucedido, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente, que possui limites específicos para saques.
    """

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe pai
        self._limite = limite  # Limite de saque
        self._limite_saques = limite_saques  # Limite de saques permitidos

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, verificando limites de saque e quantidade de saques realizados.

        :param valor: Valor a ser sacado.
        :return: True se o saque for bem-sucedido, False caso contrário.
        """
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)  # Chama o método sacar da classe pai

    def __str__(self):
        """Retorna uma representação textual da conta corrente."""
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """
    Classe que representa o histórico de transações de uma conta.
    """

    def __init__(self):
        self._transacoes = []  # Inicializa uma lista para armazenar transações

    @property
    def transacoes(self):
        """Retorna a lista de transações."""
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma nova transação ao histórico.

        :param transacao: Transação a ser adicionada.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    """
    Classe abstrata que representa uma transação bancária.
    """

    @property
    @abstractproperty
    def valor(self):
        """Retorna o valor da transação."""
        pass

    @abstractclassmethod
    def registrar(self, conta):
        """
        Método abstrato para registrar a transação em uma conta.

        :param conta: Conta na qual a transação será registrada.
        """
        pass


class Saque(Transacao):
    """
    Classe que representa uma transação de saque.
    """

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do saque."""
        return self._valor

    def registrar(self, conta):
        """
        Registra a transação de saque na conta.

        :param conta: Conta onde a transação será registrada.
        """
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe que representa uma transação de depósito.
    """

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do depósito."""
        return self._valor

    def registrar(self, conta):
        """
        Registra a transação de depósito na conta.

        :param conta: Conta onde a transação será registrada.
        """
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    """Exibe o menu de opções para o usuário."""
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    """
    Filtra um cliente pelo CPF.

    :param cpf: CPF do cliente a ser filtrado.
    :param clientes: Lista de clientes para filtragem.
    :return: Cliente filtrado ou None se não encontrado.
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta de um cliente.

    :param cliente: Cliente do qual se deseja recuperar a conta.
    :return: Conta do cliente ou None se não houver conta.
    """


    """
    Código para o desenho do diagrama em Python
    """
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Criando a figura e o eixo
fig, ax = plt.subplots(figsize=(12, 8))

# Desenhando as classes no diagrama UML
classes = {
    "Cliente": (1, 6),
    "PessoaFisica": (1, 5),
    "Conta": (1, 4),
    "ContaCorrente": (1, 3),
    "Historico": (1, 2),
    "Transacao": (3, 4),
    "Deposito": (3, 3),
    "Saque": (3, 2)
}

# Desenho dos retângulos para cada classe
for class_name, (x, y) in classes.items():
    ax.add_patch(patches.Rectangle((x - 0.4, y - 0.4), 0.8, 0.6, fill=True, edgecolor='black', facecolor='lightgray'))
    ax.text(x, y, class_name, fontsize=12, ha='center', va='center')

# Desenho das relações
relationships = [
    ("Cliente", "PessoaFisica"),
    ("Cliente", "Conta"),
    ("Conta", "ContaCorrente"),
    ("Transacao", "Deposito"),
    ("Transacao", "Saque")
]

for parent, child in relationships:
    parent_coords = classes[parent]
    child_coords = classes[child]
    ax.annotate('', xy=(child_coords[0], child_coords[1]), xytext=(parent_coords[0], parent_coords[1]),
                arrowprops=dict(arrowstyle="->", color='black', lw=1))

# Definindo limites e removendo eixos
ax.set_xlim(0, 4)
ax.set_ylim(0, 7)
ax.axis('off')

# Salvando o diagrama como imagem
plt.title("Diagrama UML do Sistema Bancário", fontsize=16)
plt.savefig('/mnt/data/diagrama_uml_sistema_bancario.png', format='png')
plt.show()

    """
    Melhorias Destacadas
Estrutura de Classes: Utilização de classes para representar conceitos de cliente, conta e transações, tornando o código mais organizado e modular.
Herança e Polimorfismo: Implementação de herança (ex. ContaCorrente estendendo Conta) e polimorfismo, facilitando a manutenção e extensibilidade do sistema.
Métodos Abstratos: Uso de métodos abstratos na classe Transacao para garantir que cada tipo de transação (saque e depósito) implemente suas regras específicas.
Encapsulamento: Propriedades e métodos privados (self._atributo) melhoram a segurança dos dados e restringem o acesso direto aos atributos.
Histórico de Transações: Implementação de um histórico para acompanhar todas as transações realizadas em uma conta, aumentando a transparência e o controle sobre as operações.
Verificação de Erros: Verificações robustas para garantir que operações como saques e depósitos sejam válidas e informem o usuário sobre erros.
Diagrama UML
Vou gerar a imagem do diagrama UML com base na estrutura do sistema bancário.

Estrutura do Diagrama UML
Classes:
Cliente (abstrata)
endereco
contas
Métodos: realizar_transacao, adicionar_conta
PessoaFisica (extende Cliente)
nome
data_nascimento
cpf
Conta (abstrata)
saldo
numero
agencia
cliente
historico
Métodos: sacar, depositar
ContaCorrente (extende Conta)
limite
limite_saques
Métodos: sacar
Historico
transacoes
Métodos: adicionar_transacao
Transacao (abstrata)
Métodos: valor, registrar
Saque (extende Transacao)
valor
Método: registrar
Deposito (extende Transacao)
valor
Método: registrar
Relacionamentos
Herança: Cliente -> PessoaFisica, Conta -> ContaCorrente, Transacao -> Saque/Deposito
Associação: Cliente possui Conta, Conta possui Historico.

Diagrama UML adicionando na pasta do desafio
    """
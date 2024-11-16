# Trilha Python DIO

### #238 Código desenvolvido com base nas aulas de Guilherme Arthur de Carvalho sobre fundamentos de Python. 

## **Desafio 01: Desenvolver um Sistema Bancário Simples em Python**
O desafio consiste em criar um sistema bancário simples com as seguintes funcionalidades:

### **Depósito:**

- Permitir depósitos de valores positivos.
- Armazenar todos os depósitos em uma variável e exibi-los no extrato.

### **Saque:**

- Permitir até 3 saques diários, com um limite máximo de R$ 500 por saque.
- Verificar se há saldo suficiente antes de permitir o saque.
- Informar ao usuário se não for possível sacar devido à falta de saldo.
- Armazenar todos os saques em uma variável e exibi-los no extrato.

### **Extrato:**

- Exibir um extrato com o histórico de todas as operações de depósito e saque.
- Mostrar o saldo atual no final da listagem no formato R$ xxx.xx.

O sistema deve trabalhar com apenas um usuário e deve garantir que o saldo nunca fique negativo. O menu interativo permite ao usuário escolher entre as operações de depósito, saque, visualização do extrato e sair do programa. 🚀🏦


## **Desafio 02: Inserir Data e Hora no Sistema Bancário Simples em Python**

- Estabelecer um limite de 10 transações diárias para uma conta
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.


## **Desafio 03: Criar Cliente e Vincular a Conta Corrente do Sistema Bancário**

### **Cliente:**

- Criar as funções para:
    - Criar cliente do banco armazenado em uma lista
    - Criar conta corrente
    - vincular a conta bancária ao cliente  

- Funções:
    - Saque: keywords only
    - Depósito: positional only
    - Extrato: positional only and keywords only  

- **Conta Corrente:**
    - O programa deve armazenar as contas em uma lista
    - Uma conta é composta por:
        - **Agência** (número fixo: 0001)
        - **Número da Conta** (número sequencial e inicia por 1)
        - **Cliente (usuário)** (pode ter mais de uma conta, mas uma conta prertence a somente um cliente)

- Dados cadastrais por cliente:
    - Nome
    - Data de Nascimento
    - CPF: único por cliente
    - Endereço: logradouro, nº - bairro - cidade/UF


**Dica**: 
Para vincular um usuário a uma conta, foltre a lista de usuários buscando o núero do CPF informado para cada usuários da lista.


## **Desafio 04: Remodelar o Sistema Bancário em POO**

### **Remodelar o Sistema:**


- Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML a seguir:

    * ![UML DESAFIO DIO](image.png)

* Classes:   
   

    * Saque
        * **_ valor: float**

            * Saque herda atributos e métodos da classe Transação   

    * Depósito
        * **_ valor: float**

            * Depósito herda atributos e métodos da classe Transação   
   
    * Transação << interface >> | Classe abstrata
        * **+ registrar(conta: Conta)**
      
    * Histórico
        * **+ adicionar_transacao(transacao: Transacao)**

            * Histórico pertence a uma conta 

    * Conta
        * **- saldo: float**
        * **- numero: int**
        * **- agencia: str**
        * **- cliente: Cliente**
        * **- historico: Historico**
        * **+ saldo(): float**
        * **+ nova_conta(cliente: Cliente, numero: int): Conta**
        * **+ sacar(valor: float): bool**

            * Conta tem um histórico
            * Conta está vinculada a um Cliente obrigatóriamente

    * Conta Corrente
        * **_ limite: float**
        * **_ limite_saques: int**

            * A classe Conta Corrente deriva da classe Conta**

    * Cliente
        * **_endereco: str**
        * **_ contas: list**
        * **+ realizar_transacao(conta: Conta, transacao: Transacao)**
        * **+ adicionar_conta(conta:Conta)**

            * Cliente poder ter várias Contas

    * Pessoa Física
        * **_ cpf: str**
        * **_ nome: str**
        * **_ data_nascimento: date**

            * Pessoa Física herda atributos e métodos da classe Cliente   
 

**Desafio Extra**: 
Após concluir a modelagem das classes e a criação dos métodos. Atualizar os métodos que tratam as oeperações do menu para funcionarem com as classes modelasdas.


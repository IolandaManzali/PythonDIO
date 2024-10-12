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

- Conta Corrente:
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


# Chatbot Bancário

Este projeto implementa um chatbot bancário simples utilizando sockets em Python. O chatbot permite ao usuário interagir com um servidor para consultar saldo, realizar transferências e obter informações sobre produtos bancários.

## Estrutura do Projeto

O projeto consiste em dois scripts principais:

1. **Servidor (`servidor_chatbot.py`)**: Responsável por simular um servidor bancário que processa comandos do usuário.
2. **Cliente (`cliente_chatbot.py`)**: Um cliente que se conecta ao servidor e envia comandos para interagir com o chatbot bancário.

## Funcionalidades do Chatbot

- **oi**: Saudação inicial.
- **saldo**: Consulta o saldo da conta (saldo inicial de R$ 1500,00).
- **transferir [valor]**: Realiza uma transferência de um valor especificado. Exemplo: `transferir 200.00`.
- **produtos**: Informa sobre os produtos bancários disponíveis (contas correntes, poupança, cartões de crédito, seguros).
- **tchau**: Encerra a conversa com o chatbot.

## Execução

### 1. Requisitos

- Python 3.x instalado em seu sistema.

### 2. Executando o Servidor

Primeiro, inicie o servidor que simula o banco:

```
python servidor_chatbot.py
```

Em outro terminal, execute o cliente para começar a interagir com o chatbot bancário:

```
python cliente_chatbot.py
```

Digite os comandos no terminal para interagir com o servidor. A conversa continua até que o usuário digite tchau.


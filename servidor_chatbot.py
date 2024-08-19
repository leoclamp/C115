from socket import *

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O chatbot bancário está pronto para receber mensagens')

# Simulando dados bancários
saldo_conta = 1500.00

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Conectado a {addr}')

    while True:
        # Recebe a mensagem do cliente
        mensagem = connectionSocket.recv(1024).decode()

        if not mensagem:
            print('Conexão encerrada pelo cliente')
            break

        print(f'Cliente: {mensagem}')

        # Processa a mensagem e responde com base em comandos bancários
        if mensagem.lower() == 'oi':
            resposta = "Olá! Bem-vindo ao Banco. Como posso ajudar você hoje?"
        elif mensagem.lower() == 'saldo':
            resposta = f"Seu saldo atual é R$ {saldo_conta:.2f}."
        elif mensagem.lower().startswith('transferir'):
            try:
                _, valor_str = mensagem.split()
                valor = float(valor_str)
                if valor > saldo_conta:
                    resposta = "Saldo insuficiente para realizar a transferência."
                else:
                    saldo_conta -= valor
                    resposta = f"Transferência de R$ {valor:.2f} realizada com sucesso! Seu novo saldo é R$ {saldo_conta:.2f}."
            except ValueError:
                resposta = "Por favor, insira o valor correto para a transferência. Exemplo: 'transferir 200.00'"
        elif mensagem.lower() == 'produtos':
            resposta = "Oferecemos contas correntes, poupança, cartões de crédito e seguros."
        elif mensagem.lower() == 'tchau':
            resposta = "Obrigado por utilizar nossos serviços! Até logo!"
            connectionSocket.send(resposta.encode())
            break
        else:
            resposta = "Desculpe, não entendi. Você pode perguntar sobre saldo, transferir valores, ou nossos produtos."

        # Envia a resposta para o cliente
        connectionSocket.send(resposta.encode())

    connectionSocket.close()

    
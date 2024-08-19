from socket import *

serverName = 'localhost'
serverPort = 3000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Bem-vindo ao Banco Chatbot!")
print("Comandos disponíveis: 'oi', 'saldo', 'transferir [valor]', 'produtos', 'tchau'.")

while True:
    # Lê a mensagem do usuário
    mensagem = input("Você: ")

    # Envia a mensagem para o servidor (chatbot)
    clientSocket.send(mensagem.encode())

    # Recebe a resposta do servidor
    resposta = clientSocket.recv(1024).decode()

    print('Chatbot Bancário:', resposta)

    if mensagem.lower() == 'tchau':
        break

clientSocket.close()


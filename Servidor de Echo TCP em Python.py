

import socket                                                 #Importa biblioteca para aplicacoes em rede
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria socket TCP/IP (SOCK_STREAM)
end_servidor = ('localhost', 10000)
serv_sock.bind(end_servidor)                                  #Metodo que liga endereco/porta ao socket
serv_sock.listen(10)                                          #Define o limite de conexoes

try:
         print("Aguardando conexao!")
         conexao, end_cliente = serv_sock.accept()            #tupla que contem numero da conexao e endereco IP do Cliente
         print("Conectado a: " + str(end_cliente))            #Mostra endereco e porta do cliente conectado
         recebe = ""                                          #Inicializando variaveis
         while(recebe != "bye"):                              #Loop enquanto converte diferente de "bye"
            print("Aguardando mensagem!\n")
            recebe = conexao.recv(1024)                       #Recebe mensagem pela conexao
            print("Mensagem recebida: " + recebe)             #Exibe na tela
            print("Enviando mensagem de volta!\n")
            conexao.send(recebe)                              #Envia para o cliente

finally:

    print("Finalizando Conexao!!")
    conexao.close()                                           #Fecha conexao caso mensagem = bye



import socket                                                     # Biblioteca para aplicacao em rede
cliente_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria um socket TCP/IP (SOCK_STREAM)
end_servidor = ('localhost', 10000)                               # end_servidor recebe endereco e porta do servidor
cliente_sock.connect(end_servidor)                                # socket conecta ao endereco especificado em end_servidor
msg = ""                                                          # Inicializa variaveis
retorno = ""

try:
    while (msg != "bye"):                                       #Enquanto mensagem for diferente de bye
        print("Digite uma mensagem: ")                          #Captura mensagem digitada
        mensagem=raw_input()
        cliente_sock.send(mensagem)                             #Envia mensagem pelo socket codificada em bytes
        print("Mensagem enviada!")
        msg= cliente_sock.recv(1024)                            #Recebe mensagem de volta do servidor
        print("Mensagem recebida de volta: " + msg+ "\n")       #Decodifica mensagem e imprime

finally:

    #Fecha conexao caso mensagem = bye
    print("Finalizando Conexao!!")
    cliente_sock.close();

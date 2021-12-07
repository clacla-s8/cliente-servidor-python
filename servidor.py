import socket # importação do modulo socket
# o socket usa a combinação de um ip com o numero da porta
HOST = 'localhost' # ip ou nome da máquina, caso aqui ip da maquina local
PORT = 40000 # numero da porta
# invocando o medodo socket passando os parametros (FAMILIA DO PROTOCOLO, TIPO DO PROTOCOLO)
# A familia do protocolo usado é ipv4, protoco TCP, portanto STREAM
#objeto 's' criado.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT)) #vinculando o host e a porta
s.listen(1) # colocando em modo de escuta
#conn e addr são o retorno de s.accept(), que é o metodo que aceita a conexão
conn, addr = s.accept() # conn = conexão e  addr = endereço
print('host: ' , HOST , 'nome da máquina, caso aqui nome da maquina local', '\n'
      'porta: ' , PORT , 'numero da porta', '\n'
      'socket: ' , s ,'medodo socket passando os parametros (FAMILIA DO PROTOCOLO, TIPO DO PROTOCOLO)', '\n' ,
'A familia do protocolo usado é ipv4, protoco TCP, portanto STREAM', '\n'
      )

arq = open('SuperLeitura.txt', 'wb') # abrindo o arquivo para escrever a mensagem vinda do lado cliente

#laço para ler e rescrever os dados
while 1:
    dados = conn.recv(8) #chamando metodo receive do socket passando por parametro o tamanho dos dados que serão recebidos e armazenados na variavel dados
    if not dados: # se não tiver mais dados termina.
        break
        print(dados) #imprime os dados no console
    arq.write(dados) # escreve os dados no arquivo SuperLeitura.txt

arq.close() #fecha o arquivo
conn.close() #encerra conexão



























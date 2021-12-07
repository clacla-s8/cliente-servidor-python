import socket # importação do modulo socket
# o socket usa a combinação de um ip com o numero da porta
HOST = 'localhost' # ip ou nome da máquina, caso aqui nome da maquina local
PORT = 40000 # numero da porta
# invocando o medodo socket passando os parametros (FAMILIA DO PROTOCOLO, TIPO DO PROTOCOLO)
# A familia do protocolo usado é ipv4, protoco TCP, portanto STREAM
#objeto 's' criado.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT)) # conectar no socket do servidor, ambos no mesmo host e na mesma porta
arq = open('leiturinha.txt', 'r') #abrindo arquivo em modo leitura para q o servidor possa ler

for i in arq.readlines():
    print(i, '\n')
    s.send(i.encode()) #enviando para o servidor em forma de string

arq.close()
s.close()

from socket import *
# it can be any server port just make sure your giving the same value in TCP_client
serverPort=12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('the server is ready to listen')
while True:
               connectionSocket,addr=serverSocket.accept()
               sentence=connectionSocket.recv(1024)
               capitalizedSentence=sentence.upper()
               connectionSocket.send(capitalizedSentence)
               connectionSocket.close()
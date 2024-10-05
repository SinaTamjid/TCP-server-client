from socket import *
#local server name
serverName='127.0.0.1'
# it can be any server port just make sure your giving the same value in TCP_server
serverport=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverport))
#get the massage you trying to pass to the server
sentence=str(input('input lowercase sentence: '))
clientSocket.send(sentence.encode())
modifiedSentence=clientSocket.recv(1024)
#making sure that the massage send and printing  it
print ('From Server:',modifiedSentence)
#we make sure that after sending massage we close the socket
clientSocket.close()
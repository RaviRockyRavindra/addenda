# @author me
# @created at 15-05-2021 7:22 am
# @python venv / base
# @purpose addenda server

# imports
import socket
import _thread
import sys
import threading

#global Variables
available_connections=[]

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('192.168.0.106', 12000)
try:
        serverSocket.bind(server_address)
        serverSocket.listen()
        print("..server started & listening..")
        print("hostname",socket.gethostname())
        print("Server listening on",serverSocket)
except socket.error as errors:
        print("error while connecting ..",errors)

def client_connection(clientSocket, client_address):
    available_connections.append(clientSocket)
    print(available_connections)
    greeting_message = "welcome to the addenda"
    clientSocket.send(greeting_message.encode())
 

while True:
    connection, client_addr = serverSocket.accept()
    _thread.start_new_thread(client_connection,(connection,client_addr))






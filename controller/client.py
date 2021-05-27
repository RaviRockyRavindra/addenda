# @author me
# @created at 15-05-2021 7:22 am
# @python venv / base
# @purpose addenda client

#imports
import random
import socket
import sys
import threading
from tkinter import *
import tkinter as tk
sys.path.append(".")
sys.path.append("Y:\projects\Addenda-game\View")
# from CardsFit import Card

# from CardsFit import Deck


# @global variables
serverMessageGlobal = "null"
image_dir="Y:\\projects\\Addenda-game\\res\\images\\"
# list_of_filenames= os.listdir(image_dir)


widgets_list=[]
userName__inputsubmit = " " 
playername1= " "
playername2= " "


# @client_server_configuration
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_addr = ('192.168.0.106',random.randrange(13000,14000))
server_address = ('192.168.0.106',12000)
serverSocket.bind(client_socket_addr)
serverSocket.connect(server_address)
print("------server connected-----")


def pullMessage():
        server_message = serverSocket.recv(100000).decode()
        ## must declare for global values
        global serverMessageGlobal
        serverMessageGlobal = server_message
        print("inside func pullmessage",serverMessageGlobal)


def send_message(messageString):
    while True:
        message_to_server = serverSocket.send(messageString)        

pullMessage()
player1= input("player1 name")
player2= input("player2 name")
if player1 and player2:
    import ui
    ui.username__command(player1,player2)
# ui.gui_mode()


while True:
    threading.Thread(target=pullMessage).start()
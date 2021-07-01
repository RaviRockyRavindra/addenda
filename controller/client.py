# @author me
# @created at 15-05-2021 7:22 am
# @python venv / base
# @purpose addenda client
#imports

import pickle
import random
import socket
import sys
import threading
import _thread
import time
from tkinter import *
import tkinter as tk
sys.path.append(".")
sys.path.append("..\\View")
sys.path.append("Y:\projects\Addenda-game\model")
import ui as uii
from UserSession import UserSession
from GameSession import GameSession
# @global variables
serverMessageGlobal = "null"
image_dir="..\\res\\images\\"
widgets_list=[]
userName__inputsubmit = " " 
playername1= " "
playername2= " "
pplist =[]
randport = 0
serverSocket = None


if __name__=="__main__":
    randport = random.randrange(13000,14000)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_addr = ('192.168.0.106',randport)
    server_address = ('192.168.0.106',12000)
    serverSocket.bind(client_socket_addr)
    print("socket binding ---",serverSocket) 
    print("main socket--",serverSocket)

def main():
    global serverSocket
    # @client_server_configuration
    print("------server connected-----")
    serverSocket.connect(server_address)
    print("client socket",client_socket_addr)
    print("serverSockert",serverSocket)
        
def getActiveConnections(socket):
    serverSocket = socket
    active_sessions_list = []
    serverSocket.send("listOfActiveConnections".encode())
    
    print("in getACtiveConnect---fetching sessions")
    time.sleep(5)
    while True:
        server_message = serverSocket.recv(100000)
        # server_message = server_message.strip('][').split(', ')
        server_message = pickle.loads(server_message)
        print(server_message)
        if server_message:
            print("active sessions list",server_message)
            for one in server_message:
                print(one)
                active_sessions_list.append(one)
            return active_sessions_list
        return active_sessions_list    
        
def joinToTeam(socket,sessionId,name):
    serverSocket = socket
    populateString = " joinTeam /" + str(sessionId)+ "/" + name
    serverSocket.send(populateString.encode())
    print("updating the server")
    time.sleep(3)
    statusofGame = serverSocket.recv(100000).decode()
    print("status of Game",statusofGame)
    return statusofGame

def getWinnerUpdate(socket,sessionId):
    global serverSocket
    serverSocket = socket
    populateString = "getWinnerUpdate/" + str(sessionId)
    serverSocket.send(populateString.encode())
    winnervalue = serverSocket.recv(10000).decode()
    print("return value of get winner status")
    return winnervalue

def updateDeckCardValue(socket,sessionId,name,value,identity):
    serverSocket = socket
    populateString = " updateDeckCardvalue /" + str(sessionId) + "/" + name + "/" + str(value) + "/" + identity
    if identity == "player2":
       print(identity, populateString)
    else:
        print(identity, populateString)
    serverSocket.send(populateString.encode())

def send_message(socket,messageString):
    serverSocket = socket
    while True:
        message_to_server = serverSocket.send(messageString)      

def sessionCreated(socket,sessionNumber,name):
    serverSocket = socket
    print(serverSocket)
    populateString = "sessionCreated /" + str(sessionNumber) + "/" + name
    serverSocket.send(populateString.encode())

def distributeCards(socket,sessionId,identity):
    serverSocket = socket
    print("distribute start from client ----",sessionId,identity)
    dataa = "distributeCards/" + str(sessionId) + "/" + str(identity)
    dataa = dataa.encode()
    print(dataa)
    serverSocket.send(dataa)

def performActionOncards(globalGamePlayerSocket):
    serverSocket = globalGamePlayerSocket
    serverSocket.send("performActionCards")    

def player_opnion(username):
    serverSocket.send(username)

def cardHit(socket,playerIdentity,score,session,cardLabel):
    populateString = "cardhit/"+ str(playerIdentity) +"/"+ str(score) +"/"+ str(session) + "/" + str(cardLabel)
    print("cardHit pre data",populateString)
    socket.send(populateString.encode())    


def pullMessage(serverSocket):
    serverSocket = serverSocket
    global pplist
    print("pullmessage")
    while True:
        try:
            message = serverSocket.recv(100000).decode()
            print("------------------",message)
            if message.find("distributeCards") != -1:
                print("inside the pull message distribued cards",message)
                uii.serveCards()
            
            if message.find("messageOUT") != -1:
                print(message)
                message = message.split("/")
                uii.popudisplay()

            if message.find("gamesessionrefresh") != -1:
                pplist.clear()
                print("inside pull message gameUpdateObject")
                # dataToSendSockets = "GameSession /" + str(obj.getSession()) + "/" + str(obj.getyPlayer1move()) + "/" + str(obj.getyPlayer2move()) + "/" + str(obj.getyPlayer1score()) + "/" + str(obj.getyPlayer2score()) + "/" + obj.getGameScore + "/" + obj.getUserTurn()
                obj = message.split("/")
                print(obj)
                player1Card = obj[1]
                player2card = obj[2]
                player12card= obj[3]
                player22card = obj[4]
                score1=obj[5]
                score2=obj[6]
                winner=obj[7]

                pplist.append(player1Card)
                pplist.append(player2card)
                pplist.append(player12card)
                pplist.append(player22card)
                pplist.append(score1)
                pplist.append(score2)
                pplist.append(winner)
                uii.setMycards(pplist)

        except Exception as e:
            print("strucked with an run time error",e)   
            break

def sendMessage(socket,session,value,idenity):
    socket = socket
    prepareMessag= "messagein/"+ str(session) + "/" + value + "/" + idenity 
    socket.send(prepareMessag.encode())


def callPullThread(socket):
    socket = socket
    print("running the thread..",socket)
    threading.Thread(target=pullMessage,args=(socket,)).start()         

if __name__ == "__main__":
    main()
    uii.intialWindow(serverSocket) 


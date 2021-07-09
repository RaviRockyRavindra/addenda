# @author me
# @created at 15-05-2021 7:22 am
# @python venv / base
# @purpose addenda server

# imports
from os import name
import socket
import ast
import _thread
import pickle
import sys
import threading
from tkinter.constants import NO
sys.path.append("Z:\projects\Addenda-game\model")
sys.path.append(".")
from UserSession import UserSession
from GameSession import GameSession as gameSession
import DataBaseClass
#global Variables
available_connections=[]
connections_info={}
sessions=[]
listofsessionsIDS=[]
listofGameSession=[]
Gloablplayer1Score=[]
Globalplayer2score=[]

list_of_players={}
player1socket = None
player1Turn=True
player2Turn=True 
scoreupdated1 = 0
scoreupdated2 = 0
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
    global player1Turn,player2Turn
    global scoreupdated1,scoreupdated2
    available_connections.append(clientSocket)
    print(available_connections)
    while True:
            clientMessage = clientSocket.recv(10000).decode()
            if clientMessage.find("sessionCreated") !=-1:
                    sessionMessage = clientMessage.split("/") 
                    status = "partialActive"
                    listofsessionsIDS.append(sessionMessage[1])
                    user = UserSession(sessionMessage[2],"null",sessionMessage[1],clientSocket,None,status,0,0,"null")
                    sessions.append(user)

            elif clientMessage.find("listOfActiveConnections") !=-1:
                    print("inside server listofconnections")
                #     populateString = "listOfActiveConnections " + str(sessions)
                #     print(populateString)
                    data =pickle.dumps(listofsessionsIDS)
                    clientSocket.send(data)

            elif clientMessage.find("joinTeam") !=-1:
                    clientMessage = clientMessage.split("/")
                    player2session = clientMessage[1]
                    player2name = clientMessage[2]
                    for one in sessions:
                            if (one.getSession() == player2session):
                                    one.setStatus("Active")
                                    one.setPlayer2Name(player2name)
                                    print("setting socket 2 ",clientSocket)
                                    one.setPlayer2Socket(clientSocket)
                    populateString = "Activated"                
                    clientSocket.send(populateString.encode())

            elif clientMessage.find("updateDeckCardvalue") != -1:
                    clientMessage = clientMessage.split("/")
                    id = clientMessage[1]
                    name = clientMessage[2]
                    value = clientMessage[3]
                    finalValue = int(value)
                    identity = clientMessage[4]
                    for one in sessions:
                            if (one.getSession() == id and identity == "player1"):
                                    one.setDeckScore1(finalValue)
                                    print("deckscore1",one.getDeckScore1())
                            elif (one.getSession() == id and identity == "player2"):
                                    one.setDeckScore2(finalValue)       
                                    print("deckscore2",one.getDeckScore2())

            elif clientMessage.find("getWinnerUpdate") != -1:
                    clientMessage = clientMessage.split("/")
                    id = clientMessage[1]
                    for one in sessions:
                            if (one.getSession() == id):
                                    if int(one.getDeckScore1()) == 0 or int(one.getDeckScore2()) == 0:
                                            one.setWinner("loading")
                                        #     print(one.getDeckScore1(),"deckscore1")
                                        #     print(one.getDeckScore2(),"deckscore2")
                                            print("in loading status ")
                                    elif int(one.getDeckScore1()) == int(one.getDeckScore2()):
                                            one.setWinner("retake")
                                        #     print(one.getDeckScore1(),"deckscore1")
                                        #     print("in 1 == 2 status ") 
                                            clientSocket.send(one.getWinner().encode())
                                    elif int(one.getDeckScore1()) > int(one.getDeckScore2()):
                                            one.setWinner("player1")
                                        #     print("in 1 > 2 status ")
                                            print(one.getWinner())
                                            clientSocket.send(one.getWinner().encode())
                                    elif int(one.getDeckScore2()) > int(one.getDeckScore1()):
                                            one.setWinner("player2")
                                            print(one.getWinner())
                                        #     print("in 2 > 1 status ")
                                            clientSocket.send(one.getWinner().encode())

            elif clientMessage.find("distributeCards") != -1:
                     print("clientMessage",clientMessage)
                     clientMessage = clientMessage.split("/")
                     sessionId = clientMessage[1]
                     identity = clientMessage[2]
                     print("distribute",sessionId,identity)
                     for each in sessions:
                             print(each.getSession())
                             print(type(each.getSession()))
                             print(type(sessionId))
                             if each.getSession() == sessionId and identity == "player1":
                                     player2socket = each.getPlayer2Socket() 
                                     print("sending to player 2 socket",player2socket)
                                     targetData = "distributeCards"
                                     player2socket.send(targetData.encode())
                             elif each.getSession() == sessionId and identity == "player2":
                                     player1socket = each.getPlayer1Socket()
                                     print("sending to player 1 socket",player1socket)
                                     targetData = "distributeCards"
                                     player1socket.send(targetData.encode())  

            elif clientMessage.find("messagein") != -1:
                    t_socket=None
                    clientMessage = clientMessage.split("/")
                    session_II = clientMessage[1]
                    value_H = clientMessage[2]
                    identity_H = clientMessage[3]

                    for one in sessions:
                            print(sessions)
                            if (one.getSession() == session_II and identity_H == "player1"):
                                    t_socket = one.getPlayer2Socket()
                                    print("in message socket ",t_socket)
                                    v = "messageOUT /"+value_H
                                    t_socket.send(v.encode())

                            elif (one.getSession() == session_II and identity_H == "player2"):
                                    t_socket = one.getPlayer1Socket()
                                    print("in message socket ", one.getPlayer2Socket())
                                    v = "messageOUT /"+value_H
                                    t_socket.send(v.encode())




            elif clientMessage.find("cardhit") != -1:
                     dataToSendSockets = "null"
                     print("in cardhit")
                     h_clientMessage = clientMessage.split("/")
                     h_sessionId = h_clientMessage[3]
                     cardLabel = h_clientMessage[4]
                     g_score = h_clientMessage[2]
                     h_identity = h_clientMessage[1]

                     if h_identity == "player1":
                        Status = DataBaseClass.session_exist(h_sessionId)
                        if Status:
                                print(player1Turn)
                                if player1Turn:
                                        # non dealer card1
                                        exe=DataBaseClass.update1Session(cardLabel,h_sessionId) 
                                        player1Turn = False
                                        dataSocket=DataBaseClass.getRecords(h_sessionId)
                                        scoreupdated1 = DataBaseClass.getPlayer1Score(h_sessionId)

                                else:
                                        # 11 22
                                        
                                        exe=DataBaseClass.updateSessionplayer1(h_sessionId,cardLabel)
                                        dataSocket=DataBaseClass.getRecords(h_sessionId)
                                        scoreupdated1 = DataBaseClass.getPlayer1Score(h_sessionId)
                                
                        else:
                                exe=DataBaseClass.createSession(h_sessionId,cardLabel,"null",int(g_score),0,int(g_score))        
                                player1Turn=False
                                dataSocket=DataBaseClass.getRecords(h_sessionId)
                                scoreupdated1 = DataBaseClass.getPlayer1Score(h_sessionId)
                                                              
                     elif h_identity == "player2":
                        Status = DataBaseClass.session_exist(h_sessionId)
                        if Status:
                                print(player2Turn)
                                if player2Turn:
                                        # non dealer card2
                                        exe=DataBaseClass.update1Session2(h_sessionId,cardLabel)
                                        player2Turn = False
                                        dataSocket=DataBaseClass.getRecords(h_sessionId)
                                        scoreupdated2 = DataBaseClass.getPlayer2Score(h_sessionId)
                                        
                                else:
                                       
                                       exe=DataBaseClass.updateSessionplayer2(h_sessionId,cardLabel)    
                                       dataSocket=DataBaseClass.getRecords(h_sessionId)
                                       scoreupdated2 = DataBaseClass.getPlayer2Score(h_sessionId)
                        else:
                                exe=DataBaseClass.createSession(h_sessionId,"null",cardLabel,0,int(g_score),int(g_score))   
                                player2Turn=False
                                dataSocket=DataBaseClass.getRecords(h_sessionId)
                                scoreupdated2 = DataBaseClass.getPlayer2Score(h_sessionId)

                     targetSocket = None
                     winnerstatus=DataBaseClass.getWinner(h_sessionId)
                     if exe:
                             
                             datastring = "gamesessionrefresh/"+str(dataSocket[2])+"/"+str(dataSocket[3])+"/"+str(dataSocket[6]) + "/"+str(dataSocket[7]) + "/" + str(scoreupdated1) + "/" + str(scoreupdated2) + "/" + str(winnerstatus) + "/" + str(dataSocket[8]) + "/" + str(dataSocket[9])
                             print(datastring)
                             for getses in sessions:
                                     print("sessions",getses)
                                     if int(h_sessionId) == int(getses.getSession()):
                                             targetSocket = getses.getPlayer1Socket()
                                             targetSocket2 = getses.getPlayer2Socket()
                             targetSocket.send(datastring.encode())
                             targetSocket2.send(datastring.encode())
                     else:
                             print("not updated or created")       
                     
                
while True:
    connection, client_addr = serverSocket.accept()
    _thread.start_new_thread(client_connection,(connection,client_addr))


import random
import socket
import sys
from time import time, sleep
import PIL
import PIL.ImageTk
# from PIL import Image
import PIL.Image

import threading
from tkinter import *
import tkinter as tk
import os
count = 0
sys.path.append("Z:\projects\Addenda-game\controller")

import client
from CardsFit import Card
from CardsFit import Deck


## global var
serverMessageGlobal = "null"
widgets_list=[]
globalGamePlayerSocket = None
windowTk = tk.Tk()
intialWindiowTk = tk.Tk()
# communicationWindow = tk.Tk()
# chatWindowtk=tk.Tk()
congowidget = tk.Label(windowTk)
infosubmitButton = tk.Button(intialWindiowTk,text ="Submit button")
choices = { 'Create','Join'}
textWidgetName = tk.Label(intialWindiowTk,text="enter player name")
activeConnections = []
globalUserName = " "
GlobalGameDealer= False
cardDealerButton = tk.Button(windowTk,text="Distribute")

globalSessionId = 0
globalIdentityGame = " "
tkvar = StringVar()
myCardsDisplayGrid = tk.Label()
oppsitionCardsDisplayGrid = tk.Label()
# cardsDistributeGridLabel = tk.Button()
tkvar.set('Create')
popupMenu = OptionMenu(intialWindiowTk, tkvar, *choices)
inputNamePlayer1 = tk.Entry(intialWindiowTk)
messageinput = tk.Entry(windowTk)
messagedisplay = tk.Label(windowTk,text="Incoming message display here")

messageSubmit= tk.Button(windowTk,text="SubmitMessage")

# inputMessage = tk.Entry(chatWindowtk)
# sendMessage = tk.Label(chatWindowtk)
# sendButton = tk.Button(chatWindowtk,text="send")


# frame1 = Frame(windowTk,bg="#000000",width=1000,height=500)
# frame2 = Frame(windowTk,bg="#ffffff",width=1000,height=500)
# frame2 = Frame(windowTk, borderwidth=2, pady=5)
shuffleButton = tk.Button(text ="Shuffle Cards")

cutCardsButton = tk.Button(text ="Cut Cards")
image = PIL.Image.open("Z:\projects\Addenda-game\Card Back 4.png")
photo = PIL.ImageTk.PhotoImage(image)
allCardsLabel = tk.Label()
cutCardsLabel = tk.Label()
userName__inputsubmit = " " 
playername1= "player1"
playername2= "player2"
image_dir="Z:\\projects\\Addenda-game\\res\\images\\"

addendaLabel = tk.Label(text=serverMessageGlobal)
# 
# playerNameLabel1 = tk.Label(text=playername1)
# playerNameLabel2 = tk.Label(text=playername2)
list_of_cards_grid=[]
list_of_cards_grid_cut = []
player1score__ = 0
player2score__ = 0
playerScore1 = tk.Label(windowTk,text=player1score__)
statusWaiting = tk.Label(windowTk,text="loading")
playerScore2 = tk.Label(windowTk,text=player2score__)
# frame1.grid(row=2, column=1)
# frame2.grid(row=2, column=1)
windowTk.config(bg='green')
windowTk.title("cards windows addenda")
intialWindiowTk.config(bg='green')
intialWindiowTk.title("info window addenda")
# communicationWindow.config(bg='green')
# communicationWindow.title("communication window addenda")
# chatWindowtk.config(bg='green')
# chatWindowtk.title("communication")




# def getAllCards_open():
#     # Deck().display()
#     ## display cards in grid
#     # listCards = shuffle_cards()
#     # print(listCards)
#     shuffleList = shuffle_cards()
#     row = 1
#     pos = 0
#     col = -1
#     for eachcard in shuffleList:
#         pos = pos + 1
#         col = col + 1
#         eachcard = str(eachcard)
#         image_path = image_dir + eachcard + ".png"
#         image = PIL.Image.open(image_path)
#         photo = PIL.ImageTk.PhotoImage(image)
#         label = Label(image = photo)
#         label.image = photo
#         if(pos >= 1 and pos <= 10):
#             label.grid(row=row,column=col)
#         elif(pos > 10 and pos <= 20):                               
#             if pos==11:
#                 col = 0
#                 row = 2 
#             label.grid(row=row,column=col)
#         elif(pos > 20 and pos <= 30):
#             if pos == 21:
#                 col = 0
#                 row = 3
#             label.grid(row=row,column=col)
#         elif(pos > 30 and pos <= 40):
#             if pos == 31:
#                 col = 0
#                 row = 4
#             label.grid(row=row,column=col)
#         elif(pos > 40 and pos <= 52):
#             if pos == 41:
#                 col = 0
#                 row = 5
#             label.grid(row=row,column=col)


def getAllCards_close():
    # Deck().display()
    ## display cards in grid
    # listCards = shuffle_cards()
    # print(listCards)
    
    global allCardsLabel, list_of_cards_grid
    shuffleList = shuffle_cards()
    row = 1
    pos = 0
    col = -1
    for eachcard in range(len(shuffleList)):
        pos = pos + 1
        col = col + 1
        singleEachcard = "Card Back 4"
        image_path = image_dir + singleEachcard + ".png"
        image = PIL.Image.open(image_path)
        photo = PIL.ImageTk.PhotoImage(image)
        allCardsLabel = Label(image = photo)
        allCardsLabel.image = photo
        if(pos >= 1 and pos <= 10):
            allCardsLabel.grid(row=row,column=col)
            list_of_cards_grid.append(allCardsLabel)
        elif(pos > 10 and pos <= 20):                               
            if pos==11:
                col = 0
                row = 2 
            allCardsLabel.grid(row=row,column=col)
            list_of_cards_grid.append(allCardsLabel)
        elif(pos > 20 and pos <= 30):
            if pos == 21:
                col = 0
                row = 3
            allCardsLabel.grid(row=row,column=col)
            list_of_cards_grid.append(allCardsLabel)
        elif(pos > 30 and pos <= 40):
            if pos == 31:
                col = 0
                row = 4
            allCardsLabel.grid(row=row,column=col)
            list_of_cards_grid.append(allCardsLabel)
        elif(pos > 40 and pos <= 52):
            if pos == 41:
                col = 0
                row = 5
            allCardsLabel.grid(row=row,column=col)
            list_of_cards_grid.append(allCardsLabel)
          
    
        # print(allCardsLabel.grid_info())

def shuffle_cards():
    shuffle_cards = Deck().shuffle_cards()
    return shuffle_cards

# def gui_mode():
    # print("inside func gui_mode",serverMessageGlobal)
    ## setting window size and backgroud color
    # windowTk.geometry("400x200") 

    # windowTk.config(bg='green')

    ## end of setting window size and backgroud color
    
    ## heading Label     
    # addendaLabel.pack()
    # addendaLabel.place(relx=0.5,rely=0.01,anchor=CENTER)
    ## heading Label close

    # ## text widget name    
    # 
    # ##end.. label widget close


    # ## entry to take the input from user    
    #
    # ## end.. entry to take the input from user

    ## button widget name submit
    # submitButton.pack()
    # submitButton.place(rely = 0.6, relx = 0.5, anchor = CENTER)
    ## end button widget name submit

    

def hide_widgets(widgets_list):
    for eachWidget in widgets_list:
        eachWidget.destroy()
        

def display_widgets(widgets_list):
    for eachWidget in widgets_list:
        eachWidget.pack()    

def windowTkinterRefresh():
    windowTk.update()
    windowTk.after(1000,windowTkinterRefresh)

def intialwindowTkinterRefresh():
    intialWindiowTk.update()
    intialWindiowTk.after(1500,intialwindowTkinterRefresh)   

# def communicationwindowTkinterrefresh():
#     communicationWindow.update()
#     communicationWindow.after(1500,communicationwindowTkinterrefresh)  

def sendMessageToTarget():
    val=messageinput.get()
    print(val,"--message inside send message function")
    client.sendMessage(globalGamePlayerSocket,globalSessionId,val,globalIdentityGame)
              

def username__command(sessionId):
    global userName__inputsubmit, playername1, playername2
    global sendButton, sendMessage, inputMessage

    # widgets_list.append(addendaLabel)
    # widgets_list.append(textWidgetName)
    # widgets_list.append(inputNamePlayer1)
    # widgets_list.append(inputNamePlayer2)
    # shuffleButton.pack()

    windowTk.title(str(sessionId))
       ## player lables are setting up here 
    # playerNameLabel1.config(text=" player1")
    

    # playerNameLabel1.grid(row=0,column=3)


    # playerNameLabel1.place(rely= 0.5, relx= 0.5, anchor=CENTER)   
    # playerNameLabel2.place(rely= 0.5, relx= 0.5, anchor=CENTER)
 

    # playerNameLabel1.grid(row=0,column=1)
    # playerNameLabel2.grid(row=1,column=2)

    # playerScore1.config(text=" Score 1: "+str(player1score__))
    # playerScore1.grid(row=0,column=7)

    # playerScore2.config(text=" Score 2: "+str(player2score__))
    # playerScore2.grid(row=0,column=8)

    # hide_widgets(widgets_list)    
    

    # submitButton.config(command=username__command)

    shuffleButton.config(command=shuffle_button_clicked)
    shuffleButton.grid(row=0,column=0)

    cutCardsButton.config(command=cut_button_clicked)
    cutCardsButton.grid(row=0,column=1)

    messagedisplay.grid(row=11,column=1)
    messageinput.grid(row=10,column=1)
    print("here message submit defines -------------------")
    messageSubmit.config(command=sendMessageToTarget)
    messageSubmit.grid(row=10,column=2)

    windowTkinterRefresh()
    # communicationwindowTkinterrefresh()
    # communicationWindow.mainloop()
    windowTk.mainloop()
    

def shuffle_button_clicked():
    if cutCardsLabel:
        print("existed before")
        remove_cards_grid_cut()
    getAllCards_close()

def remove_cards_grid():
    for one in list_of_cards_grid:
        one.grid_forget()

listServeCards= []


def serveCards():
    global statusWaiting
    global cutCardsLabel,cardDealerButton
    print(globalGamePlayerSocket)
    statusWaiting.config(text="playing")
    print(GlobalGameDealer,"Global value === also identity is ",globalIdentityGame)
    # when a winner hit the serve cards will make a reques t to player2 socket
    if GlobalGameDealer:
        print("cards served--------------from winnerr")
        client.distributeCards(globalGamePlayerSocket,globalSessionId,globalIdentityGame)
  
    if cutCardsLabel:
        for one in list_of_cards_grid_cut:
            one.grid_forget()
        print("removed cards",list_of_cards_grid_cut)

    sleep(5)    
    
    randomNumber2 = shuffle_cards()
    row = 0
    col = 0
    pos = 0
    print("randomNumber2 cards",randomNumber2)
    for each in randomNumber2[:12]:
        pos = pos + 1
        col = col + 1
        image_path = image_dir + str(each) + ".png"
        print("position",pos,str(each))
            # locallist.append(str(each))
        image = PIL.Image.open(image_path)
        photo = PIL.ImageTk.PhotoImage(image)
            # cardsDistributeGridLabel = tk.Label(image = photo)
            # # cardsDistributeGridLabel.image=photo
            # cardsDistributeGridLabel.image = photo
        cardButton = tk.Button(windowTk,image=photo)
        cardButton.image = photo
        cardButton.config(command=lambda name=str(each):cardClicked(globalIdentityGame,globalSessionId,name))
            # cardsDistributeGridLabel.config()
            # cardValue = pos
        if pos >= 1 and pos < 10:
            row = 1
            cardButton.grid(row=row,column=col)
            listServeCards.append(cardButton)
        elif pos >= 10 and pos < 13:
            if pos == 10:
                row = 2 
                col = 0
                cardButton.grid(row=row,column=col)
                listServeCards.append(cardButton)
        

def setMycards(data):
    myCardsList = []
    global congowidget
    oppCardsList = []
    congostatus = "Load"
    exceedwinner=data[8]
    if data[6] =="player1" or data[6] == "player2":
        congostatus = "lost the game"
        
 
    print("data",data)
    if globalIdentityGame == "player1":
        print("on screen 1 data received")
        myCardsList.append(data[0])
        myCardsList.append(data[2])
        oppCardsList.append(data[1])
        oppCardsList.append(data[3])
        scorewidget = tk.Label(windowTk,text="Score 1: "+data[4])
        scorewidget.grid(row=0,column=4)

        gameScorewidget = tk.Label(windowTk,text="GameScore: "+data[7])
        gameScorewidget.grid(row=0,column=6)
        
        if data[6] == "player1":
            congostatus = "Congrats"

        if exceedwinner == "player1":
            congostatus = "you lost the game"

        elif exceedwinner == "player1":
            congostatus = "Congrats won the game"       
        
        elif exceedwinner == " ":
            congostatus = "load"

        congowidget.config(text=congostatus)
        congowidget.grid(row=0,column=8)
    

    elif globalIdentityGame == "player2":
        myCardsList.append(data[1])
        myCardsList.append(data[3])
        oppCardsList.append(data[0])
        oppCardsList.append(data[2])

        scorewidget = tk.Label(windowTk,text="Score 2: "+data[5])
        scorewidget.grid(row=0,column=6)
 
        gameScorewidget = tk.Label(windowTk,text="GameScore: "+data[7])
        gameScorewidget.grid(row=0,column=7)
        
        if data[6] == "player2":
            congostatus = "Congrats"

        if exceedwinner == "player2":
            congostatus = "you lost the game"   
        
        elif exceedwinner == "player1":
            congostatus = "Congrats won the game"

        elif exceedwinner == " ":
            congostatus = "load"        

        congowidget.config(text=congostatus)
        congowidget.grid(row=0,column=8)

    print(globalIdentityGame,myCardsList,oppCardsList)
    
    myCardsDisplayGrid = tk.Label()
    pos =0
    row=5
    for each in myCardsList:
        pos = pos + 1
        if each == "null":
            image_path = image_dir + "Card Back 4" + ".png"
        else:
            image_path = image_dir + str(each) + ".png"
        image = PIL.Image.open(image_path)
        photo = PIL.ImageTk.PhotoImage(image)
        myCardsDisplayGrid = tk.Button(image = photo)
        myCardsDisplayGrid.image = photo
        myCardsDisplayGrid.grid(row=row,column=pos,padx=10, pady=10)

    pos=0
    row=9
    oppsitionCardsDisplayGrid = tk.Label()
    for each in oppCardsList:
        pos = pos + 1
        if each == "null":
            image_path = image_dir + "Card Back 4" + ".png"
        else:
            image_path = image_dir + str(each) + ".png"
        image = PIL.Image.open(image_path)
        photo = PIL.ImageTk.PhotoImage(image)
        oppsitionCardsDisplayGrid = tk.Button(image = photo)
        oppsitionCardsDisplayGrid.image = photo  
        oppsitionCardsDisplayGrid.grid(row=row,column=pos,padx=10, pady=10)  


def convertLabeltoValue(pos):
    pos = pos.split(" ")
    pos = pos[0]
    if pos == "King":
        target = 13
    elif pos == "Queen":
        target = 12

    elif pos == "Jack":
        target = 11
    
    elif pos == "Ace":
        target = 1

    else:
        target = pos        
    
    return target

def cardClicked(playeridentity,session,pos):
    cardLabel=pos
    pos = convertLabeltoValue(pos)
    print("getVlaue is ",pos)
    client.cardHit(globalGamePlayerSocket,playeridentity,pos,session,cardLabel)
   

def dealer():
    global cardDealerButton
    cardDealerButton.config(text="Serve Cards")
    cardDealerButton.config(command=serveCards)
    cardDealerButton.grid(row=0,column=1)

def remove_cards_grid_cut():
    for one in list_of_cards_grid_cut:
            one.grid_forget()

def updateDeckCardValue(globalSessionId,globalUserName,targetValue,globalIdentityGame):
    client.updateDeckCardValue(globalGamePlayerSocket,globalSessionId,globalUserName,targetValue,globalIdentityGame) 

def cut_button_clicked():
    global count, cutCardsButton,cutCardsLabel,shuffleButton,statusWaiting
    cutCardsButton.grid_forget()
    shuffleButton.grid_forget()
    targetCard = " "
    count = count + 1
    while(count > 2):
        cutCardsButton.grid_forget()
    global cutCardsLabel,list_of_cards_grid_cut,statusWaiting 
    remove_cards_grid()
    if cutCardsLabel:
        remove_cards_grid_cut()
     
    randomCardsNumber = random.randint(5,20)
    row = 1
    pos = 0
    col = -1
    randomcardPick = shuffle_cards()
    randomCardsPick = randomcardPick[randomCardsNumber]
    for e in range(randomCardsNumber):
        pos = pos + 1
        col = col + 1
        cardbackimage = "Card Back 4"
        if pos == randomCardsNumber:
            cardbackimage = randomCardsPick
            targetCard = cardbackimage
        image_path = image_dir + str(cardbackimage) + ".png"
        image = PIL.Image.open(image_path)
        photo = PIL.ImageTk.PhotoImage(image)
        cutCardsLabel = Label(image = photo)
        cutCardsLabel.image = photo
        if(pos >= 1 and pos <= 10):
             cutCardsLabel.grid(row=row,column=col)
             list_of_cards_grid_cut.append(cutCardsLabel)
        elif(pos > 10 and pos <= 20):                               
            if pos==11:
                col = 0
                row = 2 
            cutCardsLabel.grid(row=row,column=col)
            list_of_cards_grid_cut.append(cutCardsLabel)
        elif(pos > 20 and pos <= 30):
            if pos == 21:
                col = 0
                row = 3
            cutCardsLabel.grid(row=row,column=col)
            list_of_cards_grid_cut.append(cutCardsLabel)
        elif(pos > 30 and pos <= 40):
            if pos == 31:
                col = 0
                row = 4
            cutCardsLabel.grid(row=row,column=col)
            list_of_cards_grid_cut.append(cutCardsLabel)
        elif(pos > 40 and pos <= 52):
            if pos == 41:
                col = 0
                row = 5
            cutCardsLabel.grid(row=row,column=col)
            list_of_cards_grid_cut.append(cutCardsLabel)
    local_value = len(list_of_cards_grid_cut)
    targetCard = str(targetCard)
    targetValue = targetCard.split(" ")
    targetValue = targetValue[0]
    if (targetValue=="Queen"):
        targetValue = 12

    elif targetValue == "Jack":
        targetValue = 11 
    elif targetValue == "King":
        targetValue = 13
    elif targetValue == "Ace":
        targetValue =1           

    print("targetValue",targetValue,"identity",globalIdentityGame)
    threading.Thread(target=updateDeckCardValue, args=(globalSessionId,globalUserName,targetValue,globalIdentityGame)).start()
    #client.updateDeckCardValue(globalSessionId,globalUserName,targetValue,globalIdentityGame)
    # remove_cards_grid_cut()
    statusWaiting.grid(row=0,column=0)
    threading.Thread(target=getWinnerStatus).start()
    # getWinnerStatus()



def getWinnerStatus():
    sleep(5)

    global statusWaiting,GlobalGameDealer,windowTk
    value = client.getWinnerUpdate(globalGamePlayerSocket,globalSessionId)
    statusResposne = "looser"
    if value != "retake":
        client.callPullThread(globalGamePlayerSocket)
        if globalIdentityGame == value:
            statusResposne = "winner"
            GlobalGameDealer = True
            populateLabel = str(globalSessionId) + str(globalIdentityGame)
            windowTk.title(populateLabel)
            dealer()
        else:
            statusResposne = "looser"    
            GlobalGameDealer = False
            populateLabel = str(globalSessionId) + str(globalIdentityGame)
            windowTk.title(populateLabel)
            
    else:

        shuffleButton.config(command=shuffle_button_clicked)
        shuffleButton.grid(row=0,column=0)
        cutCardsButton.config(command=cut_button_clicked)
        cutCardsButton.grid(row=0,column=1)
        statusResposne = "Retake"

    print(statusResposne,"in get winnerupadte")
    statusWaiting.config(text=statusResposne)

def sessionButtonsClicked(sessionId,name):
    global globalSessionId
    print("inside session")
    globalSessionId = sessionId
    resultStatus = client.joinToTeam(globalGamePlayerSocket,sessionId,name)
    print("resultSattus",resultStatus)
    if resultStatus.find("Activated") != -1:
        intialWindiowTk.destroy()
        username__command(sessionId)

def popudisplay(value):
    global messagedisplay
    print("inside the popup display", value)
    messagedisplay.config(text=value)


def intialButtonClicked():
    global globalSessionId,globalUserName,globalIdentityGame
    sessionNumber = random.randint(1000,2000)
    val1 = tkvar.get()
    global activeConnections
    val2 = inputNamePlayer1.get()
    globalSessionId = sessionNumber
    globalUserName = val2
    if val1 =="Create":
        globalIdentityGame = "player1"
        client.sessionCreated(globalGamePlayerSocket,sessionNumber,val2)
        intialWindiowTk.destroy()
        username__command(sessionNumber)
    elif val1 == "Join":
        globalIdentityGame = "player2"
        print("in UI",globalIdentityGame)
        listCon = client.getActiveConnections(globalGamePlayerSocket)
        print("from UI---- JOIn method",listCon)
        reslist =[]
        for exam in listCon:
            reslist.append(exam)
        if listCon:
            textWidgetName.destroy()
            inputNamePlayer1.destroy()
            popupMenu.destroy()
            infosubmitButton.destroy()
            for one in reslist:
                activeConnections.append(one)
                Button(intialWindiowTk,text=one,command=lambda: sessionButtonsClicked(one,val2)).pack()
            



def intialWindow(socket):
    global globalGamePlayerSocket,inputMessage,sendMessage,sendButton
    globalGamePlayerSocket = socket
    print('inside ui---intialwindow')
    
    
    infosubmitButton.config(command=intialButtonClicked)
# command=intialButtonClicked(optionchoosed,local__name)
    
    
    textWidgetName.pack()
    textWidgetName.place(relx=0.5, rely=0.45, anchor=CENTER)
    inputNamePlayer1.pack()
    inputNamePlayer1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    popupMenu.config(width=10)
    popupMenu.pack()
    popupMenu.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    infosubmitButton.pack()
    infosubmitButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)


    # intialwindowTkinterRefresh()
    intialWindiowTk.mainloop()
    
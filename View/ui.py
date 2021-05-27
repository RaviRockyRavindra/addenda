
import random
import socket
import sys
import PIL
import PIL.ImageTk
# from PIL import Image
import PIL.Image
import threading
from tkinter import *
import tkinter as tk
import os

count = 0


sys.path.append("Y:\projects\Addenda-game\controller")
from CardsFit import Card
from CardsFit import Deck

## global var
serverMessageGlobal = "null"
widgets_list=[]
windowTk = tk.Tk()
# frame1 = Frame(windowTk,bg="#000000",width=1000,height=500)
# frame2 = Frame(windowTk,bg="#ffffff",width=1000,height=500)
# frame2 = Frame(windowTk, borderwidth=2, pady=5)
shuffleButton = tk.Button(text ="Shuffle Cards")

cutCardsButton = tk.Button(text ="Cut Cards")
image = PIL.Image.open("Y:\projects\Addenda-game\Card Back 4.png")
photo = PIL.ImageTk.PhotoImage(image)
allCardsLabel = tk.Label()
cutCardsLabel = tk.Label()
userName__inputsubmit = " " 
playername1= "player1"
playername2= "player2"
image_dir="Y:\\projects\\Addenda-game\\res\\images\\"
# inputNamePlayer1 = tk.Entry()
# inputNamePlayer2 = tk.Entry()
addendaLabel = tk.Label(text=serverMessageGlobal)
# textWidgetName = tk.Label(text="enter players name")
playerNameLabel1 = tk.Label(text=playername1)
playerNameLabel2 = tk.Label(text=playername2)
list_of_cards_grid=[]
list_of_cards_grid_cut = []
player1score__ = 0
player2score__ = 0
playerScore1 = tk.Label(windowTk,text=player1score__)
playerScore2 = tk.Label(windowTk,text=player2score__)
# frame1.grid(row=2, column=1)
# frame2.grid(row=2, column=1)
windowTk.config(bg='green')


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
    # textWidgetName.pack()
    # textWidgetName.place(relx=0.5, rely=0.45, anchor=CENTER)
    # ##end.. label widget close


    # ## entry to take the input from user    
    # inputNamePlayer1.pack()
    # inputNamePlayer1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    # inputNamePlayer2.pack()
    # inputNamePlayer2.place(relx = 0.5, rely = 0.55, anchor = CENTER)
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

def username__command(player1_fromclient,player2_fromclient):
    global userName__inputsubmit, playername1, playername2, playerNameLabel1, playerNameLabel2

    # widgets_list.append(addendaLabel)
    # widgets_list.append(textWidgetName)
    # widgets_list.append(inputNamePlayer1)
    # widgets_list.append(inputNamePlayer2)

    

    # shuffleButton.pack()

       ## player lables are setting up here 
    playerNameLabel1.config(text=" Name "+str(player1_fromclient))
    playerNameLabel2.config(text=" Name "+str(player2_fromclient))

    playerNameLabel1.grid(row=0,column=3)
    playerNameLabel2.grid(row=0,column=4)

    # playerNameLabel1.place(rely= 0.5, relx= 0.5, anchor=CENTER)   
    # playerNameLabel2.place(rely= 0.5, relx= 0.5, anchor=CENTER)
 

    # playerNameLabel1.grid(row=0,column=1)
    # playerNameLabel2.grid(row=1,column=2)

    playerScore1.config(text=" Score 1: "+str(player1score__))
    playerScore1.grid(row=0,column=7)

    playerScore2.config(text=" Score 2: "+str(player2score__))
    playerScore2.grid(row=0,column=8)

    hide_widgets(widgets_list)    
    

    # submitButton.config(command=username__command)

    shuffleButton.config(command=shuffle_button_clicked)
    shuffleButton.grid(row=0,column=0)

    cutCardsButton.config(command=cut_button_clicked)
    cutCardsButton.grid(row=0,column=1)

    windowTkinterRefresh()
    windowTk.mainloop()

def shuffle_button_clicked():
    if cutCardsLabel:
        print("existed before")
        remove_cards_grid_cut()
    getAllCards_close()

def remove_cards_grid():
    for one in list_of_cards_grid:
        one.grid_forget()

def remove_cards_grid_cut():
    for one in list_of_cards_grid_cut:
        one.grid_forget()        

def cut_button_clicked():
    global count, cutCardsButton
    count = count + 1
    while(count > 3):
        cutCardsButton.grid_forget()
    global cutCardsLabel,list_of_cards_grid_cut
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
        if count ==1:
            cardOne = list_of_cards_grid_cut[local_value]
            cardOne = cardOne.split(" ")
            cardOne = cardOne[0]
        elif count ==2:
            cardTwo = list_of_cards_grid_cut[local_value]
            cardTwo = cardTwo.split(" ")
            cardTwo = cardTwo[0]    
 


    


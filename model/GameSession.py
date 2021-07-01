from typing import List
import ast

class GameSession:
    def __init__(self,session,gameScore,userTurn,player1score,player2score,player1move,player2move):
        self.session = session
        self.player1move = player1move
        self.player2move = player2move
        self.gameScore = gameScore
        self.userTurn = userTurn
        self.player1score = player1score
        self.player2score = player2score

    def getSession(self):
        return self.session    

    def getyPlayer1move(self):
        return self.player1move 
 
    def getyPlayer2move(self):
        return self.player2move
 
    def getyPlayer1score(self):
        return self.player1score
 
    def getyPlayer2score(self):
        # sum =0
        # print(type(self.player2score))
        # for each in self.player2score:
        #     sum = sum + int(each)
        # return sum
        return self.player2score

    def getGameScore(self):
        return self.gameScore
 
    def setSession(self,session):
        self.session = session    

    def setPlayer1move(self,player1move):
        self.player1move = player1move
 
    def setPlayer2move(self,player2move):
        self.player2move = player2move
 
    def setPlayerScore(self,platyer1score):
        self.player1score = platyer1score
 
    def setPlayer2score(self,player2socre):
        self.player2score = player2socre
 
    def setGameScore(self,gamescore):
        self.gameScore = gamescore

    def getUserTurn(self):
        return self.userTurn

    def setUserTurn(self,userTurn):
        self.userTurn = userTurn     


# listjj=[4,5,6]

# x = ['2','3']


# for c in x:
#     dd.append(ast.literal_eval(c))

# print(dd)    

# obj = GameSession(1234,"2 of hearts","null","oplayer1",2,x,x)

# print(obj.getyPlayer1score())
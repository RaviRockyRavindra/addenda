from sys import winver


class UserSession(object):
    def __init__(self,player1Name,player2Name,sessionId,player1socket,player2socket,status,deckscore1,deckscore2,winner):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.sessionId = sessionId
        self.player1socket = player1socket
        self.player2socket = player2socket
        self.status = status
        self.deckscore1 = deckscore1
        self.deckscore2 = deckscore2
        self.winner = winner


    def getPlayer1Socket(self):
        return self.player1socket

    def setPlayer1Socket(self,player1Socket):
        self.player1socket = player1Socket   

    def getPlayer2Socket(self):
        return self.player2socket

    def setPlayer2Socket(self,player2Socket):
        self.player2socket = player2Socket     

    def getPlayer1Name(self):
        return self.player1Name

    def setPlayerName(self,player1Name):
        self.player1Name = player1Name

    def getPlayer2Name(self):
        return self.player2Name

    def setPlayer2Name(self,player2Name):
        print(player2Name)
        self.player2Name = player2Name     

    def getSession(self):
        return self.sessionId

    def setSession(self,sessionId):
        self.sessionId = sessionId 


    def getStatus(self):
        return self.status

    def setStatus(self,status):
        self.status = status

    def getWinner(self):
        print("winner result in model",self.winner)
        return self.winner

    def setWinner(self,winner):
        self.winner = winner    

    def getDeckScore1(self):            
        return self.deckscore1

    def setDeckScore1(self,deckscore1):
        self.deckscore1 = deckscore1  

    def getDeckScore2(self):
        return self.deckscore2

    def setDeckScore2(self,deckscore2):
        self.deckscore2= deckscore2 
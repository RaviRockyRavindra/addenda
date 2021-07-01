import re
import MySQLdb

hostname = '192.168.0.108'
username = 'root'
password = 'root'
database = 'Addenda'



def createSession(session,cardLable1,cardLable2,playerscore1,playerscore2):
    try:
        print("createSession")
        cardlabel11="NULL"
        cardlabel22="NULL"
        sql = "Insert INTO game(sessionId,CardLabel1,CardLable2,playerscore1,playerscore2) VALUE(%s,%s,%s,%s,%s)"
        val = (session,cardLable1,cardLable2,playerscore1,playerscore2)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def updateSessionplayer1(session,CardLabel11):

    try:
        sql = "UPDATE game SET CardLabel11=%s WHERE sessionId = %s"
        val = (CardLabel11,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))

def updateSessionplayer2(session,CardLabel22):

    try:
        sql = "UPDATE game SET CardLabel22=%s WHERE sessionId = %s"
        val = (CardLabel22,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))        

def update1Session(CardLabel1,session):

    try:
        sql = "UPDATE game SET CardLabel1=%s WHERE sessionId = %s"
        val = (CardLabel1,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))

def update1Session2(session,CardLabel2):

    try:
        sql = "UPDATE game SET CardLable2=%s WHERE sessionId = %s"
        val = (CardLabel2,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))


def connect():
    try:
        global myConnection
        myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
        return myConnection
    # If connection is not successful
    except:
        print("Can't connect to database")
        return None
    # If Connection Is Successful
        print("Connected")   

def getWinner(session):

    try:
        sql = "Select playerscore1,playerscore2,CardLabel1,CardLable2,CardLabel11,cardLabel22 from game where sessionId=%s"
        val = (session,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        data = cursor.fetchone()
        print(data[0])
        print(data[1])
        player1score=int(data[0])
        player2score=int(data[1])
        card1=data[2]
        card2=data[3]
        card11=data[4]
        card22=data[5]
        
        status = "pending"
        
        if card1 != "null" and card2 != "null" and card11!="null" and card22 !="null":
            if player1score > player2score:
                status = "player1"
            else:
                status = "player2"    

        print(status)

        return status
            

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def updatedScoretoplayer1(session,score):
    try:
        sql = "UPDATE game SET playerscore1=%s WHERE sessionId = %s"
        val = (score,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))

def getRecords(session):

    try:
        sql = "Select * from game where sessionId=%s"
        val = (session,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        data = cursor.fetchone()
        print(data[2])
        print(data[3])
        print(data[6])
        print(data[7])

        return data
            

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def updatedScoretoplayer1(session,score):
    try:
        sql = "UPDATE game SET playerscore1=%s WHERE sessionId = %s"
        val = (score,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))

def updatedScoretoplayer2(session,score):
    try:
        sql = "UPDATE game SET playerscore2=%s WHERE sessionId = %s"
        val = (score,session)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        print("inside the updateSession")
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))


def getPlayer1Score(session):

    try:
        sql = "Select CardLabel1,CardLabel11 from game where sessionId=%s"
        val = (session,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        data = cursor.fetchone()
        print(data)
        number2=0
        number1=0
        if data[0] != "null":
            number = data[0].split(" ")
            print(number)
            number = number[0]
            if number == "Ace":
                number1 = 1
            elif number == "Jack":
                number1 = 11
            elif number == "Queen":
                number1 = 12
            elif number == "King":
                number1 = 13
            else:
                number1 = int(number)
            
            if data[1] != "null":
                numberT = data[1].split(" ")
                numberT = numberT[0]
                if numberT == "Ace":
                    number2 = 1
                
                elif numberT == "Jack":
                    number2 = 11
                
                elif numberT == "Queen":
                    number2 = 12
                
                elif numberT == "King":
                    number2 = 13
                else:
                    number2=numberT   

        finalcount = int(number2) + int (number1)
        print(finalcount)
        updatedScoretoplayer1(session,finalcount)
        return finalcount
            

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def getPlayer2Score(session):

    try:
        sql = "Select CardLable2,cardLabel22 from game where sessionId=%s"
        val = (session,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        data = cursor.fetchone()
        number1=0
        number2=0
        if data[0] != "null":
            number = data[0].split(" ")
            number = number[0]
            if number == "Ace":
                number1 = 1
            elif number == "Jack":
                number1 = 11
            elif number == "Queen":
                 number1 = 12
            elif number == "King":
                number1 = 13

            else:
                number1 = number

            if data[1] != "null":
                numberT = data[1].split(" ")
                numberT = numberT[0]
                if numberT == "Ace":
                    number2 = 1
                
                elif numberT == "Jack":
                    number2 = 11
                
                elif numberT == "Queen":
                    number2 = 12
                
                elif numberT == "King":
                    number2 = 13
                else:
                    number2=numberT

        finalcount = int(number2) + int (number1) 
        updatedScoretoplayer2(session,finalcount)
        print(finalcount)
        return finalcount

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def session_exist(session):
    try:
        sql = "Select sessionId from game where sessionId =%s"
        val = (session,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        if cursor.execute(sql,val):
            return True
        else:
            return False
        print("inside the sesson_exist")    

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))    


def logout(user_name_logout):
    try:
        sql = "UPDATE users SET status = %s WHERE username = %s"
        val = (0,user_name_logout)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False


def signup_user(user_name,password):
    try:
        sql = "INSERT INTO users (username, password, status) VALUES (%s,%s,%s)"
        val = (user_name,password,1)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False

def remove_user(username):
    try:
        sql = "Delete FROM users WHERE username = %s"
        val = (username,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        myConnection.commit()
        return True

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return False


def select_user_key(profilename):
    try:
        sql = "Select public_key from user_keys where profile_name = %s"
        val = (profilename,)
        myConnection = connect()
        cursor = myConnection.cursor()
        cursor.execute(sql,val)
        public_key_from_db = cursor.fetchall()
        myConnection.commit()
        return str(public_key_from_db)

    except MySQLdb.MySQLError as err:
        print("issue during execution",str(err))
        return None

getWinner(1047)
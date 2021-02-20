import sqlite3
def perdb(r_userid,r_name,r_pass,r_age):
    dbname=r_userid + ".db"
    connections=sqlite3.connect(dbname)
    cursor=connections.cursor()

    # EXPENSE DATA TABLE - EXPMAN
    cmdd="""CREATE TABLE IF NOT EXISTS EXPMAN (WEEK INTEGER PRIMARY KEY,
    FOOD FLOAT, SHOPPING FLOAT, ENTERTAINMENT FLOAT, BILLS FLOAT)"""
    cursor.execute(cmdd)
    cursor.execute("INSERT INTO EXPMAN VALUES (1,0,0,0,0)") #Initialising the blocks 
    connections.commit()
    cursor.execute("INSERT INTO EXPMAN VALUES (2,0,0,0,0)")
    connections.commit()
    cursor.execute("INSERT INTO EXPMAN VALUES (3,0,0,0,0)")
    connections.commit()
    cursor.execute("INSERT INTO EXPMAN VALUES (4,0,0,0,0)")
    connections.commit()
    #-----

    # BALANCE and EXPENSE_LIMIT DATA TABLE - UPBAL
    cmdb="""CREATE TABLE IF NOT EXISTS UPBAL (BALANCE FLOAT, EXPENSE_LMT FLOAT)"""
    cursor.execute(cmdb)
    cursor.execute("INSERT INTO UPBAL VALUES (0,0)")   #Initialising the blocks
    connections.commit()
    #------


    cursor.execute("SELECT *FROM EXPMAN")
    r=cursor.fetchall()
    print(r)
    print("success")

    cursor.execute("SELECT *FROM UPBAL")
    r2=cursor.fetchall()
    print(r2)
    print("success")
    connections.close()


def register(r_name,r_userid,r_pass,r_age):
    connections=sqlite3.connect('youtest.db')
    cursor=connections.cursor()
    
    #ALL USERS DATA BASE TABLE
    cmd1="""CREATE TABLE IF NOT EXISTS usertest 
    (userid TEXT PRIMARY KEY, name TEXT, pass TEXT, age INTEGER)"""
    cursor.execute(cmd1)
    #-------

    cursor.execute("INSERT INTO usertest values (?,?,?,?)",(r_userid,r_name,r_pass,r_age))
    connections.commit() 
    
    #cursor.execute("SELECT *FROM usertest WHERE userid=(?)",(r_userid,))
    #r=cursor.fetchall()
    #print(r)
    
    cursor.execute("SELECT *FROM usertest")
    r=cursor.fetchall()
    print(r)

    #calling function for indv user database
    perdb(r_userid,r_name,r_pass,r_age)
    #----
    
    connections.close()

x=input("Create UserID : ")
y=input("Enter your Name : ")
z=input("Create Password : ")
i=int(input("Enter your age : "))
register(x,y,z,i)
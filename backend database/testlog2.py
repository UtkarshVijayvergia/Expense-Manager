def logtest2(l_userid,l_pass):
    import sqlite3
    connections=sqlite3.connect('propresff.db')
    cursor=connections.cursor()
    cursor.execute("SELECT userid FROM usertest where userid=(?)",(l_userid,))
    r=cursor.fetchone()[0]
    #print(r)
    if r!=None:
        cursor.execute("SELECT pass FROM usertest where userid=(?)",(l_userid,))
        t=cursor.fetchone()[0]
        if t==l_pass:
            #print(t)
            #features()
            print("LOGIN SUCCESSFUL")
    connections.close()
l_userid=input("USER_ID : ")
l_pass=input("PASSWORD : ")
logtest2(l_userid,l_pass)

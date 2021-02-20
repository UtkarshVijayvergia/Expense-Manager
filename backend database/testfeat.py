import sqlite3
from matplotlib import pyplot as plt


def feattest(l_userid):
    lpdb=l_userid + ".db"
    connections=sqlite3.connect(lpdb)
    cursor=connections.cursor()



    def upbalt(lpdb,up_bal):
        connections=sqlite3.connect(lpdb)
        cursor=connections.cursor()
        #cmdb="""CREATE TABLE IF NOT EXISTS UPBAL (BALANCE FLOAT)"""
        #cursor.execute(cmdb)
        #cursor.execute("UPDATE UPBAL SET BALANCE = (?)",(up_bal,))
        cursor.execute("SELECT *FROM UPBAL")
        bprv_val=cursor.fetchone()[0]
        bnew_val=bprv_val+up_bal
        cursor.execute("UPDATE UPBAL SET BALANCE = (?)",(bnew_val,))
        #print(new_val)
        #cursor.execute("SELECT *FROM UPBAL")
        #r=cursor.fetchall()
        #print(r)

        connections.commit()
        connections.close()
    
    def explimit(lpdb,up_exp):
        connections=sqlite3.connect(lpdb)
        cursor=connections.cursor()

        #TABLE UPBAL   
        cursor.execute("SELECT *FROM UPBAL")
        eprv_val=cursor.fetchone()[1]
        enew_val=eprv_val+up_exp
        cursor.execute("UPDATE UPBAL SET EXPENSE_LMT = (?)",(enew_val,))

        cursor.execute("SELECT *FROM UPBAL")
        rx=cursor.fetchone()[0]
        print("CURRENT BALANCE : ",rx)

        cursor.execute("SELECT *FROM UPBAL")
        rx7=cursor.fetchone()[1]
        print("EXPENSE LIMIT : ",rx7)

        connections.commit()
        connections.close()

    def weekdatt(lpdb,nweek,e_fo,e_sh,e_ent,e_bil):
        connections=sqlite3.connect(lpdb)
        cursor=connections.cursor()

        #TABLE EXPMAN
        if nweek==1:
            cursor.execute("UPDATE EXPMAN SET FOOD=(?),SHOPPING=(?),ENTERTAINMENT=(?),BILLS=(?) WHERE WEEK=1",(e_fo,e_sh,e_ent,e_bil))
        elif nweek==2:
            cursor.execute("UPDATE EXPMAN SET FOOD=(?),SHOPPING=(?),ENTERTAINMENT=(?),BILLS=(?) WHERE WEEK=2",(e_fo,e_sh,e_ent,e_bil))
        elif nweek==3:
            cursor.execute("UPDATE EXPMAN SET FOOD=(?),SHOPPING=(?),ENTERTAINMENT=(?),BILLS=(?) WHERE WEEK=3",(e_fo,e_sh,e_ent,e_bil))
        elif nweek==4:
            cursor.execute("UPDATE EXPMAN SET FOOD=(?),SHOPPING=(?),ENTERTAINMENT=(?),BILLS=(?) WHERE WEEK=4",(e_fo,e_sh,e_ent,e_bil))
        else:
            print("Not Valid")
        
        connections.commit()
        cursor.execute("SELECT *FROM EXPMAN")
        exp_prt=cursor.fetchall()
        print(exp_prt)

        #TOTAL EXPENSE PRINT

        #WEEK 1
        s_exp1=0
        cursor.execute("SELECT *FROM EXPMAN WHERE WEEK = 1")
        #for i in range(4):
        rx=cursor.fetchall()
        #for i in range(4):
            #v=rx[i]
            #s_exp1=s_exp1+v


        print("TOTAL EXPENSE FOR WEEK 1 : ",rx)

        #WEEK 2
        s_exp2=0
        cursor.execute("SELECT *FROM EXPMAN WHERE WEEK = 2")
        #for i in range(4):
        ry=cursor.fetchall()
        #    s_exp2=s_exp2+ry

        print("TOTAL EXPENSE FOR WEEK 2 : ",ry)

        #WEEK 3
        s_exp3=0
        cursor.execute("SELECT *FROM EXPMAN WHERE WEEK = 3")
        #for i in range(4):
        rz=cursor.fetchall()
         #   s_exp3=s_exp3+rz

        print("TOTAL EXPENSE FOR WEEK 3 : ",rz)

        #WEEK 4
        s_exp4=0
        cursor.execute("SELECT *FROM EXPMAN WHERE WEEK = 4")
        #for i in range(4):
        rza=cursor.fetchall()
            #s_exp4=s_exp4+rza

        print("TOTAL EXPENSE FOR WEEK 4 : ",rza)


        #FINAL PRINT TOTAL EXPENSE
        #s_expt=s_exp1+s_exp2+s_exp3+s_exp4
        #print("TOTAL EXPENSES MADE SO FAR DURING THIS MONTH : ",s_expt)

        connections.close()

    
    def statrep(lpdb):

        connections=sqlite3.connect("UAR.db")
        cursor=connections.cursor()
        cursor.execute("SELECT *FROM EXPMAN")
        rpp=cursor.fetchall()
        print(rpp)
        cursor.execute("SELECT SUM(FOOD) FROM EXPMAN")
        sf1=cursor.fetchone()[0]
        print(sf1)
        cursor.execute("SELECT SUM(SHOPPING) FROM EXPMAN")
        sf2=cursor.fetchone()[0]
        print(sf2)
        cursor.execute("SELECT SUM(ENTERTAINMENT) FROM EXPMAN")
        sf3=cursor.fetchone()[0]
        print(sf3)
        cursor.execute("SELECT SUM(BILLS) FROM EXPMAN")
        sf4=cursor.fetchone()[0]
        print(sf4)

        xb=['Food','Shopping','Entertainment','Bills']

        yb=[sf1,sf2,sf3,sf4]

        plt.bar(xb,yb)
        plt.show()

        connections.close()
    
    connections.close()


    




    upbalt(lpdb,by)
    explimit(lpdb,ey)
    weekdatt(lpdb,nweek,e_fo,e_sh,e_ent,e_bil)
    statrep(lpdb)




        

    #def statrt():

# Input for user id    
x=input("Enter UserID : ")

xvp=input("Enter Password: ")

#Input for balance 
by=eval(input("Enter the latest transaction to update your Balance : "))

#Input for exp_limit
ey=eval(input("Increase or Decrease your Expense Limit : "))
#feattest(x) 

#Input for week
nweek=int(input("For which Week, Expenses have to be registerd? : "))

e_fo=eval(input("Enter Food Expense: "))
e_sh=eval(input("Enter Shopping Expense: "))
e_ent=eval(input("Enter Entertainment Expense: "))
e_bil=eval(input("Enter Bills Expense: "))

feattest(x)




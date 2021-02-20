from tkinter import *
root = Tk()

#######################################################################################################


# EXIT BUTTON FUNCTION
def destroy():
    main.destroy()
    root.destroy()


#########################################################################################################


# BUTTON HOVER EFFECT

def hover_b1(b):
    b1['bg'] = 'SpringGreen3'

def hover_b1_leave(b):  
    b1['bg'] = 'SystemButtonFace'


def hover_b2(b):
    b2['bg'] = 'SpringGreen3'

def hover_b2_leave(b):  
    b2['bg'] = 'SystemButtonFace'


def hover_b3(b):
    b3['bg'] = 'SpringGreen3'

def hover_b3_leave(b):  
    b3['bg'] = 'SystemButtonFace'


def hover_b4(b):
    b4['bg'] = 'SpringGreen3'

def hover_b4_leave(b):  
    b4['bg'] = 'SystemButtonFace'


def hover_login_button(b):
    login_button['bg'] = 'SpringGreen3'

def hover_login_button_leave(b):  
    login_button['bg'] = 'SystemButtonFace'


def hover_back_button(b):
    back_button['bg'] = 'SpringGreen3'

def hover_back_button_leave(b):  
    back_button['bg'] = 'SystemButtonFace'


def hover_week_1(b):
    week_1['bg'] = 'SpringGreen3'

def hover_week_1_leave(b):  
    week_1['bg'] = 'SystemButtonFace'


def hover_week_2(b):
    week_2['bg'] = 'SpringGreen3'

def hover_week_2_leave(b):  
    week_2['bg'] = 'SystemButtonFace'


def hover_week_3(b):
    week_3['bg'] = 'SpringGreen3'

def hover_week_3_leave(b):  
    week_3['bg'] = 'SystemButtonFace'


def hover_week_4(b):
    week_4['bg'] = 'SpringGreen3'

def hover_week_4_leave(b):  
    week_4['bg'] = 'SystemButtonFace'


def hover_back_button_main1(b):
    back_button_main1['bg'] = 'SpringGreen3'

def hover_back_button_main1_leave(b):  
    back_button_main1['bg'] = 'gray17'


def hover_submit(b):
    submit['bg'] = 'SpringGreen3'

def hover_submit_leave(b):  
    submit['bg'] = 'gray17'


#####################################################################################################


# WEEKLY DATA ENTER WINDOW
def main1():

    main1 = Toplevel(main)
    main1.iconbitmap('logo.ico')
    
    # SET HEIGHT & WIDTH
    main1.geometry('900x700')   # width x height
    main1.minsize(450,750)      
    main1.maxsize(10000,10000)

    # dictionary of colors:
    colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    # setting root window:

    main1.title('EXPENSE MANAGER')
    main1.config(bg="gray17")

    # IMAGE
    global photo_login
    global logo_login

    photo_login = PhotoImage(file = 'logo_write.png')
    logo_login = Label(main1, image = photo_login)
    logo_login.place(x=80,y=10)

    # TEXT
    enter_weekly_label = Label(main1, text = 'Enter Your Weekly Expenses', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    enter_weekly_label.place(x=250, y=280)

    #######################################################################################################

    # WEEKLY DATA ENTER WINDOW
    def weekx():
        weekx = Toplevel(main1)
        weekx.iconbitmap('logo.ico')
        
        # SET HEIGHT & WIDTH
        weekx.geometry('900x700')   # width x height
        weekx.minsize(450,750)      
        weekx.maxsize(10000,10000)

        # dictionary of colors:
        #colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

        # setting root window:

        weekx.title('EXPENSE MANAGER')
        weekx.config(bg="gray17")

        # IMAGE
        global photo_login
        global logo_login

        photo_login = PhotoImage(file = 'logo_write.png')
        logo_login = Label(weekx, image = photo_login)
        logo_login.place(x=80,y=10)
        

        # SIGN UP TITLE
        weekx_title = Label(weekx, text='PLEASE ENTER YOUR EXPENSES',font=('comicsansms', 35), bg="gray17", fg="light cyan")
        weekx_title.place(x=250, y=280)

        # TEXT
        food = Label(weekx, text='FOOD',font=('comicsansms', 15), bg="gray17", fg="light cyan")
        shopping = Label(weekx, text='SHOPPING',font=('comicsansms', 15), bg="gray17", fg="light cyan")
        entertainment = Label(weekx, text='ENTERTAINMENT',font=('comicsansms', 15), bg="gray17", fg="light cyan")
        bills = Label(weekx, text='BILLS',font=('comicsansms', 15), bg="gray17", fg="light cyan")    

        food.place(x=500,y=400)
        shopping.place(x=500,y=450)
        entertainment.place(x=500,y=500)
        bills.place(x=500,y=550)

        # INPUT STORING
        food_value = StringVar()
        shopping_value = StringVar()
        entertainment_value = StringVar()
        bills_value = StringVar()

        food_entry = Entry(weekx, textvariable=food_value,font=('comicsansms', 15))
        shopping_entry = Entry(weekx, textvariable=shopping_value,font=('comicsansms', 15))
        entertainment_entry = Entry(weekx, textvariable=entertainment_value,font=('comicsansms', 15))
        bills_entry = Entry(weekx, textvariable=bills_value,font=('comicsansms', 15))

        food_entry.place(x=690,y=400)
        shopping_entry.place(x=690,y=450)
        entertainment_entry.place(x=690,y=500)
        bills_entry.place(x=690,y=550)


        ##################################################################

        # GETTING VALUES IN A TEXT FILE
        def getvals_weekx():
            print(f'{food_value.get(), shopping_value.get(), entertainment_value.get(), bills_value.get() }')
            with open('EM_weekx.txt','a') as f:
                f.write(f'/n{food_value.get(), shopping_value.get(), entertainment_value.get(), bills_value.get()}')

        ##################################################################


        # SUBMIT BUTTON
        global submit

        submit = Button(weekx,text='SUBMIT',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='PLUS')
        submit.place(x=570,y=680)

        submit.bind('<Enter>',hover_submit)
        submit.bind('<Leave>',hover_submit_leave)        
        

        # BACK BUTTON
        global back_button_main1

        back_button_main1 = Button(weekx, text='BACK',width=9,height=1,bg='gray17',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=weekx.destroy)
        back_button_main1.place(x=30,y=30)

        back_button_main1.bind('<Enter>',hover_back_button_main1)
        back_button_main1.bind('<Leave>',hover_back_button_main1_leave)
        
        
        weekx.mainloop()


    #######################################################################################################
    
    # WEEK BUTTONS
    global week_1
    global week_2
    global week_3
    global week_4

    week_1 = Button(main1, text='WEEK 1',width=11,height=1,bg='white',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus')
    week_2 = Button(main1, text='WEEK 2',width=11,height=1,bg='white',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus')
    week_3 = Button(main1, text='WEEK 3',width=11,height=1,bg='white',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus')
    week_4 = Button(main1, text='WEEK 4',width=11,height=1,bg='white',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus')

    week_1.place(x=300,y=450)
    week_2.place(x=900,y=450)
    week_3.place(x=300,y=600)
    week_4.place(x=900,y=600)

    # CONFIGURE COMMANDS TO BUTTON
    week_1.config(command=weekx)
    week_2.config(command=weekx)
    week_3.config(command=weekx)
    week_4.config(command=weekx)

    # ADDING HOVER EFFECT TO BUTTONS
    week_1.bind('<Enter>',hover_week_1)
    week_1.bind('<Leave>',hover_week_1_leave)

    week_2.bind('<Enter>',hover_week_2)
    week_2.bind('<Leave>',hover_week_2_leave)

    week_3.bind('<Enter>',hover_week_3)
    week_3.bind('<Leave>',hover_week_3_leave)

    week_4.bind('<Enter>',hover_week_4)
    week_4.bind('<Leave>',hover_week_4_leave)




    # BACK BUTTON
    global back_button_main1

    back_button_main1 = Button(main1, text='BACK',width=9,height=1,bg='gray17',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=main1.destroy)
    back_button_main1.place(x=30,y=30)

    back_button_main1.bind('<Enter>',hover_back_button_main1)
    back_button_main1.bind('<Leave>',hover_back_button_main1_leave)


    main1.mainloop()


######################################################################################################


# UPDATE BALANCE LIMIT
def main2():

    main2 = Toplevel(main)
    main2.iconbitmap('logo.ico')
    
    # SET HEIGHT & WIDTH
    main2.geometry('900x700')   # width x height
    main2.minsize(450,750)      
    main2.maxsize(10000,10000)

    # dictionary of colors:
    colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    # setting root window:

    main2.title('EXPENSE MANAGER')
    main2.config(bg="gray17")

    # IMAGE
    global photo_login
    global logo_login

    photo_login = PhotoImage(file = 'logo_write.png')
    logo_login = Label(main2, image = photo_login)
    logo_login.place(x=80,y=10)

    # TEXT
    current_balance_label = Label(main2, text = 'Your Current Balance Limit is : Rs 6500', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    new_balance_label = Label(main2, text = 'Please Enter Your New Balance Limit ', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    
    current_balance_label.place(x=250, y=280)
    new_balance_label.place(x=250,y=430)

    # INPUT STORING
    new_balance_limit = StringVar()
    new_balance_limit_entry = Entry(main2, textvariable=new_balance_limit,font=('comicsansms', 15))
    new_balance_limit_entry.place(x=400,y=510)

    # SUBMIT BUTTON
    global submit

    submit = Button(main2, text='SUBMIT',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='PLUS')
    submit.place(x=430,y=600)

    submit.bind('<Enter>',hover_submit)
    submit.bind('<Leave>',hover_submit_leave)

    # BACK BUTTON
    global back_button_main1

    back_button_main1 = Button(main2, text='BACK',width=9,height=1,bg='gray17',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=main2.destroy)
    back_button_main1.place(x=30,y=30)

    back_button_main1.bind('<Enter>',hover_back_button_main1)
    back_button_main1.bind('<Leave>',hover_back_button_main1_leave)


    main2.mainloop()


#######################################################################################################


# UPDATE EXPENSE LIMIT
def main3():

    main3 = Toplevel(main)
    main3.iconbitmap('logo.ico')
    
    # SET HEIGHT & WIDTH
    main3.geometry('900x700')   # width x height
    main3.minsize(450,750)      
    main3.maxsize(10000,10000)

    # dictionary of colors:
    colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    # setting root window:

    main3.title('EXPENSE MANAGER')
    main3.config(bg="gray17")

    # IMAGE
    global photo_login
    global logo_login

    photo_login = PhotoImage(file = 'logo_write.png')
    logo_login = Label(main3, image = photo_login)
    logo_login.place(x=80,y=10)

    # TEXT
    current_balance_label = Label(main3, text = 'Your Current Expense Limit is : Rs 6000', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    new_balance_label = Label(main3, text = 'Please Enter Your New Expense Limit ', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    
    current_balance_label.place(x=250, y=280)
    new_balance_label.place(x=250,y=430)

    # INPUT STORING
    new_expense_limit = StringVar()
    new_expense_limit_entry = Entry(main3, textvariable=new_expense_limit,font=('comicsansms', 15))
    new_expense_limit_entry.place(x=400,y=510)

    # SUBMIT BUTTON
    global submit

    submit = Button(main3, text='SUBMIT',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='PLUS')
    submit.place(x=430,y=600)

    submit.bind('<Enter>',hover_submit)
    submit.bind('<Leave>',hover_submit_leave)

    # BACK BUTTON()
    global back_button_main1

    back_button_main1 = Button(main3, text='BACK',width=9,height=1,bg='gray17',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=main3.destroy)
    back_button_main1.place(x=30,y=30)

    back_button_main1.bind('<Enter>',hover_back_button_main1)
    back_button_main1.bind('<Leave>',hover_back_button_main1_leave)


    main3.mainloop()


#######################################################################################################


# STATISTICAL REPORT WINDOW
def main4():
    main4 = Toplevel(main)
    main4.iconbitmap('logo.ico')
    
    # SET HEIGHT & WIDTH
    main4.geometry('900x700')   # width x height
    main4.minsize(450,750)      
    main4.maxsize(10000,10000)

    # dictionary of colors:
    colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    # setting root window:

    main4.title('EXPENSE MANAGER')
    main4.config(bg="gray17")

    # TEXT
    title_label = Label(main4, text = 'REPORT', font=('comicsansms', 40, UNDERLINE), bg="gray17", fg="green")


    week_1_stats = Label(main4, text = 'WEEK 1: Rs 3150', font=('comicsansms', 20, UNDERLINE), bg="gray17", fg="light cyan")
    stats_1_label = Label(main4, text = 'FOOD: 570         SHOPPING: 1800         ENTERTAINMENT: 330         BILLS: 450', font=('comicsansms', 15), bg="gray17", fg="light cyan")
    
    week_2_stats = Label(main4, text = 'WEEK 2: Rs 480' , font=('comicsansms', 20, UNDERLINE), bg="gray17", fg="light cyan")
    stats_2_label = Label(main4, text = 'FOOD: 0           SHOPPING: 0            ENTERTAINMENT: 0           BILLS: 480', font=('comicsansms', 15), bg="gray17", fg="light cyan")

    week_3_stats = Label(main4, text = 'WEEK 3: Rs 920' , font=('comicsansms', 20, UNDERLINE), bg="gray17", fg="light cyan")
    stats_3_label = Label(main4, text = 'FOOD: 0           SHOPPING: 470          ENTERTAINMENT: 0           BILLS: 450', font=('comicsansms', 15), bg="gray17", fg="light cyan")

    week_4_stats = Label(main4, text = 'WEEK 4: Rs 1570', font=('comicsansms', 20, UNDERLINE), bg="gray17", fg="light cyan")
    stats_4_label = Label(main4, text = 'FOOD: 620         SHOPPING: 0            ENTERTAINMENT: 530         BILLS: 420', font=('comicsansms', 15), bg="gray17", fg="light cyan")
    
    total_stats =  Label(main4, text = 'TOTAL: Rs 5120', font=('comicsansms', 20, UNDERLINE), bg="gray17", fg="light cyan")
    stats_total_label =  Label(main4, text = 'FOOD: 1190         SHOPPING: 2270         ENTERTAINMENT: 860         BILLS: 1400', font=('comicsansms', 15), bg="gray17", fg="light cyan")
    
    
    # PLACING TEXTS

    title_label.place(x=550, y=20)

    week_1_stats.place(x=120,y=170)
    stats_1_label.place(x=150,y=210)

    week_2_stats.place(x=120,y=280)
    stats_2_label.place(x=150,y=320)

    week_3_stats.place(x=120,y=390)
    stats_3_label.place(x=150,y=430)

    week_4_stats.place(x=120,y=500)
    stats_4_label.place(x=150,y=540)

    total_stats.place(x=120,y=610)
    stats_total_label.place(x=150,y=650)


    # BACK BUTTON
    global back_button_main1

    back_button_main1 = Button(main4, text='BACK',width=9,height=1,bg='gray17',fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=main4.destroy)
    back_button_main1.place(x=30,y=30)

    back_button_main1.bind('<Enter>',hover_back_button_main1)
    back_button_main1.bind('<Leave>',hover_back_button_main1_leave)

#######################################################################################################


# CALCULATOR WINDOW FUNCTION
def calculator():

    calc = Toplevel(main)

    calc.title('EXPENSE MANAGER')
    calc.iconbitmap('logo.ico')

    e = Entry(calc, width = 35, borderwidth = 5, bg = 'white')
    e.grid(row = 0, column = 0, columnspan = 3, padx = 10,pady = 10)


    def add(number):    
        x = e.get()
        e.delete(0, END)
        e.insert(0, str(x)+str(number))


    def clear():
        e.delete(0,END)


    def addition():
        first = e.get()
        global f_num
        global math
        math = 'adding'
        f_num = int(first)
        e.delete(0,END)


    def equal():
        second = e.get()
        e.delete(0,END)

        if math == 'adding':
            e.insert(0, f_num + int(second))
        if math == 'subtract':
            e.insert(0, f_num - int(second))
        if math == 'multiply':
            e.insert(0, f_num * int(second))
        if math == 'divide':
            e.insert(0, f_num / int(second))


    def sub():
        first = e.get()
        global f_num
        global math
        math = 'subtract'
        f_num = int(first)
        e.delete(0,END)


    def  mul():
        first = e.get()
        global f_num
        global math
        math = 'multiply'
        f_num = int(first)
        e.delete(0,END)


    def div():
        first = e.get()
        global f_num
        global math
        math = 'divide'
        f_num = int(first)
        e.delete(0,END)


    # def button

    button_1 = Button(calc, text = '1', padx = 40, pady = 20, command = lambda: add(1), bg = 'white')
    button_2 = Button(calc, text = '2', padx = 40, pady = 20, command = lambda: add(2), bg = 'white')
    button_3 = Button(calc, text = '3', padx = 40, pady = 20, command = lambda: add(3), bg = 'white')
    button_4 = Button(calc, text = '4', padx = 40, pady = 20, command = lambda: add(4), bg = 'white')
    button_5 = Button(calc, text = '5', padx = 40, pady = 20, command = lambda: add(5), bg = 'white')
    button_6 = Button(calc, text = '6', padx = 40, pady = 20, command = lambda: add(6), bg = 'white')
    button_7 = Button(calc, text = '7', padx = 40, pady = 20, command = lambda: add(7), bg = 'white')
    button_8 = Button(calc, text = '8', padx = 40, pady = 20, command = lambda: add(8), bg = 'white')
    button_9 = Button(calc, text = '9', padx = 40, pady = 20, command = lambda: add(9), bg = 'white')
    button_0 = Button(calc, text = '0', padx = 40, pady = 20, command = lambda: add(0), bg = 'white')

    button_add = Button(calc, text = '+', padx = 39, pady = 20, command = lambda: addition(), bg = 'white')
    button_equal=Button(calc, text = '=', padx = 88, pady = 20, command = lambda: equal(), bg = 'white')
    button_clear=Button(calc, text = 'Clear', padx = 78, pady = 20, command = lambda: clear(), bg = 'white')
    button_sub = Button(calc, text = '-', padx = 40, pady = 20, command = lambda: sub(), bg = 'white')
    button_mul = Button(calc, text = '*', padx = 40, pady = 20, command = lambda: mul(), bg = 'white')
    button_div = Button(calc, text = '/', padx = 40, pady = 20, command = lambda: div(), bg = 'white')


    #create button

    button_1.grid(row = 3, column = 0)
    button_2.grid(row = 3, column = 1)
    button_3.grid(row = 3, column = 2)

    button_4.grid(row = 2, column = 0)
    button_5.grid(row = 2, column = 1)
    button_6.grid(row = 2, column = 2)

    button_7.grid(row = 1, column = 0)
    button_8.grid(row = 1, column = 1)
    button_9.grid(row = 1, column = 2)

    button_0.grid(row = 4, column = 0)

    button_add.grid(row = 5, column = 0,)
    button_clear.grid(row = 4, column = 1,columnspan = 2)
    button_equal.grid(row = 5, column = 1,columnspan = 2)

    button_sub.grid(row = 6, column = 0)
    button_mul.grid(row = 6, column = 1)
    button_div.grid(row = 6, column = 2)

 
    calc.mainloop()


######################################################################################################


# MAIN WINDOW FUNCTION
def main_win():
    global main
    main = Toplevel(root1)

    # dictionary of colors:
    colour = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    # setting root window:

    main.title('EXPENSE MANAGER')
    main.iconbitmap('logo.ico')
    main.config(bg="gray17")

    # SET HEIGHT & WIDTH
    main.geometry('900x700+850+50')   # width x height
    main.minsize(450,750)      
    main.maxsize(10000,10000)

    # SETTING BUTTON SWITCHES STATE:
    global button_switch_main
    button_switch_main = False

    # NAVIGATION BAR IMAGES:
    nav_image_main = PhotoImage(file="menu.png")
    nav_image_close_main = PhotoImage(file="close.png")

    # NAVIGATION SIDEBAR FUNCTION:
    def button_switcher():
        global button_switch_main
        if button_switch_main is True:
            # CREATE ANIMATED NAV SIDEBAR:
            for x in range(301):
                navmain.place(x=-x, y=0)
                topframe_main.update()

            # RESETTING WIDGET COLOURS:
            up_label_main.config(bg='gray17', fg='green')
            home_label_main.config(bg='orange')
            topframe_main.config(bg='orange')
            main.config(bg='gray17')

            # TURNING BUTTON/NAV BAR OFF:
            button_switch_main = False
        else:
            # MAKE DIM:
            up_label_main.config(bg=colour["nero"], fg="#5F5A33")
            home_label_main.config(bg=colour["nero"])
            topframe_main.config(bg=colour["nero"])
            main.config(bg=colour["nero"])

            # ANIMATED NAVBAR OPENING:
            for x in range(-300, 0):
                navmain.place(x=x, y=0)
                topframe_main.update()

            # TURNING BUTTON ON:
            button_switch_main = True


    # TOP NAV SIDEBAR:
    topframe_main = Frame(main, bg='orange')
    topframe_main.pack(side="top", fill=X)

    # HEAD TEXT (RIGHT):
    home_label_main = Label(topframe_main, text="EM", font="Bahnschrift 15", bg='orange', fg="gray17", height=2, padx=20)
    home_label_main.pack(side="right")

    # MAIN TEXT:
    up_label_main = Label(main, text="WELCOME TO EXPENSE MANAGER", font=('comicsansms', 40), bg="gray17", fg="light cyan")
    up_label_main.place(x=400, y=80)

    balance_label = Label(main, text = 'Your Current Balance is : Rs 3000', font=('comicsansms', 30), bg="gray17", fg="light cyan")
    balance_label.place(x=250, y=280)

    powered_label = Label(main, text='Powered by Expense Manager', font=('comicsansms', 10), bg="gray17", fg="white")
    powered_label.place(x=30,y=750)

    version_label = Label(main,text='Version 1.0.0', font=('comicsansms', 10), bg="gray17", fg="white")
    version_label.place(x=1410,y=750)

    # BUTTONS IN NAV SIDEBAR:
    nav_button_main = Button(topframe_main, image=nav_image_main, bg='orange', activebackground='orange', bd=0, padx=20, command=button_switcher)
    nav_button_main.place(x=10, y=10)

    # NAVBAR FRAME:
    navmain = Frame(main, bg="gray17", height=1000, width=300)
    navmain.place(x=-300, y=0)
    Label(navmain, font="Bahnschrift 15", bg='orange', fg="black", height=2, width=300, padx=20).place(x=0, y=0)

    dashboard_main = Button(navmain, text='Dashboard', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0) 
    update_balance_main = Button(navmain, text='Update Balance', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)
    update_expense_main = Button(navmain, text='Update Expense Limit', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)
    enter_weekly_main = Button(navmain, text='Enter Weekly Data', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)
    calculator_main = Button(navmain, text='Calculator', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0) 
    statistics_main = Button(navmain, text='Statistical Report', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)
    exit_main = Button(navmain, text='Exit', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)
    contact_main = Button(navmain, text='Contact Details', font="BahnschriftLight 15", bg="gray17", fg='orange', activebackground="gray17", activeforeground="green", bd=0)


    dashboard_main.place(x=25, y=80)
    update_balance_main.place(x=25, y=120)
    update_expense_main.place(x=25, y=160)
    enter_weekly_main.place(x=25, y=200)
    calculator_main.place(x=25, y=240)
    statistics_main.place(x=25, y=280)
    contact_main.place(x=25,y=690)
    exit_main.place(x=25, y=730)

    # CONFIGURE COMMANDS TO BUTTON
    dashboard_main.config(command=button_switcher)
    update_balance_main.config(command=main2)
    update_expense_main.config(command=main3)
    enter_weekly_main.config(command=main1)
    calculator_main.config(command=calculator)
    statistics_main.config(command=main4)
    exit_main.config(command=destroy)

    # NAVBAR CLOSE BUTTON:
    nav_button_close_main = Button(navmain, image=nav_image_close_main, bg='orange', activebackground='orange', bd=0, command=button_switcher)
    nav_button_close_main.place(x=250, y=10)



    main.mainloop()


#######################################################################################################


# LOGIN WINDOW FUNCTION
def login():

    global root1
    root1 = Toplevel(root)

    # SET HEIGHT & WIDTH
    root1.geometry('900x700')   # width x height
    root1.minsize(450,750)      
    root1.maxsize(10000,10000)

    #
    root1.iconbitmap('logo.ico')

    # IMAGE
    global photo_login
    global logo_login

    photo_login = PhotoImage(file = 'logo_write.png')
    logo_login = Label(root1, image = photo_login)
    logo_login.place(x=80,y=10)

    # LOGIN TITLE
    login_title = Label(root1, text='LOGIN',font=('comicsansms', 40))
    login_title.place(x=650,y=270)

    # TEXT
    userid = Label(root1, text='USER ID',font=('comicsansms', 20))
    password = Label(root1, text='PASSWORD',font=('comicsansms', 20))

    userid.place(x=490,y=420)
    password.place(x=480,y=490)

    # INPUT STORING
    userid_value = StringVar()
    password_value = StringVar()

    userid_entry = Entry(root1, textvariable=userid_value,font=('comicsansms', 20))
    password_entry = Entry(root1, textvariable=password_value,font=('comicsansms', 20))

    userid_entry.place(x=690,y=420)
    password_entry.place(x=690,y=490)

    ##################################################################

    # GETTING VALUES IN A TEXT FILE
    def getvals_login():
        print(f'{userid_value.get(), password_value.get()}')
        with open('EM_login.txt','a') as f:
            f.write(f'{userid_value.get(), password_value.get()}\n')

        main_win()

    ##################################################################

    # LOGIN BUTTON
    global login_button
    login_button = Button(root1, text='LOG IN',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus',command=getvals_login)
    login_button.place(x=660,y=590)
    login_button.bind('<Enter>',hover_login_button)
    login_button.bind('<Leave>',hover_login_button_leave)

    # BACK BUTTON
    global back_button
    back_button = Button(root1, text='BACK',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=root1.destroy)
    back_button.place(x=30,y=30)
    back_button.bind('<Enter>',hover_back_button)
    back_button.bind('<Leave>',hover_back_button_leave)


    root1.mainloop()


#######################################################################################################


# SIGN UP WINDOW FUNCTION
def sign_up():
    root2 = Toplevel(root)

    # SET HEIGHT & WIDTH
    root2.geometry('900x700')   # width x height
    root2.minsize(450,750)      
    root2.maxsize(10000,10000)

    #
    root2.iconbitmap('logo.ico')

    # IMAGE
    global photo_login
    global logo_login

    photo_login = PhotoImage(file = 'logo_write.png')
    logo_login = Label(root2, image = photo_login)
    logo_login.place(x=80,y=10)

    # SIGN UP TITLE
    signup_title = Label(root2, text='SIGN UP',font=('comicsansms', 35))
    signup_title.place(x=650,y=270)

    # TEXT
    name = Label(root2, text='NAME',font=('comicsansms', 15))
    age = Label(root2, text='AGE',font=('comicsansms', 15))
    userid = Label(root2, text='USER ID',font=('comicsansms', 15))
    password = Label(root2, text='PASSWORD',font=('comicsansms', 15))
    cpassword = Label(root2, text='CONFIRM PASSWORD',font=('comicsansms', 15))    

    name.place(x=500,y=400)
    age.place(x=500,y=450)
    userid.place(x=490,y=500)
    password.place(x=480,y=550)
    cpassword.place(x=460,y=600)

    # INPUT STORING
    name_value = StringVar()
    age_value = StringVar()
    userid_value = StringVar()
    password_value = StringVar()
    cpassword_value = StringVar()

    name_entry = Entry(root2, textvariable=name_value,font=('comicsansms', 15))
    age_entry = Entry(root2, textvariable=age_value,font=('comicsansms', 15))
    userid_entry = Entry(root2, textvariable=userid_value,font=('comicsansms', 15))
    password_entry = Entry(root2, textvariable=password_value,font=('comicsansms', 15))
    cpassword_entry = Entry(root2, textvariable=cpassword_value,font=('comicsansms', 15))

    name_entry.place(x=690,y=400)
    age_entry.place(x=690,y=450)
    userid_entry.place(x=690,y=500)
    password_entry.place(x=690,y=550)
    cpassword_entry.place(x=690,y=600)

    ##################################################################

    # GETTING VALUES IN A TEXT FILE
    def getvals_signup():
        print(f'{name_value.get(), age_value.get(), userid_value.get(), password_value.get(),  cpassword_value.get() }')
        with open('EM_signup.txt','a') as f:
            f.write(f'/n{name_value.get(), age_value.get(), userid_value.get(), password_value.get(),  cpassword_value.get()}')

    ##################################################################

    # SIGN UP BUTTON
    global login_button
    login_button = Button(root2, text='SIGN UP',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus',command=getvals_signup)
    login_button.place(x=660,y=670)
    login_button.bind('<Enter>',hover_login_button)
    login_button.bind('<Leave>',hover_login_button_leave)

    # BACK BUTTON
    global back_button
    back_button = Button(root2, text='BACK',width=9,height=1,fg='red',font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=root2.destroy)
    back_button.place(x=30,y=30)
    back_button.bind('<Enter>',hover_back_button)
    back_button.bind('<Leave>',hover_back_button_leave)

    root2.mainloop()


#######################################################################################################


# SET HEIGHT & WIDTH
root.geometry('900x700')   # width x height
root.minsize(450,750)      
root.maxsize(10000,10000)

# HEAD and ICON
root.title('EXPENSE MANAGER')
root.iconbitmap('logo.ico')

# IMAGE
photo = PhotoImage(file = 'logo_write.png')
logo = Label(root, image = photo)
logo.pack()

# FRAME
f1 = Frame(root)
f1.pack(side=TOP, anchor='nw',fill=X,padx=100)

# arrow button 1 -- LOGIN
arrow1 = Label(f1,text='----->',font=('comicsansms', 40, 'bold'))
arrow1.grid(row=1,column=1,pady=30)
b1 = Button(f1, fg='red', text='LOGIN',width=9,height=1,font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus',command=login)
b1.grid(row=1,column=2)
b1.bind('<Enter>',hover_b1)
b1.bind('<Leave>',hover_b1_leave)

# arrow button 2 -- SIGN UP
arrow2 = Label(f1,text='----->',font=('comicsansms', 40, 'bold'))
arrow2.grid(row=2,column=1,padx=50,pady=30)
b2 = Button(f1, fg='red', text='SIGN UP',width=9,height=1,font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus',command=sign_up)
b2.grid(row=2,column=2)
b2.bind('<Enter>',hover_b2)
b2.bind('<Leave>',hover_b2_leave)

# arrow button 3
arrow3 = Label(f1,text='----->',font=('comicsansms', 40, 'bold'))
arrow3.grid(row=3,column=1,padx=50,pady=30)
b3 = Button(f1, fg='red', text='ABOUT',width=9,height=1,font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='plus')
b3.grid(row=3,column=2)
b3.bind('<Enter>',hover_b3)
b3.bind('<Leave>',hover_b3_leave)

# arrow button 4 -- EXIT
arrow4 = Label(f1,text='----->',font=('comicsansms', 40, 'bold'))
arrow4.grid(row=4,column=1,padx=50,pady=30)
b4 = Button(f1, fg='red', text='EXIT',width=9,height=1,font=('comicsansms', 20),borderwidth=2,relief='raised',cursor='exchange',command=root.destroy)
b4.grid(row=4,column=2)
b4.bind('<Enter>',hover_b4)
b4.bind('<Leave>',hover_b4_leave)

# STATUS
status_label = Label(f1, text='E-mail: manager_expense@gmail.com',font=('comicsansms', 15), bd=1, relief=SUNKEN, anchor=E)
#status_label.grid(row=5,column=1,columnspan=1000,sticky=E+W,pady=50,padx=200)(fill=X, side=BOTTOM, ipady=2)
status_label.grid(row=5,column=1,columnspan=1000,ipady=2,pady=50,padx=200) 



root.mainloop()


#######################################################################################################
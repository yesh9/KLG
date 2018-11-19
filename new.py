from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
selectedims=[]

def start():
    global timer
    timer=30
    global d       
    global k
    k=0
    d=0
    global selectedims
    global selectedwords
    selectedwords=[]
    global fnames
    selectedims=[]
    fnames=[]
    with open('wordlist.txt','r') as f:
        x=list(f)
        for i in range(4):
            fnames.append(random.choice(x[:len(x)]).rstrip())
        for i in range(4):
            selectedims.append(PhotoImage(file=fnames[i]+'.gif'))
    creategui()
def countdown():
    global timer
    global canvas
    global tme
    if timer<30:
        canvas.delete(tme)
    timer-=1
    tme=canvas.create_text(1100,50,text="Timer Left On This Screen: "+str(timer),fill="white",font=("Lucida Calligraphy",15))
    if timer==0:
        Test()
    else:
        root.after(1000, countdown)
def creategui():
    global backgroundimg
    global selectedims
    global canvas
    global root
    global tme
    canvas.delete('all')
    canvas.update()
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    canvas.create_text(200,50,text="Kids Learning Game",fill="White",font=("Arial",25))
    canvas.create_text(683,120,text="Memorize Object on Screen",fill="White",font=("Arial",15))
    resetbutton=Button(canvas,text="Refresh",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=reset)
    canvas.create_window(1150,630,window=resetbutton)
    x=0
    for i in range(4):
        x=canvas.create_image(300+500*(i//2),150+250*(i%2),image=selectedims[i],anchor=NW)
    countdown()
def reset():
    global canvas
    global scttxts
    global root
    global k
    global d
    d=0
    k=0
    root.destroy()
    root=Tk()
    canvas=Canvas(root,width=1366,height=768)
    canvas.pack()
    scttxts=[]
    start()
k=0
scttxts=[]
def store(event,word,index):
    global selectedwords
    global txts
    global canvas
    global k
    global d
    global scttxts
    if k-d>3:
        messagebox.showinfo("Warning","Only 4 Choices are Allowed")
        return
    scttxts.append(canvas.create_text(1000,190+40*k,text=word,fill="red",font=("Arial",20)))
    canvas.tag_bind(scttxts[k],'<ButtonPress-1>',lambda evt,send=k:remove(evt,send,word))
    canvas.update()
    k+=1
    selectedwords.append(word)
    selectedwords=list(set(selectedwords))
def remove(event,x,wordd):
    global selectedwords
    global txts
    global canvas
    global scttxts
    global d
    d+=1
    canvas.delete(scttxts[x])
    while wordd in selectedwords:
        selectedwords.remove(wordd)
def submit():
    guessescorrect=0
    global fnames
    global selectedwords
    for word in selectedwords:
        if word in fnames:
           guessescorrect+=fnames.count(word)
    messagebox.showinfo("Result","You got "+str((guessescorrect/len(fnames))*100)+" % Correct")
    homepage()
            
def Test():
    global backgroundimg
    global selectedims
    global canvas
    global txts
    global root
    global tme
    global k
    global scttxts
    scttxts=[]
    k=0
    global d
    d=0
    canvas.delete('all')
    canvas.update()
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    resetbutton=Button(canvas,text="Submit",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=submit)
    canvas.create_window(680,650,window=resetbutton)
    canvas.create_text(683,50,text="Select What You Saw On Last Screen",fill="White",font=("Arial",20))
    canvas.create_text(400,130,text="Select From These:",fill="White",font=("Arial",10))
    canvas.create_rectangle(300,100,500,600,outline="white",width=3)
    canvas.create_text(1000,130,text="Selected:",fill="White",font=("Arial",10))
    canvas.create_text(1000,150,text="(Can be Deselected)",fill="White",font=("Arial",8,'italic'))
    canvas.create_rectangle(900,100,1100,600,outline="white",width=3)
    f=open('wordlist.txt','r')
    x=f.readlines()
    f.close()
    txts=[]
    for i in range(len(x)):
        txts.append(canvas.create_text(400,190+40*i,text=x[i].rstrip(),fill="White",font=("Arial",20)))
    for i in range(len(x)):
        canvas.tag_bind(txts[i],'<ButtonPress-1>',lambda evt,send=x[i].rstrip():store(evt,send,i))
def homepage():
    global backgroundimg
    global selectedims
    global canvas
    global txts
    global root
    global tme
    global user
    global k
    global d
    global selectedims
    selectedtxts=[]
    k=0
    d=0
    scttxts=[]
    txts=[]
    global selectedwords
    selectedwords=[]
    canvas.delete('all')
    canvas.update()
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    startbutton=Button(canvas,text="Start Game",width=10,fg="white",bg="green",font=("Arial",13,'bold'),command=start)
    canvas.create_window(600,560,window=startbutton)
    exitbutton=Button(canvas,text="Exit",width=10,fg="white",bg="Red",font=("Arial",13,'bold'),command=root.destroy)
    canvas.create_window(750,560,window=exitbutton)
    lobutton=Button(canvas,text="Logout",width=10,fg="white",bg="Red",font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(450,560,window=lobutton)
    canvas.create_text(683,50,text="Kids Learning Game",fill="White",font=("Arial",45,'bold'))
    canvas.create_text(1200,50,text="Welcome "+str(user)+',',fill="White",font=("Arial",15,'bold'))
    canvas.create_text(683,150,text="Kids Learning Game is a Game designed for kids to learn names of objects and day to day things.\n\
It also Emphasises on memmory building and retaining capacity of kids to produce great outcomes.",fill="white",font=("Arial",15))
    canvas.create_text(200,250,text="Rules:-",fill="White",font=("Arial",25,'bold'))
    canvas.create_text(600,370,text="1- You will be given 30 second to carefully obeseve 4 images on first screen.\n\n\
2- After Timer Runs Out You Will be Promted to choose the images you saw\n\n\
3- You Cannot Choose more than 4 Items\n\n\
4-You will be shown your scores percentage",fill="white",font=("Arial",15))

ci=0
valuser=False
def validity(event,x,y):
    global tme
    global ci
    global password
    global valuser
    valuser=False
    usr=username.get()
    if ci>0:
        canvas.delete(tme)
    if len(usr)<5 or usr.isdigit() or '-' in usr or '$'in usr or '%' in usr or '^' in usr or '*' in usr:
        tme=canvas.create_text(x,y,text="X",fill="White",font=("Arial",20,'bold'))
        valuser=False
    else:
         tme=canvas.create_text(x,y,text="\u2713",fill="White",font=("Arial",20,'bold'))
         valuser=True
    ci+=1
cip=0
valpass=False
def validitypass(event,x,y):
    global tme2
    global cip
    global password
    global valpass
    valpass=False
    pwd=password.get()
    pascore=3
    if cip>0:
        canvas.delete(tme2)
    if len(pwd)<8:
        pascore-=1
    if pwd.isdigit() or( '-' not in pwd and '$' not in pwd and '%' not in pwd and '^' not in pwd and '*'  not in pwd and '@' not in pwd and '#' not in pwd and '!' not in pwd):
        pascore-=1
    f=1
    for i in range(10):
        if str(i) in pwd:
            f=0
    if f:
        pascore-=1
    if pascore>=3:
        tme2=canvas.create_text(x,y,text="\u2713",fill="White",font=("Arial",20,'bold'))
        valpass=True
    else:
        tme2=canvas.create_text(x,y,text="X",fill="White",font=("Arial",20,'bold'))
        valpass=False
    cip+=1
def skip():
    global user
    user="Guest"
    homepage()
def loginLogic():
    global username
    global password
    global user
    flag=True
    usr=username.get()
    pwd=password.get()
    f=open("users.dat",'r')
    users=list(f)
    f.close()
    for i in users:
        uname,passw,secq,secan=i.split('+')
        if usr==uname and pwd==passw:
            flag=False
            user=usr
            homepage()
    if flag:
         messagebox.showerror("Error", "Invalid Id or password")
def loginpage():
    global backgroundimg
    global selectedims
    global canvas
    global txts
    global root
    global tme
    global username
    global password
    global ci
    canvas.delete('all')
    canvas.update()
    ci=0
    cip=0
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    canvas.create_text(945,150,text="Kids Learning Game",fill="White",font=("Arial",25,'bold'))
    canvas.create_rectangle(770,180,1120,530,outline="White",width=2)
    canvas.create_text(945,220,text="Login",fill="White",font=("Arial",20,'bold'))
    canvas.create_text(870,300,text="Username:",fill="White",font=("Arial",15,'bold'))
    username=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13))
    username.bind('<KeyPress>',lambda evt:validity(evt,1100,300))
    canvas.create_window(1000,300,window=username)
    canvas.create_text(870,350,text="Password:",fill="White",font=("Arial",15,'bold'))
    password=Entry(canvas,width=15,fg="white",bd=3,bg="Magenta",font=("Arial",13),show='*')
    password.bind("<KeyPress>",lambda evt:validitypass(evt,1100,350))
    canvas.create_window(1000,350,window=password)
    loginbutton=Button(canvas,text="Login",width=10,fg="white",bg="green",font=("Arial",13,'bold'),command=loginLogic)
    canvas.create_window(900,440,window=loginbutton)
    reg=canvas.create_text(1030,440,text="Register",fill="white",font=("Arial",13))
    canvas.tag_bind(reg,"<ButtonPress-1>",lambda evt:Register())
    sk=canvas.create_text(947,510,text="Continue as Guest >>",fill="white",font=("Arial",13,'underline'))
    canvas.tag_bind(sk,"<ButtonPress-1>",lambda evt:skip())
    fg=canvas.create_text(947,480,text="Forgot Password",fill="white",font=("Arial",13,'underline'))
    canvas.tag_bind(fg,"<ButtonPress-1>",lambda evt:forgotpage())
def RegisterLogic():
    global username
    global securityquestion
    global password
    global secans
    global valuser
    global valpass
    if valuser and valpass:
        usr=username.get()
        pwd=password.get()
        secq=securityquestion.get()
        secans1=secans.get()
        flag=0
        f=open("users.dat",'r')
        users=list(f)
        f.close()
        for i in users:
            if usr in i:
                   messagebox.showerror("Validatation Error", "Username Already Exists")
                   flag=1
        if flag==0:
                f=open("users.dat",'a')
                f.write(usr+'+'+pwd+'+'+secq+'+'+secans1+'\n')
                f.close()
                messagebox.showinfo("Registration Successful", "Registration success! You Can Now Login")
                loginpage()
    else:
        messagebox.showinfo("Registration Successful", "Invalid Entries")
def Register():
    global backgroundimg
    global selectedims
    global canvas
    global txts
    global root
    global tme
    global username
    global password
    global ci
    global securityquestion
    global combostyle
    global secans
    canvas.delete('all')
    canvas.update()
    ci=0
    cip=0
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    canvas.create_text(945,150,text="Kids Learning Game",fill="White",font=("Arial",25,'bold'))
    canvas.create_rectangle(770,180,1120,530,outline="White",width=2)
    canvas.create_text(945,200,text="Register",fill="White",font=("Arial",20,'bold'))
    canvas.create_text(870,270,text="Username:",fill="White",font=("Arial",15,'bold'))
    canvas.create_text(870,390,text="Answer:",fill="White",font=("Arial",15,'bold'))
    username=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13))
    username.bind("<Key>",lambda evt:validity(evt,1100,270))
    canvas.create_window(1000,270,window=username)
    canvas.create_text(870,310,text="Password:",fill="White",font=("Arial",15,'bold'))
    password=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13),show='*')
    password.bind("<Key>",lambda evt:validitypass(evt,1100,310))
    canvas.create_window(1000,310,window=password)
    securityquestion=StringVar()
    securityquestion.set("Select A Security Question?")
    combostyle.theme_use('combostyle')
    secmenu=  ttk.Combobox(root, width=38,textvariable=securityquestion)
    secmenu['values'] = ["What Was Your First Car?","Which boy/girl you first kissed?","What was your childhood nickname?","Who is Your best friend?"]
    secmenu['state'] = 'readonly'
    canvas.create_window(947,350,window=secmenu)
    secans=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13))
    canvas.create_window(1000,390,window=secans)
    loginbutton=Button(canvas,text="Register",width=10,fg="white",bg="green",font=("Arial",13,'bold'),command=RegisterLogic)
    canvas.create_window(900,450,window=loginbutton)
    reg=canvas.create_text(1030,450,text="Login",fill="white",font=("Arial",13))
    canvas.tag_bind(reg,"<ButtonPress-1>",lambda evt:loginpage())
    sk=canvas.create_text(947,510,text="Continue as Guest >>",fill="white",font=("Arial",13,'underline'))
    canvas.tag_bind(sk,"<ButtonPress-1>",lambda evt:skip())
def resetLogic():
    global username
    global securityquestion
    global password
    global secans
    usr=username.get()
    pwd=password.get()
    flag=0
    f=open("users.dat",'r')
    users=list(f)
    f.close()
    for i in range(len(users)):
        uname,passw,secq,secan=users[i].split('+')
        if usr==uname and secq.upper()==securityquestion.get().upper() and secan.rstrip().upper() == secans.get().upper():
            users[i]=uname+'+'+pwd+'+'+secq+'+'+secan
            flag=1
    if flag:
         f=open("users.dat",'w')
         for i in users:
             f.write(i)
         f.close()
         messagebox.showinfo("Successfull", "Password Reset Success ")
         loginpage()
    else:
         messagebox.showerror("Error", "Invalid Username or Question")
def forgotpage():
    global backgroundimg
    global selectedims
    global canvas
    global txts
    global root
    global tme
    global username
    global password
    global ci
    global securityquestion
    global secans
    global combostyle
    
    canvas.delete('all')
    canvas.update()
    ci=0
    cip=0
    backgroundimg=PhotoImage(file="vackground.gif")
    canvas.create_image(0,0,image= backgroundimg,anchor=NW)
    canvas.create_text(945,150,text="Kids Learning Game",fill="White",font=("Arial",25,'bold'))
    canvas.create_rectangle(770,180,1120,530,outline="White",width=2)
    canvas.create_text(945,200,text="Reset Password",fill="White",font=("Arial",20,'bold'))
    canvas.create_text(870,270,text="Username:",fill="White",font=("Arial",15,'bold'))
    canvas.create_text(870,390,text="Answer:",fill="White",font=("Arial",15,'bold'))
    username=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13))
    username.bind("<Key>",lambda evt:validity(evt,1100,270))
    canvas.create_window(1000,270,window=username)
    canvas.create_text(850,310,text="New Password:",fill="White",font=("Arial",15,'bold'))
    password=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13),show='*')
    password.bind("<Key>",lambda evt:validitypass(evt,1100,310))
    canvas.create_window(1000,310,window=password)
    securityquestion=StringVar()
    securityquestion.set("Select A Security Question?")
    combostyle.theme_use('combostyle')
    secmenu=  ttk.Combobox(root, width=38,textvariable=securityquestion)
    secmenu['values'] = ["What Was Your First Car?","Which boy/girl you first kissed?","What was your childhood nickname?","Who is Your best friend?"]
    secmenu['state'] = 'readonly'
    canvas.create_window(947,350,window=secmenu)
    secans=Entry(canvas,width=15,fg="white",bd=3,bg="magenta",font=("Arial",13))
    canvas.create_window(1000,390,window=secans)
    loginbutton=Button(canvas,text="Reset Password",width=15,fg="white",bg="green",font=("Arial",13,'bold'),command=resetLogic)
    canvas.create_window(900,450,window=loginbutton)
    reg=canvas.create_text(1030,450,text="Login",fill="white",font=("Arial",13))
    canvas.tag_bind(reg,"<ButtonPress-1>",lambda evt:loginpage())
    sk=canvas.create_text(947,510,text="Continue as Guest >>",fill="white",font=("Arial",13,'underline'))
    canvas.tag_bind(sk,"<ButtonPress-1>",lambda evt:skip())
root=Tk()
canvas=Canvas(root,width=1366,height=768)
canvas.pack()
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                             settings = {'TCombobox':
                                         {'configure':
                                          {'selectbackground': 'magenta',
                                           'fieldbackground': 'magenta',
                                           'selectforeground': 'white'
                                           }}} )
loginpage()
root.mainloop()
    

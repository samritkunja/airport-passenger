
import tkinter as tk
from tkinter import ttk
import random
import pickle
import datetime
from functools import partial
admin={}
passengerlist={}
flights={}
cancelled={}
supervis={}
standard={}
global seatsprice
seatsprice=0
booked=["b1"]
seatslist=[]
#flights={flightno:[departure time,destination,status,eta,location,airline,{phonno:[seats]}]}
fa=open("admin.dat","rb")
try:
    while True:
        da=pickle.load(fa)
        for i in da:
            admin[i]=da[i]
except EOFError:
    fa.close()
fs=open("supervis.dat","rb")
try:
    while True:
        ds=pickle.load(fs)
        for i in ds:
            supervis[i]=ds[i]
except EOFError:
    fs.close()
fst=open("standard.dat","rb")
try:
    while True:
        dst=pickle.load(fst)
        for i in dst:
            standard[i]=dst[i]
except EOFError:
    fst.close()
f_defineflights=open("flights.dat","rb")
try:
    while True:
        d_defineflights=pickle.load(f_defineflights)
        for i in d_defineflights:
            flights[i]=d_defineflights[i]
except EOFError:
    f_defineflights.close()
f_definecancelled=open("cancelled.dat","rb")
try:
    while True:
        d_definecancelled=pickle.load(f_definecancelled)
        for i in d_definecancelled:
            cancelled[i]=d_definecancelled[i]
except EOFError:
    f_definecancelled.close()
fp=open("passenger.dat","rb")
try:
    while True:
        dp=pickle.load(fp)
        for i in dp:
            passengerlist[i]=dp[i]
except EOFError:
    fp.close()

def airport():
    def returntomain(a):
                a.destroy()
                main()
    mainsc.destroy()
    def reminder():
        '''
        now=datetime.datetime.now()    
        for i in flights:
            l=flights[i][0].split(":")
            time=now.replace(hour=int(l[0]),minute=int(l[1]),second=0,microsecond=0)        
            if now>time:
                remindersc=tk.Tk()
                remindersc.title("Reminder!")
                tk.Label(master=remindersc,text="Flight Number "+i.upper()+" Not Updated").grid(row=0,column=0)       '''
    def deluser():
        def deluserback():
            u=uname.get()
            if not(u in admin or u in supervis or u in cancelled):
                popup=tk.Tk()
                popup.title("Username Not Found!")
                tk.Label(master=popup,text="Username not found! Please try again!").grid(row=1,column=1)
            else:
                if u in admin:
                    del admin[u]
                    delfiles("admin.dat",{u:""})
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Admin User Successfully Deleted!").grid(row=1,column=1)
                elif u in supervis:
                    del supervis[u]
                    delfiles("supervis.dat",{u:""})
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text=" Supervisor Successfully Deleted!").grid(row=1,column=1)
                if u in standard:
                    del standard[u]
                    delfiles("standard.dat",{u:""})
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Standard User Successfully Deleted!").grid(row=1,column=1)                
        delusersc=tk.Tk()
        delusersc.title("Delete A User")
        tk.Label(master=delusersc,text="Enter the Username").grid(row=1,column=0)
        uname=tk.Entry(master=delusersc)
        unamne.grid(row=1,column=1)
        r2=tk.Button(master=delusersc,text="Confirm Deletion",width=25,command=deluserback).grid(row=1,column=2)
        
    def manageuser():
        def adduser():
            def addadmin():
                def adminusname():
                    def adminuserback():
                        p=passw.get()                                                             
                        admin[u]=p
                        d={u:p}
                        files("admin.dat",d)
                        popup=tk.Tk()
                        popup.title("Success")
                        tk.Label(master=popup,text="Admin Successfully Added!").grid(row=1,column=1)
                    u=usname.get()
                    if u in admin or u in supervis or u in standard:
                            popup=tk.Tk()
                            popup.title("Username Already Exists!")
                            tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                            manageusersc.destroy()
                            aa.destroy()
                    else:        
                        tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                        passw=tk.Entry(master=aa,show='*')
                        passw.grid(row=2,column=1)
                        tk.Button(master=aa,text="Confirm Password",command=adminuserback,width=25).grid(row=2,column=3)
                aa=tk.Tk()
                aa.title("Add An Admin")
                tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
                usname=tk.Entry(master=aa)
                usname.grid(row=1,column=1)
                a3=tk.Button(master=aa,text="Confirm Username",width=25,command=adminusname).grid(row=1,column=3)
            def addsuper():
                def superusname():
                    def superuserback():
                        p=passw.get()                                                             
                        supervis[u]=p
                        
                        d={u:p}
                        files("supervis.dat",d)
                        popup=tk.Tk()
                        popup.title("Success")
                        tk.Label(master=popup,text="Supervisor Successfully Added!").grid(row=1,column=1)
                    u=usname.get()
                    if u in admin or u in supervis or u in standard:
                            popup=tk.Tk()
                            popup.title("Username Already Exists!")
                            tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                            manageusersc.destroy()
                            aa.destroy()
                    else:        
                        tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                        passw=tk.Entry(master=aa,show='*')
                        passw.grid(row=2,column=1)
                        tk.Button(master=aa,text="Confirm Password",command=superuserback,width=25).grid(row=2,column=3)
                aa=tk.Tk()
                aa.title("Add A Supervisor")
                tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
                usname=tk.Entry(master=aa)
                usname.grid(row=1,column=1)
                a3=tk.Button(master=aa,text="Confirm Username",width=25,command=superusname).grid(row=1,column=3)
            def addstand():
                def standusname():
                    def standuserback():
                        p=passw.get()                                                             
                        standard[u]=p                        
                        d={u:p}
                        files("standard.dat",d)
                        
                        popup=tk.Tk()
                        popup.title("Success")
                        tk.Label(master=popup,text="Standard User Successfully Added!").grid(row=1,column=1)
                    u=usname.get()
                    if u in admin or u in supervis or u in standard:
                            popup=tk.Tk()
                            popup.title("Username Already Exists!")
                            tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                            
                            aa.destroy()
                    else:        
                        tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                        passw=tk.Entry(master=aa,show='*')
                        passw.grid(row=2,column=1)
                        tk.Button(master=aa,text="Confirm Password",command=standuserback,width=25).grid(row=2,column=3)
                aa=tk.Tk()
                aa.title("Add A Standard User")
                tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
                usname=tk.Entry(master=aa)
                usname.grid(row=1,column=1)
                a3=tk.Button(master=aa,text="Confirm Username",width=25,command=standusname).grid(row=1,column=3)
            addusersc=tk.Tk()
            addusersc.title("Add A User")
            tk.Button(master=addusersc,width=25,text="Add An Admin",command=addadmin).grid(row=1,column=1)
            tk.Button(master=addusersc,width=25,text="Add A Supervisor",command=addsuper).grid(row=2,column=1)
            tk.Button(master=addusersc,width=25,text="Add A Standard User",command=addstand).grid(row=3,column=1)
        def viewuser():
            viewsc=tk.Tk()
            viewsc.title("View Users")
            tk.Label(master=viewsc,text="Admins Are:").grid(row=0,column=0)
            c=0
            for i in admin:
                c+=1
                tk.Label(master=viewsc,text=("------",i)).grid(row=c,column=0)
            c+=1
            tk.Label(master=viewsc,text="Supervisors Are:").grid(row=c,column=0)        
            for i in supervis:
                c+=1
                tk.Label(master=viewsc,text=("-----",i)).grid(row=c,column=0)
            c+=1
            tk.Label(master=viewsc,text="Standard Users Are:").grid(row=c,column=0)        
            for i in standard:
                c+=1
                tk.Label(master=viewsc,text=("-----",i)).grid(row=c,column=0)
        def deluser():
            def deluserback():
                u=uname.get()
                if not(u in admin or u in supervis or u in standard):
                    popup=tk.Tk()
                    popup.title("Username Not Found!")
                    tk.Label(master=popup,text="Username not found! Please try again!").grid(row=1,column=1)
                else:
                    if u in admin:
                        del admin[u]
                        delfiles("admin.dat",{u:""})
                        r1=tk.Tk()
                        r1.title("Success!")
                        tk.Label(master=r1,text="Admin User Successfully Deleted!").grid(row=1,column=1)
                        delusersc.destroy()
                    elif u in supervis:
                        del supervis[u]
                        delfiles("supervis.dat",{u:""})
                        r1=tk.Tk()
                        r1.title("Success!")
                        tk.Label(master=r1,text=" Supervisor Successfully Deleted!").grid(row=1,column=1)
                        delusersc.destroy()
                    if u in standard:
                        del standard[u]
                        delfiles("standard.dat",{u:""})
                        r1=tk.Tk()
                        r1.title("Success!")
                        tk.Label(master=r1,text="Standard User Successfully Deleted!").grid(row=1,column=1)
                        delusersc.destroy()
            delusersc=tk.Tk()
            delusersc.title("Delete A User")
            tk.Label(master=delusersc,text="Enter the Username").grid(row=1,column=0)
            uname=tk.Entry(master=delusersc)
            uname.grid(row=1,column=1)
            r2=tk.Button(master=delusersc,text="Confirm Deletion",width=25,command=deluserback).grid(row=1,column=2)                
        manageusersc=tk.Tk()
        manageusersc.title("Manage Users")
        tk.Button(master=manageusersc,text="Add Users",width=25,command=adduser).grid(row=1,column=0)
        tk.Button(master=manageusersc,text="Delete A User",width=25,command=deluser).grid(row=2,column=0)
        tk.Button(master=manageusersc,text="View Current Users",width=25,command=viewuser).grid(row=3,column=0)
    def update():
        updatesc=tk.Tk()     
        updatesc.title("Update/Add A Flight")    
        tk.Label(master=updatesc,text="Enter The Flight Number").grid(row=1,column=0)
        flightnum=tk.Entry(master=updatesc)
        flightnum.grid(row=1,column=1)   
        def updatebutton1():
            tk.Label(master=updatesc,text="Enter Departure Time").grid(row=3,column=0)
            deptime=tk.Entry(master=updatesc)
            deptime.grid(row=3,column=1)
            tk.Label(master=updatesc,text="Enter ETA").grid(row=4,column=0)
            eta=tk.Entry(master=updatesc)
            eta.grid(row=4,column=1)
            tk.Label(master=updatesc,text='FROM:').grid(row=5,column=0)
            n=tk.StringVar()
            location=ttk.Combobox(master=updatesc,textvariable=n)
            location['values']=('DELHI','BANGALORE','CHENNAI','MUMBAI','KOLKATA')
            location.grid(row=5,column=1)
            tk.Label(master=updatesc,text='TO:').grid(row=6,column=0)
            n1=tk.StringVar()
            destination=ttk.Combobox(master=updatesc,textvariable=n1)
            destination['values']=('DELHI','BANGALORE','CHENNAI','MUMBAI','KOLKATA')
            destination.grid(row=6,column=1)
            tk.Label(master=updatesc,text="Enter Status").grid(row=7,column=0)
            status=tk.Entry(master=updatesc)
            status.grid(row=7,column=1)
            tk.Label(master=updatesc,text="Enter Airline").grid(row=8,column=0)
            airline=tk.Entry(master=updatesc)
            airline.grid(row=8,column=1)
            
            def updatebutton2():       
                if deptime.get()!="" and status.get()!="" and destination.get()!="" and location.get()!="" and eta.get()!="" and airline.get()!="" and destination.get()!=location.get():
                    for i in flights:
                        if flightnum.get().lower()==i:
                            xl=[deptime.get(),destination.get().lower(),status.get().lower(),eta.get(),location.get().lower(),airline.get().lower(),flights[i][-1]]
                            flights[flightnum.get().lower()]=xl
                    else:
                        xl=[deptime.get(),destination.get().lower(),status.get().lower(),eta.get(),location.get().lower(),airline.get().lower(),{}]
                        flights[flightnum.get().lower()]=xl
                    d={flightnum.get().lower():xl}
                    files("flights.dat",d)
                    updatepopup=tk.Tk()
                    tk.Label(master=updatepopup,text="Successfully Updated!!").grid(row=0,column=0)
                    updatesc.destroy()
                else:
                    if destination.get()==location.get():
                        updateerrorpopup=tk.Tk()
                        tk.Label(master=updateerrorpopup,text="Location And Destination Cannot Be Same!").grid(row=0,column=0)
                    else:
                        updateerrorpopup=tk.Tk()
                        tk.Label(master=updateerrorpopup,text="All Fields Are Compulsory!").grid(row=0,column=0)
                        
                        
            tk.Button(master=updatesc,text="Confirm",command=updatebutton2).grid(row=9,column=1)   
        tk.Button(master=updatesc,text="Confirm",command=updatebutton1).grid(row=2,column=1)
        updatesc.mainloop()
        
    def cancel():
        def cancelback():
            t=flightnum.get().lower()
            cancelsc.destroy()        
            if t in cancelled:
                re=tk.Tk()
                re.title("Already Cancelled!")
                tk.Label(master=re,text="Flight Already Cancelled. Please try again!").grid(row=1,column=1)
                cancel()
            elif not(t in flights):
                re=tk.Tk()
                re.title("Flight Not Found!")
                tk.Label(master=re,text="Flight Not Found. Please try again!").grid(row=1,column=1)
                cancel()
            else:
                t1=flights.pop(t)
                t1[2]="cancelled"
                cancelled[t]=t1
                d={t:t1}
                files("cancelled.dat",d)
                delfiles("flights.dat",d)
                
                re=tk.Tk()
                re.title("Success!")
                tk.Label(master=re,text="Flight Successfully Cancelled!").grid(row=1,column=1)           
        cancelsc=tk.Tk()
        cancelsc.title("Cancel a Flight")
        tk.Label(master=cancelsc,text="Enter the flight number").grid(row=1,column=0)
        flightnum=tk.Entry(master=cancelsc)
        flightnum.grid(row=1,column=1)
        t7=tk.Button(master=cancelsc,width=25,text="Confirm",command=cancelback).grid(row=2,column=1)
    def viewpassenger():
        viewpassengersc=tk.Tk()
        viewpassengersc.title("View Passenger Details")
        tk.Label(viewpassengersc,text="Flight Number       Passenger Name        Passenger Phone Number").grid(row=1,column=0)
        c=1
        for i in flights:
            g=flights[i][-1]            
            for j in g:
                c+=1
                p=str(i)+"          "+passengerlist[j]+"              "+j
                tk.Label(viewpassengersc,text=p).grid(row=c,column=0)
    def admain():
        def switchuserad():
            admainsc.destroy()
            login()
        admainsc=tk.Tk()
        admainsc.title("Admin Control Panel")    
        tk.Button(master=admainsc,text="View The Details Of Flights",command=view).grid(row=1,column=1)
        tk.Button(master=admainsc,text="Switch User",command=switchuserad).grid(row=2,column=1)
        tk.Button(master=admainsc,text="Cancel A Flight",command=cancel).grid(row=4,column=1)
        tk.Button(master=admainsc,text="Manage Users",command=manageuser).grid(row=5,column=1)
        tk.Button(master=admainsc,text="Exit The Program",command=exit).grid(row=8,column=1)
        tk.Button(master=admainsc,text="Update/Add A Flight",command=update).grid(row=3,column=1)
        tk.Button(master=admainsc,text="View Passengers on Flights",command=viewpassenger).grid(row=6,column=1)
        tk.Button(master=admainsc,text="Return To Main Screen",command=partial(returntomain,admainsc)).grid(row=7,column=1)
        
    def supmain():
        def switchusersup():
            supmainsc.destroy()
            login()
        supmainsc=tk.Tk()
        supmainsc.title("Supervisor Control Panel")
        tk.Label(master=supmainsc,text="").grid(row=6,column=0)    
        tk.Button(master=supmainsc,text="View The Details Of Flights",command=view).grid(row=1,column=1)
        tk.Button(master=supmainsc,text="Switch User",command=switchusersup).grid(row=2,column=1)
        tk.Button(master=supmainsc,text="Cancel A Flight",command=cancel).grid(row=4,column=1)
        tk.Button(master=supmainsc,text="View Passengers on Flights",command=viewpassenger).grid(row=5,column=1)
        tk.Button(master=supmainsc,text="Exit The Program",command=exit).grid(row=6,column=1)
        tk.Button(master=supmainsc,text="Update/Add A Flight",command=update).grid(row=3,column=1)
        tk.Button(master=supmainsc,text="Return To Main Screen",command=partial(returntomain,supmainsc)).grid(row=7,column=1)
        supmainsc.mainloop()
        
    def switchuserstand():
        stamainsc.destroy()
        login()
    def view():
        c=0
        r=1
        view=tk.Tk()
        tk.Label(master=view,text="FLIGHT NUMBER----------DEPARTURE----------DESTINATION---------STATUS").grid(row=1,column=0)
        for i in flights:
            c+=1
            r+=1
            tk.Label(master=view,text=(i.upper(),"-------",flights[i][0],"--------",flights[i][1].upper(),"--------",flights[i][2].upper())).grid(row=r,column=0)
        for i in cancelled:
            c+=1
            r+=1
            tk.Label(master=view,text=(i.upper(),"-------",cancelled[i][0],"--------",cancelled[i][1].upper(),"--------",cancelled[i][2].upper())).grid(row=r,column=0)
         
    def stamain():
        def switchuserstand():
            stamainsc.destroy()
            login()
        stamainsc=tk.Tk()
        stamainsc.title("Standard User Control Panel")
        tk.Button(master=stamainsc,text="View The Details Of Flights",command=view).grid(row=2,column=0)
        tk.Button(master=stamainsc,text="Switch User",command=switchuserstand).grid(row=3,column=0)
        tk.Button(master=stamainsc,text="Exit The Program",command=exit).grid(row=6,column=0)
        tk.Button(master=stamainsc,text="View Passengers on Flights",command=viewpassenger).grid(row=4,column=0)
        tk.Button(master=stamainsc,text="Return To Main Screen",command=partial(returntomain,stamainsc)).grid(row=5,column=0)
        img=tk.PhotoImage(file="ActualLogo.png")
        rp=tk.Label(master=stamainsc,image=img).grid(row=1,column=0)   
        stamainsc.mainloop()        
    def login():
        def userver():        
            def passver():
                b=password.get()
                if check==1:
                    if admin[a]==b:
                        loginsc.destroy()
                        reminder()
                        admain()                    
                    else:
                        a3=tk.Tk()
                        tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)          
                        
                elif check==2:
                    if supervis[a]==b:
                        loginsc.destroy()
                        reminder()                    
                        supmain()                    
                    else:
                        a3=tk.Tk()
                        tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)
                elif check==3:
                    if standard[a]==b:
                        loginsc.destroy()
                        stamain()
                        
                    else:
                        a3=tk.Tk()
                        tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)
            a=username.get()
            if not(a in admin or a in supervis or a in standard):
                a1=tk.Tk()
                tk.Label(master=a1,text="Username Not Found. Please Try Again!").grid(row=1,column=1)       
            else:           
                if a in supervis:
                    check=2
                elif a in admin:
                    check=1
                elif a in standard:
                    check=3             
                tk.Label(master=loginsc,text="Enter Your Password").grid(row=2,column=0)
                password=tk.Entry(master=loginsc,show='*')            
                password.grid(row=2,column=1)
                a3=tk.Button(master=loginsc,text="Confirm Password",width=25,command=passver).grid(row=2,column=2)   
        loginsc=tk.Tk()
        loginsc.title("Login")
        tk.Label(master=loginsc,text="").grid(row=5,column=1)
        img1=tk.PhotoImage(file="ActualLogo.png")
        rp=tk.Label(master=loginsc,image=img1).grid(row=0,column=1)
        tk.Label(master=loginsc,text="Enter Your Username").grid(row=1,column=0)
        username=tk.Entry(master=loginsc)
        username.grid(row=1,column=1)
        a22=tk.Button(master=loginsc,text="Confirm Username",width=25,command=userver).grid(row=1,column=2)
        tk.Button(master=loginsc,text="Return to Main Screen",width=25,command=partial(returntomain,loginsc)).grid(row=5,column=0)
        loginsc.mainloop()
    login()
    
'''*********************************************************************************
                             PASSENGER INTERFACE'''

def passenger():
    def returnmain(a):
                a.destroy()
                main()
    mainsc.destroy()
    global c
    c=0
    
    def price():
        global seatsprice
        p=random.random()
        p=p*6000+4000
        p=int(p)
        return str(p)
    
    def seatselection(a):
        global seatslist
        seatslist=[]
        global seatsprice
        seatsprice=0
        global c
        FILENAME = 'Airplane.png'
        global seatselectionsc
        seatselectionsc = tk.Tk()        
        l=list(flights[a][-1].values())        
        booked=[]
        if l!=[]:
            for i in l:                
                for j in i:
                    booked.append(j.lower())
        if len(booked)==12:
            tk.Label(seatselectionsc,text="Sorry! This Flight is Sold Out").grid(row=1,column=0)
            seatselectionsc.title("Sold Out!")
            seatselectionsc.mainloop()
            return
        else:
            flightsc.destroy()
            seatselectionsc.title("Seat Selection")
            canvas = tk.Canvas(master=seatselectionsc, width=500, height=500)
            canvas.pack()
            Tk_img = tk.PhotoImage(file = FILENAME,master=canvas)
            canvas.create_image((300,325),image=Tk_img)
            def a1():
                if "a1" in booked:
                    b="Booked"
                    a1s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=140,y=340)
                else:
                    global c
                    c=price()
                    b="R."+str(c)
                    a1s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"A1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=140,y=340)
                a1win = canvas.create_window(10, 10, anchor='nw', window=a1s)
            def b1():
                if "b1" in booked:
                    b="Booked"
                    b1s = tk.Label(seatselectionsc, text =b, width = 5, height=3, activebackground = "#33B5E5").place(x=190,y=340)
                else:
                    c=price()
                    b="R."+str(c)
                    b1s = tk.Button(seatselectionsc, text =b, command = partial(seatsbooking,"B1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=190,y=340)
                b1win = canvas.create_window(10, 10, anchor='nw', window=b1s)
            def c1():
                if "c1" in booked:
                    b="Booked"
                    c1s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=235,y=340)
                else:
                    c=0
                    c=price()
                    b="R."+str(c)
                    c1s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"C1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=235,y=340)
                c1win = canvas.create_window(10, 10, anchor='nw', window=c1s)
            def d1():
                if "d1" in booked:
                    b="Booked"
                    d1s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=320,y=340)
                else:                    
                    c=price()
                    b="R."+str(c)
                    d1s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"D1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=320,y=340)
                d1win = canvas.create_window(10, 10, anchor='nw', window=d1s)
            def e1():
                if "e1" in booked:
                    b="Booked"
                    e1s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=365,y=340)
                else:
                    c=price()
                    b="R."+str(c)
                    e1s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"E1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=365,y=340)
                e1win = canvas.create_window(10, 10, anchor='nw', window=e1s)
            def f1():
                if "f1" in booked:
                    b="Booked"
                    f1s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=410,y=340)
                else:
                    c=price()
                    b="R."+str(c)
                    f1s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"F1",c), width = 2, height=2, activebackground = "#33B5E5").place(x=410,y=340)
                f1win = canvas.create_window(10, 10, anchor='nw', window=f1s)

            def d2():
                if "d2" in booked:
                    b="Booked"
                    d2s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=320,y=397)
                else:
                    c=price()
                    b="R."+str(c)
                    d2s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"D2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=320,y=395)
                d2win = canvas.create_window(10, 10, anchor='nw', window=d2s)
            def a2():
                if "a2" in booked:
                    b="Booked"
                    a2s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=140,y=395)
                else:
                    c=price()
                    b="R."+str(c)
                    a2s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"A2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=140,y=395)
                a2win = canvas.create_window(10, 10, anchor='nw', window=a2s)
            def b2():
                if "b2" in booked:
                    b="Booked"
                    b2s = tk.Label(seatselectionsc, text =b, width = 5, height=3, activebackground = "#33B5E5").place(x=190,y=400)
                else:
                    c=price()
                    b="R."+str(c)
                    b2s = tk.Button(seatselectionsc, text =b, command = partial(seatsbooking,"B2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=190,y=400)
                b2win = canvas.create_window(10, 10, anchor='nw', window=b2s)
            def c2():
                if "c2" in booked:
                    b="Booked"
                    c2s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=235,y=397)
                else:
                    global c
                    c=price()
                    b="R."+str(c)
                    c2s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"C2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=235,y=395)
                c2win = canvas.create_window(10, 10, anchor='nw', window=c2s)
            def e2():
                if "e2" in booked:
                    b="Booked"
                    e2s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=365,y=395)
                else:
                    c=price()
                    b="R."+str(c)
                    e2s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"E2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=365,y=395)
                e2win = canvas.create_window(10, 10, anchor='nw', window=e2s)
            def f2():
                if "f2" in booked:
                    b="Booked"
                    f2s = tk.Label(seatselectionsc, text = b, width = 5, height=3, activebackground = "#33B5E5").place(x=410,y=395)
                else:
                    c=price()
                    b="R."+str(c)
                    f2s = tk.Button(seatselectionsc, text = b, command = partial(seatsbooking,"F2",c), width = 2, height=2, activebackground = "#33B5E5").place(x=410,y=395)
                f2win = canvas.create_window(10, 10, anchor='nw', window=f2s)
            seats=[a1,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2]
            for i in seats:
                i()    
            tk.Button(seatselectionsc,width=20,text="Continue",command=partial(confirmpop,seatslist,seatsprice,a)).pack()
            seatselectionsc.mainloop()
            
    def seatsbooking(a,n):
        global seatsprice    
        seatssc=tk.Tk()            
        if a in seatslist:
            seatssc.title("Seat already selected!")
            tk.Label(seatssc,text="Seat "+a+" is already selected!").pack()
        else:
            seatssc.title("Seat Successfully Added!")
            temp="Seat "+a+" has been added to your selection"    
            p=tk.Label(seatssc,text=temp)
            seatsprice+=int(n)                
            p.pack()    
            seatslist.append(a)
            
    def confirmpop(a,b,c):            
        global confirmsc
        confirmsc=tk.Tk()
        if a==[]:
            confirmsc.title("Please select atleast one seat!")
            tk.Label(confirmsc,text="Please select atleast one seat!").grid(row=0,column=0)
            confirmsc.mainloop()
            return
        else:
            seatselectionsc.destroy()            
            confirmsc.title("Confirmation")
            tk.Label(confirmsc,text="Your seat(s) have been booked!").pack()
            tk.Label(confirmsc,text="Your total is "+str(seatsprice)).pack()
            tk.Button(confirmsc,text="Continue",command=partial(passengerdetails,a,b,c)).pack()
            confirmsc.mainloop()
            main()
            
    def passengerdetails(a,b,c):
        confirmsc.destroy()
        def ticketscreen(a,b,g):                
            c=name.get()
            d=phno.get()
            passengersc.destroy()
            global ticketsc
            ticketsc=tk.Tk()
            ticketsc.title("TICKET")
            flights[g][-1][d]=a
            files("flights.dat",{g:flights[g]})
            files("passenger.dat",{d:c})
            passengerlist[str(d)]=str(c)            
            files("passenger.dat",{str(d):str(c)})
            tk.Label(ticketsc,text="**********TICKET*********").grid(row=0,column=0)
            tk.Label(ticketsc,text="SNams Booking Serivce").grid(row=1,column=0)
            tk.Label(ticketsc,text="").grid(row=2,column=0)
            tk.Label(ticketsc,text="Passenger Name: "+str(c)).grid(row=3,column=0)
            tk.Label(ticketsc,text="Passenger Phone Number: "+str(d)).grid(row=4,column=0)
            tk.Label(ticketsc,text="Date: "+str(datetime.date.today())).grid(row=5,column=0)
            tk.Label(ticketsc,text="Flight Number: "+str(g).upper()).grid(row=6,column=0)
            tk.Label(ticketsc,text="Departure: "+flights[g][0]).grid(row=7,column=0)
            tk.Label(ticketsc,text="Estimated Time Of Arrival: "+flights[g][3]).grid(row=8,column=0)
            tk.Label(ticketsc,text="Seats Booked: ").grid(row=9,column=0)
            f=10
            for i in a:
                tk.Label(ticketsc,text=i).grid(row=f,column=0)
                f+=1
            tk.Label(ticketsc,text="Total price: "+str(b)).grid(row=f+1,column=0)
            tk.Button(ticketsc,text="Return to Main Screen",command=partial(returnmain,ticketsc)).grid(row=f+2,column=0)
            ticketsc.mainloop()       
        global passengersc  
        passengersc=tk.Tk()
        passengersc.title("Passenger Details")
        global name,phno
        tk.Label(passengersc,text="Passenger Name").grid(row=0,column=0)
        name=tk.Entry(passengersc)
        name.grid(row=0,column=1)
        tk.Label(passengersc,text="Passenger Phone Number").grid(row=1,column=0)
        phno=tk.Entry(passengersc)
        phno.grid(row=1,column=1)          
        tk.Button(passengersc,text="Confirm",command=partial(ticketscreen,a,seatsprice,c)).grid(row=2,column=0)
        passengersc.mainloop()

    def abcd():
        global flightsc
        flightsc=tk.Tk()
        froml=location.get()
        tol=destination.get()
        if froml==tol:
            tk.Label(flightsc,text="From Location and To Location Cannot Be The Same!").grid(row=0,column=0)
            flightsc.title("From and To Locations are Same")
            flightsc.mainloop()
            return
        bookingsc.destroy()        
        newdate=(datetime.datetime.now()+datetime.timedelta(2))
        p=newdate.strftime("%d")+"-"+newdate.strftime("%m")+"-"+newdate.strftime("%y")
        x="All Displayed Flights Are On: "+p
        tk.Label(flightsc,text=x).grid(row=0,column=0)
        flightsc.title("Available Flights")
        tk.Label(master=flightsc,text="AIRLINE         DEPARTURE         ARRIVAL         DURATION         PRICE(ESTIMATED)").grid(row=1,column=0)        
        k=2        
        for i in flights:
            if flights[i][4]==froml.lower() and flights[i][1]==tol.lower():
                str=flights[i][5].upper()+"           "+flights[i][0]+"                 "+flights[i][3]+"               "+ duration(flights[i][0],flights[i][3])+"             "+price()
                tk.Label(master=flightsc,text=str).grid(row=k,column=0)
                tk.Button(master=flightsc,text="Confirm",command=partial(seatselection,i)).grid(row=k,column=1)
                k=k+1
        tk.Button(flightsc,text="Return To Main Screen",command=partial(returnmain,flightsc)).grid(row=k+1,column=0)
    
    def duration(dep,arr):
        d=0
        l=dep.split(":")
        l1=arr.split(":")
        d=(60*int(l1[0])+int(l1[1]))- (60*int(l[0])+int(l[1]))
        hr=d//60
        min=d%60
        return str(hr)+" Hrs  "+str(min)+" Mins"
    global bookingsc    
    bookingsc=tk.Tk()
    bookingsc.title('Book a Flight')
    tk.Label(master=bookingsc,text='FROM:').grid(row=0,column=0)
    n=tk.StringVar()
    location=ttk.Combobox(master=bookingsc,textvariable=n)
    location['values']=('DELHI','BANGALORE','CHENNAI','MUMBAI','KOLKATA')
    location.grid(row=0,column=1)
    tk.Label(master=bookingsc,text='TO:').grid(row=1,column=0)
    n1=tk.StringVar()
    destination=ttk.Combobox(master=bookingsc,textvariable=n1)
    destination['values']=('DELHI','BANGALORE','CHENNAI','MUMBAI','KOLKATA')
    destination.grid(row=1,column=1)
    tk.Button(master=bookingsc,text="Confirm",command=abcd).grid(row=2,column=1)
    tk.Button(master=bookingsc,text="Return To Main Screen",command=partial(returnmain,bookingsc)).grid(row=3,column=0)
    
def main():
    global mainsc
    mainsc=tk.Tk()
    mainsc.title("Home")
    tk.Button(master=mainsc,text="AIRPORT MANAGEMENT",command=airport).grid(row=0,column=0)
    tk.Button(master=mainsc,text="PASSENGER INTERFACE",command=passenger).grid(row=1,column=0)

def files(filename,d):
    f1=open(filename,"rb")
    try:
        l=[]
        flag=0
        while True:
            filerecord=pickle.load(f1)
            if filerecord.keys()==d.keys():
                flag=1
                l.append(d)
            else:
                l.append(filerecord)
    except EOFError:
        if flag==0:
            l.append(d)
        f1.close()
    f2=open(filename,"wb")
    for i in l:
        pickle.dump(i,f2)
    f2.close()
    
def delfiles(filename,d):
    f3=open(filename,"rb")
    try:
        l=[]
        while True:
            filerecord=pickle.load(f3)
            if filerecord.keys()!=d.keys():
                l.append(filerecord)
    except EOFError:
        f3.close()
    f4=open(filename,"wb")
    for i in l:
        pickle.dump(i,f4)
    f4.close()
main()
                

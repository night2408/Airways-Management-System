import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="root",database="Airways_Management")
cursor=con.cursor()
import random
import csv

def Adm_login():
    Adm_ID=int(input("Enter your ID:"))
    Adm_pswd=int(input("Enter your password:"))
    e="select * from Admin where Admin_ID={} and Password={}".format(Adm_ID,Adm_pswd)
    cursor.execute(e)
    data=cursor.fetchall()
    count=cursor.rowcount
    while count==0:
        print("Invalid ID/Password")
        print()
        Adm_ID=int(input("Enter your ID:"))
        Adm_pswd=int(input("Enter your password"))
        e="select * from Admin where Admin_ID={} and Password={}".format(Adm_ID,Adm_pswd)
        cursor.execute(e)
        data=cursor.fetchall()
        count=cursor.rowcount
    else:
        print()
        print("!!!Logged in Successfully!!!")
        
def adm_change():
    print()
    print("What do you want to do?\n"," 1.Create Employee ID\n"," 2.Delete Employee ID\n")
    ch=int(input("Enter your choice:"))
    if ch==1:
        Emp_new()
        change_runagain1()
    if ch==2:
        Emp_delete()
        change_runagain1()
    
def Emp_login():
    Emp_name=input("Enter your name:")
    Emp_pswd=input("Enter a your password:")
    Empl_ID=int(input("Enter your ID:"))
    e="select * from employee where Emp_ID={} and Name='{}'and Password='{}'".format(Empl_ID, Emp_name, Emp_pswd)
    cursor.execute(e)
    data=cursor.fetchall()
    count=cursor.rowcount
    while count==0:
        print("Invalid ID/Name/Password")
        print()
        Emp_name=input("Enter your name")
        Emp_ID=int(input("Enter your ID"))
        Emp_pswd=int(input("Enter your password"))
        e="select * from employee where Emp_ID={} and Name='{}' and Password='{}'".format(Emp_ID, Emp_name, Emp_pswd)
        cursor.execute(e)
        data=cursor.fetchall()
        count=cursor.rowcount
    else:
        print()
        print("!!!Logged in Successfully!!!")
        print()       

def Emp_new():
    Emp_newname=input("Enter Employee name:")
    Emp_newpswd=input("Enter a strong password:")
    Emp_newID= random.randint(100,1000)
    b="select Emp_ID from employee where Emp_ID={}".format(Emp_newID)
    cursor.execute(b)
    data=cursor.fetchall()
    count=cursor.rowcount
    if count==0:
        print("Employee ID is:",Emp_newID)
        e="insert into employee(Emp_ID, Name, Password) values ({},'{}','{}')".format(Emp_newID,Emp_newname,Emp_newpswd)
        cursor.execute(e)
        con.commit()
        print()
        print( "!!!ID has been created!!!" )
        print()
    else:
        while count!=0:
            Emp_newID= random.randint(100,1000)
            b="select Emp_ID from employee where Emp_ID={}".format(Emp_newID)
            cursor.execute(b)
            data=cursor.fetchall()
            count=cursor.rowcount
        if count==0:
            print("Your Employee ID is:",Emp_newID)
            e="insert into employee(Emp_ID, Name, Password) values ({},'{}','{}')".format(Emp_newID,Emp_newname,Emp_newpswd)
            cursor.execute(e)
            con.commit()
            print( "!!!ID has been created!!!" )
            print()
            
def Emp_delete():
    print()
    print("The current Employees are:")
    print()
    print("Emp_ID"," Employee Name","Password")
    p="select * from employee"
    cursor.execute(p)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
    Emp_del=int(input("Enter the ID of Employee you want to delete:"))
    st="delete from employee where Emp_ID={}".format(Emp_del)
    cursor.execute(st)
    con.commit()
    print()
    print("!!!Employee ID Deleted Successfuly!!!")
    print()
    print("The new Employee table:")
    print()
    print("Emp_ID"," Employee Name","Password")
    b="select * from employee"
    cursor.execute(b)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
            
def Cus_login():
    Cus_name=input("Enter your name:")
    Cus_pswd=input("Enter a your password:")
    Cust_ID=int(input("Enter your ID:"))
    e="select * from customer1 where Cus_ID={} and Name='{}'and Password='{}'".format(Cust_ID, Cus_name, Cus_pswd)
    cursor.execute(e)
    data=cursor.fetchall()
    count=cursor.rowcount
    while count==0:
        print("Invalid ID/Name/Password")
        print()
        Cus_name=input("Enter your name")
        Cus_ID=int(input("Enter your ID"))
        Cus_pswd=int(input("Enter your password"))
        e="select * from customer1 where Cus_ID={} and Name='{}' and Password='{}'".format(Cust_ID, Cus_name, Cus_pswd)
        cursor.execute(e)
        data=cursor.fetchall()
        return Cus_name
    else:
        print()
        print("!!!Logged in Successfully!!!")
        print()
        print("Your Ticket Details are:")
        print()
        return Cus_name

def Cus_new():
    Cus_newname=input("Enter your name:")
    Cus_newpswd=input("Enter a strong password:")
    Cus_newID=random.randint(100,1000)
    b="select Cus_ID from customer1 where Cus_ID={}".format(Cus_newID)
    cursor.execute(b)
    data=cursor.fetchall()
    count=cursor.rowcount
    if count==0:
        print("Your Passenger ID is:",Cus_newID)
        e="insert into customer1(Cus_ID, Name, Password) values ({},'{}','{}')".format(Cus_newID,Cus_newname,Cus_newpswd)
        cursor.execute(e)
        con.commit()
        print( "!!!ID has been created!!!" )
        print()
        print("Please enter your details to book ticket:")
    else:
        while count!=0:
            print()
            print("This ID is already taken make a new one")
            print()
            Cus_newID=random.randint(100,1000)
            b="select Cus_ID from customer1 where Cus_ID={}".format(Cus_newID)
            cursor.execute(b)
            data=cursor.fetchall()
            count=cursor.rowcount
        if count==0:
            print("Your Passenger ID is:",Cus_newID)
            e="insert into customer1(Cus_ID, Name, Password) values ({},'{}','{}')".format(Cus_newID,Cus_newname,Cus_newpswd)
            cursor.execute(e)
            con.commit()
            print( "!!!ID has been created!!!" )
            print()
            print("Please enter your details to book ticket:")

def Change_table():
    print("What do you want to do?")
    print()
    print(" 1.View Passenger Info\n","2.Insert new snack\n", "3.Delete a snack\n", "4.Delete Passenger Data/Account") 
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Details of Passengers:")
        print()
        print( "     Name", "     Phoneno","   Pasprt.no"," Jr.date  "," Departure   "," Destination")  
        z="select * from passen_data"
        cursor.execute(z)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        change_runagain()    
    if ch==2:
        print()
        print("The current Snacks are:")
        print()
        print("Snack,Price")
        p="select * from snack"
        cursor.execute(p)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        snackname=input("Enter the new snack:")
        price=int(input("Enter the price:"))
        st="insert into snack(snack_name, price)values('{}',{})".format(snackname,price)
        cursor.execute(st)
        con.commit()
        print()
        print("The new Snack table:")
        b="select * from snack"
        cursor.execute(b)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        change_runagain()
    if ch==3:
        print()
        print("The current Snacks are:")
        print()
        print("Snack,Price")
        p="select * from snack"
        cursor.execute(p)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        snack_name=input("Enter the name of snack you want to delete")
        st="delete from snack where snack_name='{}'".format(snack_name)
        cursor.execute(st)
        con.commit()
        print()
        print("The new Snack table:")
        b="select * from snack"
        cursor.execute(b)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        change_runagain()
    if ch==4:
        print()
        print("The details of passenger are:")
        print()
        print( "       Name", "       Phoneno","  Pass_no","  Jr_date","  Departure","  Destination")  
        z="select * from passen_data"
        cursor.execute(z)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        print()
        delete_pas=input("Enter the name of the Passenger you want to delete:")
        st="delete from passen_data where Passenger_name='{}'".format(delete_pas)
        cursor.execute(st)
        con.commit()
        print()
        print("!!!Passenger Data deleted Succesfully!!!")
        print()
        print("Passenger data:")
        print()
        print( "       Name", "       Phoneno","  Pass_no","  Jr_date","  Departure","  Destination") 
        b="select * from passen_data"
        cursor.execute(b)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        change_runagain()
                
def Cus_info():
    name=input("Enter your name:")
    phno=int(input("Enter your phone no."))
    passno=int(input("Enter your passport no.:"))
    jrdate=input("Enter date of journey(dd/mm/yyy):")
    print("Please select your depature and destination from the following:")
    f = open("places.txt", "r")
    print(f.read())
    depart=input("Enter departure place:")
    destination=input("Enter your destination:")
    sql="insert into passen_data(Passenger_name, Passenger_ph, Passenger_passportno, jr_date, departure_place, destination)values('{}',{},{},'{}','{}','{}')".format(name,phno,passno,jrdate,depart,destination)
    cursor.execute(sql)
    data=cursor.fetchall()
    con.commit()
    print()
    print("!!!Data added Sucessfully!!!")
    print()

def pas_tic():
    q="select * from passen_data where Passenger_name='{}' ".format(Cus_login())
    cursor.execute(q)
    data=cursor.fetchall()
    for row in data:
         print("Name: ", row[0])
         print("Phone number: ", row[1])
         print("Passport: ", row[2])
         print("Journey Date: ", row[3])
         print("Departure Place: ", row[4])
         print("Destination: ", row[5])

def Pass_ticketinfo():
    pas_tic()
    runagin()

def change_date():
    pas_tic()
    print()
    print("~~Enter your name and new date~~")
    print()
    Passenger_name=input("Enter your name:")
    jr_date=input("Enter the new journey date(dd/mm/yyyy):")
    st="update passen_data set jr_date='{}' where Passenger_name='{}'".format(jr_date,Passenger_name)
    cursor.execute(st)
    con.commit()
    print()
    print("Enter your name/id/password again to see the new ticket:")
    pas_tic()
    runagin()

def pas_ticket():
    print("What do you want to do?\n"," 1.View your ticket details\n"," 2.Reschulde your Flight\n")
    y=int(input("Enter your choice:"))
    if y==1:
        Pass_ticketinfo()
    elif y==2:
        change_date()
        
def change_runagain():
    print()
    print("Press 'c' to countinue and 'm' to return back to main menu:")
    ch=input("Enter your choice:")
    if ch=='c' or ch=='C':
        Change_table()
    elif ch=='m' or ch=='M':
        start()
        
def change_runagain1():
    print()
    print("Press 'c' to countinue and 'm' to return back to main menu:")
    ch=input("Enter your choice:")
    if ch=='c' or ch=='C':
        adm_change()
    elif ch=='m' or ch=='M':
        start()

def runagin():
    print()
    print("Press 'c' to countinue and 'm' to return back to main menu:")
    ch=input("Enter your choice:")
    if ch=='c' or ch=='C':
        pas_ticket()
    elif ch=='m' or ch=='M':
        start()

def runagain1():
    print()
    print("Press 'c' to countinue and 'm' to return back to main menu:")
    ch=input("Enter your choice:")
    if ch=='c' or ch=='C':
        review()
    elif ch=='m' or ch=='M':
        start()
        
def review():
    print("What do you want to do?\n"," 1.Write a Review\n"," 2.Read Reviews\n")
    a=int(input("Enter your choice:"))
    if a==1:
        print()
        writereview()
        runagain1()
    elif a==2:
        print()
        readreview()
        runagain1()
        
def writereview():
    data=""
    with open("review","w") as f1:
        infile=csv.writer(f1)
        infile.writerow(["Name","Review","Ratings","Suggestions"])
        Name=input("Enter your Name:")
        Review=input("Please write your review:")
        Ratings=int(input("Give ratings out of 5:"))
        Suggestions=input("Please give us your suggestions to make Indian Airways even better:")
        data=Name,Review,Ratings,Suggestions
        with open("review.csv","a") as f1:
            infile=csv.writer(f1)
            infile.writerow(data)

def readreview():
    print("[ Name ]","[Review]","[Rt]","[Sugges]")
    with open('review.csv','r') as f:
        outfile=csv.reader(f)
        for row in outfile:
            if row!=[]:
                print(row) 
        
def ext():
    print("~~~~Thank You~~~~")
    
def extra_baggage():
    print()
    w=input("Do you want to add more kgs to your baggage allowance?(yes/no)")
    if w=='yes' or w=='Yes':
        print()
        print("Per kg extra 300Rs")
        print()
        r=int(input("How many more kgs do you want to add to your baggage allowance?"))
        extra_baggage_q=r*300
        print()
        print("Total charge for extra baggage is",extra_baggage_q)
        return extra_baggage_q
    elif w=='no' or w=='No':
        print()
        print("*****No Extra baggage added*****")
        return 0
    
list=[]
def snacks():
    print("Choose your snacks:")
    sql="select * from snack"
    cursor.execute(sql)
    rows=cursor.fetchall()
    for x in rows:
        print(x)
    i=input("Enter the name of your snack:")
    j=int(input("Enter quantity:"))
    m="select price from snack where snack_name='{}'".format(i)
    cursor.execute(m)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        cost=float(row[0])
        z=cost*j
        list.append(z)
    snacks.a=sum(list)
    print()
    print("The cost of your snack is:",snacks.a)
    
h=[]
def start():
    f = open("welcome.txt", "r")
    print(f.read())
    print("what do you want to do?\n"," 1. Admin Login\n"," 2. Employee Login\n"," 3. Passenger Login\n"," 4. Create new Passenger ID\n"," 5. Review\n"," 6. Exit\n")
    ch=int(input("Enter your choice:"))
    if ch==1:
        Adm_login()
        adm_change()
    elif ch==2:
        Emp_login()
        Change_table()
    elif ch==3:
        print("What do you want to do?\n"," 1.View your ticket details\n"," 2.Reschulde your Flight\n")
        y=int(input("Enter your choice:"))
        if y==1:
            Pass_ticketinfo()
        elif y==2:
            change_date()
    elif ch==4:
        Cus_new()
        Cus_info()
        print()
        print("Choose your class:")
        sql="select * from classtype"
        cursor.execute(sql)
        rows=cursor.fetchall()
        for x in rows:
            print(x)
        ch=int(input("Enter your choice:"))
        if ch==1:
            print()
            print("you have opted for Firstclass\n","Your maximum baggage allowance is 45kg and hand bag 10kg\n")
            s=45000
            h.append(extra_baggage())
        elif ch==2:
            print()
            print("you have opted for Businessclass\n""Your maximum baggage allowance is 35kg and hand bag 7kg\n")
            s=24000
            h.append(extra_baggage())
        elif ch==3:
            print()
            print("you have opted for Economy\n""Your maximum baggage allowance is 30kg and hand bag 5kg\n")
            s=18000
            h.append(extra_baggage())
        print()
        k=input("Do you want to have snacks?(yes/no)")
        if k=='yes' or k=='Yes':
            snacks()
        elif k=='no' or k=='No':
            print("*****You have selected no snacks*****")
            snacks.a=0
        h.append(s)
        h.append(snacks.a)
        k=sum(h)
        #print(k)
        print("Thank you for booking from our Airlines Your total cost would be:",k)
        print()
        f = open("thankyou.txt", "r")
        print(f.read())
        start()
    elif ch==5:
        print()
        review()
    elif ch==6:
        ext()
start()











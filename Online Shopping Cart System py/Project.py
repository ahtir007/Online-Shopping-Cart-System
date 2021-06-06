##import datetime
##date_object = datetime.date.today()
##print(date_object)
from tkinter import *
from tkinter import ttk
list1=[]
global itemlist
class user:
    def __init__(self):
        self.user=""
        self.password=""

    def verify_login(self,name,passs):
        file=open("1234.txt",'r')
        for i in file:
            z=i.split()
            if name in z:
                if passs in z:
                    return True       
    def verify_login_2(self,name,passs):
        file=open("admin.txt",'r')
        for i in file:
            z=i.split()
            if name in z:
                if passs in z:
                    return True       


class admisnistration(user):
    def __init__(self):
        super().__init__()
                                        #Assosication happening

    def remove_item(self,objitem):
        for num,_2dlist in enumerate(itemlist):
               if (r_name.get()) in itemlist[num]:
                   itemlist.pop(num)
        remove()            
    def add_item(self,objitem):
        global itemlist
        objitem.item_name_quantity.append([a_name.get(),"$",int(a_price.get()),"Quantity",a_quantity.get()])
        itemlist=objitem.item_name_quantity
        print(itemlist)

class customer(user):
    def __init__(self,customername,address,email,credit_card,Productname,cost,customer_name):
        super().__init__()
        self.custname=customername
        self.address=address                                              #Composition happening
        self.email=email
        self.credit_card=credit_card
        self.objshoppingcart=Shopping_cart(Productname,cost,customer_name)
      
    def register(self,name,passs):
        self.user=name
        self.passs=passs
        file=open("1234.txt",'r')
        count=0
        for i in file:
            count=1+count
        file.close()     
        if count==0:
            file=open("1234.txt",'a')
            file.write(f"{self.user}\t{self.passs}")
            file.close()
        else:
            file=open("1234.txt",'a')
            file.write(f"\n{self.user}\t{self.passs}")
            file.close()
     
    def login(self,name,password):
        
        a=super().verify_login(name,password)
        userinfowindow(a)
            
    def update_password(self,name,password):
            update=[]
            original_list=[]
            backup_list=[]
            f = open("1234.txt",'r')
            filedata = f.readlines()
            for i in filedata:
                z=list(i.split())
                original_list.append(z)
            backup_list=original_list
            for i in original_list:
               if name in i:
                   update.append(i)
                   update[0][1]=password

            finalize_file(backup_list,update)        



        
class Shopping_cart:
    def __init__(self,Productname,cost,customer_name):
        self.Productname=Productname
        self.cost=cost
        self._order=order(customer_name)

    def additem(self,objitem):
        global list1                                      #Aggregation happeining 
        self.itemlist=objitem.item_name_quantity
        
        if var1.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[0][0],self.itemlist[0][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])
            
        if var2.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[1][0],self.itemlist[1][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])
        if var3.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[2][0],self.itemlist[2][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])

        if var4.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[3][0],self.itemlist[3][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])
                        
        if var5.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[4][0],self.itemlist[4][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])
            
        if var6.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[5][0],self.itemlist[5][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])
            
        if var7.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[6][0],self.itemlist[6][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])

        if var8.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[8][0],self.itemlist[7][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])   

        if var9.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[8][0],self.itemlist[8][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])         
        if var10.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[9][0],self.itemlist[9][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])    
        if var11.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[10][0],self.itemlist[10][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])    
        if var12.get()==1:
            objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),self.itemlist[11][0],self.itemlist[11][2],user_name_full.get())
            list1.append([objcustomer.objshoppingcart.Productname,objcustomer.objshoppingcart.cost])    

    def display(self):
       costt=0
       objorder=order("")
       
       ma=Tk()
       ma.geometry("535x400")
       ma.title("Online Shopping")
       heading=Label(ma,text="Cart").pack()
       heading_2=Label(ma,text=("Dear",user_name_full.get())).pack()
       heading_3=Label(ma,text="Your cart").pack()
       for i in list1:
           costt=int(i[1])+costt
           a=Label(ma,text=(repr(i))).pack()
       heading_6=Label(ma,text=("--------------------------------------")).pack()
       heading_5=Label(ma,text=("Shipping Type:",objorder.type_ship)).pack()
       heading_7=Label(ma,text="Total cost").pack()
       heading_4=Label(ma,text=str(costt)).pack()
       heading_8=Label(ma,text="Free Shipping").pack()
       clear__=Button(ma,text="Clear cart",command=clear_list).pack()
       clear__=Button(ma,text="Place Order",command=place_order).pack()
       ma.mainloop()

class order:
    def __init__(self,customer_name):
        self.customer_name=customer_name
        self.type_ship="Cash on Delivery(only available at the moment)"

    def placeorder(self):
       ma=Tk()
       ma.geometry("535x400")
       ma.title("Online Shopping")
       msg=Label(ma,text="Order Place").pack()
       objcustomer=customer(user_name_full.get(),user_address_f.get(),email.get(),credit_card.get(),"","","")
       msg=Label(ma,text=("Dear,",objcustomer.custname)).pack()
       order_placed=Label(ma,text=("Your order is shipped to:",objcustomer.address)).pack()
       order_placed=Label(ma,text=("Tracking ID is emailed to:",objcustomer.email)).pack()
       order_placed=Label(ma,text=("If you have any questions regarding your Order")).pack()
       order_placed=Label(ma,text=("Contact us at:","+923086960696")).pack()
       ma.mainloop()                   

class item:
    def __init__(self):
     self.item_name_quantity=[['Apple','$',int(2.50),"Quantity",20],["Orange","$",int(6.20),"Quantity",20],["Smart 4k TV","$",899,"Quantity",20],
                              ["Mango","$",int(1.5),"Quantity",20],["Smart Watch","$",int(250),"Quantity",20],["Apple(america)","$",299,"Quantity",20],["Samsung s10","$",1100,"Quantity",20]]
def remove():
    k=Toplevel()
    k.title("Online Shopping")
    z=Label(k,text="Removed").pack()
    k.mainloop() 
def admin_add():
    objitem=item()
    objadminn=admisnistration()
    objadminn.add_item(objitem)
    added()
def admin_remove():
    objitem=item()
    objadminn=admisnistration()
    objadminn.remove_item(objitem)
                                                                                                                                             
                                                                                                                                              

def adminstrator_window():
       global a_name,a_price,a_quantity,r_name
       maa=Tk()
       a_name=StringVar(maa)
       a_price=IntVar(maa)
       a_quantity=IntVar(maa)
       r_name=StringVar(maa)
       maa.geometry("535x400")
       maa.title("DataBase")
       dd=Label(maa,text="DataBase").pack()
       for i in itemlist: 
          item_database=Label(maa,text=(repr(i))).pack()
       magg=Label(maa,text="Entry to Database").place(x=10,y=180)
       mag=Label(maa,text="Enter product name").place(x=10,y=210)
       maggg=Entry(maa,textvariable=a_name).place(x=120,y=210)
       msg=Label(maa,text="Enter price").place(x=10,y=240)
       m1=Entry(maa,textvariable=a_price).place(x=75,y=240)
       m2=Label(maa,text="Quantity").place(x=10,y=270)
       m3=Entry(maa,textvariable=a_quantity).place(x=70,y=270)
       add=Button(maa,text="Enter",command=admin_add).place(x=50,y=300)
       
       magg=Label(maa,text="Remove from Database").place(x=350,y=180)
       mag=Label(maa,text="Enter product name").place(x=300,y=210)
       maggg=Entry(maa,textvariable=r_name).place(x=410,y=210)
       remove=Button(maa,text="Enter",command=admin_remove).place(x=400,y=250)
       maa.mainloop()
def adminstrator_login_verify():
     objadmin=admisnistration()
     objadmin.user=admin_username.get()
     objadmin.password=admin_password.get()
     a=objadmin.verify_login_2(objadmin.user,objadmin.password)
     if a!=True:
          main=Toplevel()
          z=Label(main,text="Wrong username or password").pack()
     else:
         adminstrator_window()
def adminstrator_login():
    global admin_username,admin_password
    main=Toplevel()
    main.geometry("535x300")
    main.title("Online Shopping")
    heading=Label(main,text="Online Shopping").pack()
    admin_username=StringVar(main)
    admin_password=StringVar(main)

    login_label=Label(main,text="Admistrator Login-In").place(x=190,y=95)
    admistrator_name=Label(main,text="Name").place(x=150,y=120)
    admistrator_username=Entry(main,textvariable=admin_username).place(x=190,y=120)
    admistrator_pass=Label(main,text="Password").place(x=150,y=150)
    admistrator_password=Entry(main,show="*",textvariable=admin_password).place(x=205,y=150)
    adminstrator=Button(main,text="Login",command=adminstrator_login_verify).place(x=200,y=200)
    

def place_order():
    objorder=order("")   # goes in order class to run placeorder function
    objorder.placeorder()
    
    
def clear_list():
    list1.clear()      #cleans the cart


def displaycart():
    objcart=Shopping_cart("","","")
    objcart.display()       #displays the cart and goes in shopping cart class


def add_item():
    
    obj=Shopping_cart("","","")
    objitem=item()                  #add items to cart and also shows cart window
    obj.additem(objitem)
    #added()
    displaycart()

def shoppingcart():
    #global user_name_full,user_address_f,email,credit_card,var1,var2,var3,var4,var5,var6,var7
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,itemlist
    main=Tk()
    main.geometry("535x300")                            #this window displays the menu what stuff is available 
    main.title("Online Shopping")
    heading=Label(main,text="Shopping Menu").pack()
    var1 = IntVar(main)
    var2 = IntVar(main)
    var3 = IntVar(main)
    var4 = IntVar(main)
    var5 = IntVar(main)
    var6 = IntVar(main)
    var7 = IntVar(main)
    var8 = IntVar(main)
    var9 = IntVar(main)
    var10 = IntVar(main)
    var11 = IntVar(main)
    var12 = IntVar(main)
    count=0
    #obj=item()
    heading=Label(main,text="Item available").pack()
    for i in itemlist:
     count1="var"   
     count+=1
     count1=count1+str(count)
     variable_name=eval(count1)
     a=Checkbutton(main, text=(i[0],"$",str(i[2])),variable=variable_name).pack()    


    z=Button(main,text="Enter",command=add_item).place(x=250,y=240)
    main.mainloop()

def userinfowindow(a):
          
        if a!=True:
          main=Toplevel()
          z=Label(main,text="Wrong username or password").pack()       #takes information regarding user for shipping
        else:
          global user_name_full,user_address_f,email,credit_card,namee
          m=Tk()
          m.geometry("535x300")
          m.title("Online Shopping")
          z=Label(m,text="Enter Your information for delievery").pack()

          user_full_name=Label(m,text='Full name')
          user_full_name.place(x=40,y=50)
          user_name_full=ttk.Entry(m)
          user_name_full.place(x=100,y=50)

          user_address=Label(m,text='Address')
          user_address.place(x=40,y=80)
          user_address_f=ttk.Entry(m)
          user_address_f.place(x=100,y=80)

          user_email=Label(m,text='Email')
          user_email.place(x=40,y=110)
          email=ttk.Entry(m)
          email.place(x=100,y=110)
          
          user_credit_no=Label(m,text='Credit Card No')
          user_credit_no.place(x=40,y=140)
          credit_card=ttk.Entry(m)
          credit_card.place(x=122,y=140)
          
          information_enter=Button(m,text="Enter",command=shoppingcart).place(x=200,y=200)
          update_password=Button(m,text="Press to update password",command=password_update).place(x=200,y=230)
          namee=user_name_full.get()
          m.mainloop()


def added():
    k=Toplevel()
    k.title("Online Shopping")
    z=Label(k,text="Added").pack()
    k.mainloop()

    
def userman_password_enter():
    name=t_name.get()                                 #check if the login Id are right or wrong by going in child customer,parent user 
    password=t_password.get()
    obj=customer("","","","","","","")
    obj.login(name,password)
    del obj
           
##-----------------------------------------------------------------------------------------------------------------------------------------
## This is the coding for the changing password    
            
def finalize_file(backup_list,update):
    for num,line in enumerate(backup_list):
        for line in line:
            if line==update[0]:
                backup_list[num]=update
    f=open("1234.txt","w")            #Store changed password code
    for i in backup_list:
         if i!=[]: 
             a=i[0]
             b=i[1]
             f.write(f"\n{a}\t{b}")
         
def updated():                                
    l=Tk()
    l=Label(l,text="Updated!").pack()

def password_update():
    global u_name,u_password

    

    p=Tk()
    u_name=StringVar(p)
    u_password=StringVar(p)                                             #This code for taking existing user and password
    pp=Label(p,text="Enter username").pack()
    pp=Entry(p,textvariable=u_name).pack()                          
    ppp=Label(p,text="Enter Password").pack()
    pppp=Entry(p,textvariable=u_password).pack()
    enter=Button(p,text="Enter",command=send_data).pack()
    p.mainloop()
def send_data_2():
        objcustomer=customer("","","","","","","")                      #Goes in customer class to run update password function
        objcustomer.update_password(u_name.get(),c_password.get())
        updated()
def send_data():

    objuser=user()    
    a=objuser.verify_login(u_name.get(),u_password.get())
    if a!=True:
          main=Toplevel()
          z=Label(main,text="Wrong username or password").pack()          ##This checks if entered pass or username is wrong if correct
          main.mainloop()                                                 ## then it starts the process of changing password
    else:
        global c_password
        man=Toplevel()
        c_password=StringVar()
        m=Label(man,text="Enter new password").pack()
        mm=Entry(man,textvariable=c_password).pack()
        mmm=Button(man,text="Enter",command=send_data_2).pack()
        man.mainloop()
##---------------------------------------------------------------------------------------------------------------------------------------------------        
def done_reg():                                        #Message for new registered user
            main=Toplevel()
            main.title("Online Shopping")
            z=Label(main,text="Registered!").pack()



def new_register():
                                                                     #This is for registration for new user
        main=Toplevel()         
        main.geometry("535x300")
        main.title("Online Shopping")
        heading=Label(main,text="Registration for new user").pack()
        
        a=Label(main,text='Name').place(x=150,y=120)
        t_name=StringVar(main)
        t_password=StringVar(main)
        usernamecust=Entry(main,textvariable=t_name).place(x=190,y=120)

        b=Label(main,text='Password').place(x=150,y=150)
        userpasswordcust=Entry(main,textvariable=t_password).place(x=205,y=150)

        enter_existing_user=Button(main,text="Enter",command=done_reg).place(x=200,y=200)    

        main.mainloop()
        name=t_name.get()
        password=t_password.get()
        

        obj=customer("","","","","","","")
        obj.register(name,password)
        
##-----------------------------------------------------------------------------------------------------------------------------------------------        
##GUI MainWindow

main=Tk()
main.geometry("535x300")
main.title("Online Shopping")
heading=Label(main,text="Online Shopping").pack()
login_label=Label(main,text="Customer Sign in").place(x=210,y=95)
a=Label(main,text='Name').place(x=150,y=120)
t_name=StringVar()
t_password=StringVar()
##admin_username=StringVar()
##admin_password=StringVar()
usernamecust=Entry(main,textvariable=t_name).place(x=190,y=120)

b=Label(text='Password').place(x=150,y=150)
userpasswordcust=Entry(main,show="*",textvariable=t_password).place(x=205,y=150)

enter_existing_user=Button(main,text="Enter",command=userman_password_enter).place(x=200,y=200)

button=Button(main,text="New register",command=new_register).place(x=40,y=200)

##login_label=Label(main,text="Admistrator Login-In").place(x=390,y=95)
##admistrator_name=Label(main,text="Name").place(x=350,y=120)
##admistrator_username=Entry(main,textvariable=admin_username).place(x=390,y=120)
##admistrator_pass=Label(main,text="Password").place(x=345,y=150)
##admistrator_password=Entry(main,textvariable=admin_password).place(x=400,y=150)
adminstrator=Button(main,text="Administrator Login",command=adminstrator_login).place(x=400,y=200)

#-------------
objitem=item()
itemlist=[]
itemlist=objitem.item_name_quantity

del objitem


#adminstrator_window()        



            


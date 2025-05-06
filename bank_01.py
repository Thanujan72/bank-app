import random

create_customer={}

intial_balance=1000

def login(): 
    correct_admin_name="Thanu"
    correct_admin_password="123456"
    # def register():
    # Name=input("Enter Name:")
    # Adderss=input("Enter Adderss:")
    # username=input("Enter user Name:")
    # usser_Password=input("Enter passowrd:")   

    while True:
        admin_name=input("Enter Name:")
        admin_password=input("Enter Password:")
        
        if correct_admin_name==admin_name and correct_admin_password==admin_password:
            # if Name==admin_name and user_passowrd==admin_password:
            print("login successful!")
            return admin()
                    
        else:
            print("Try agin")
#  def login_menu():

#     while True:
#         print("======")             



def create_customer():
    customer_Name="Kannan"
    customer_password="123456"
    customer_NIC="123654v"
    customer_ID=str(random.randint(1001,1010))
 
    while True :
        
        print("customer_ID:",customer_ID)
        Customer_Name=input("Enter customer Name:")
        customer_password=input("Enter customer password:")
        customer_NIC=input("Enter customer NIC:")
        
        if customer_Name== Customer_Name and customer_password==customer_password and customer_NIC==customer_NIC:
            print("Wel come Customer")

            print("*****************************")
            return admin()
            
        else:
            print("Sorry  your input invalid")

with open("customer.txt",'w') as bank_01:
    bank_01.write("Name \t adderss \t  ")
       
def admin():

    while True:
        print("=========ADMIN_MENU=========")
        print("1.create_customer")
        print("2.EXIT")
        choice=input("ENTER YOUR CHOICE : ")

        if choice=="1":
            create_customer()
        elif choice=="2":
            print("Thank you")
            print("*****************************")
            return bank_menu()
        else:
            print("your choice invalid")



def create_account():
    global intial_balance
    acc_no=1001
    acc_password="123456"
    holder_name="Kannan"
    
    while True:
        Acc_No=int(input("Enter your account number : "))
        AccPassword=(input("Enter your password :  "))
        Holder_Name=str(input("Enter your Name : "))
        
        if acc_no==Acc_No and acc_password==AccPassword and holder_name==Holder_Name:
            print("Wel come ")

            print("**********************************")

            return  bank_menu()
        

            
   
          
            
def bank_menu():
    
    while True:
        print("=====BANK MENU======")
        print("1.create account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Check Blance")
        print("5.Transaction History")
        print("6.Exit")
        choice=input("enter your choice(1-6):")
        
        if choice =="1":
            create_account() 
            
        elif choice=="2":
            Deposit_Money()          

        elif choice=="3":
            pass          
        elif choice=="4":
            pass           
        elif choice=="5":
            break     
        elif choice=="6":
            print("********* Thank you***********")

def deposit_Money():
    deposit+=intial_balance
    print("deposit")


                    

login()
# register()
# bank_menu()
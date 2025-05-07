import random
Customer_Details = {}
Account_Details={}
intial_balance = 1000


def login(): 
    correct_admin_name="Admin"
    correct_admin_password="Admin@123"
    

    while True:
        admin_name=input("Enter Name:")
        admin_password=input("Enter Password:")
        
        if correct_admin_name == admin_name and correct_admin_password == admin_password:
            print("login successful!")
            admin()
            print()
                    
        else:
            print("Try agin")


print("****************************************************************")


# def create_customer():
#     while True :
#         Customer_Name=input("Enter customer Name:")
#         customer_password=input("Enter customer password:")
#         customer_NIC=input("Enter customer NIC:")
#         customer_ID = random.randint(1001,1010)

#         print(f"Your customer id is :", customer_ID)

#         Customer_Details = { "Name":Customer_Name,
#                             "Password":customer_password,
#                             "NIC":customer_NIC,
                            
#                             }


#         with open("Customer_Details.txt",'a') as bank_01:
#             bank_01.write(f"{Customer_Name} \t {customer_password} \t {customer_NIC} \t {customer_ID}  \n")

#         return admin()


def create_customer():
    while True:
        Customer_Name = input("Enter customer Name:")
        customer_password = input("Enter customer password:")
        customer_NIC = input("Enter customer NIC:")
        customer_ID = random.randint(1001, 1010)

        print(f"Your customer id is: {customer_ID}")
        
        Customer_Details = {
            "Name": Customer_Name,
            "Password": customer_password,
            "NIC": customer_NIC,
            "ID": customer_ID
        }

        with open("Customer_Details.txt", 'a') as bank_01:
            bank_01.write(f"{Customer_Name} \t {customer_password} \t {customer_NIC} \t {customer_ID}  \n")

        # Return to admin() function or continue
        return admin()

            
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
   
    
    while True:
        
        Holder_Name=str(input("Enter your Name : "))
        acc_Password=(input("Enter your password :  "))
        user_NIC=int(input("Enter your NIC number :"))
        Acc_No=random.randint(1111111111,9999999999999)

        # Account_Details={"Name" : Holder_Name,
        #                  "Password" :acc_Password,
        #                   "NIC" : user_NIC 
        #                   }

        if Holder_Name == Customer_Details["Name"] :
       
            with open("acc_Details.txt",'a') as bank_01:
                        bank_01.write(f"{ Holder_Name} \t { acc_Password} \t {user_NIC} \t { Acc_No}  \n")
            return  bank_menu()

    


           
       
        
def  show_balance():
    global intial_balance
    print(f"Your balance is $ :{intial_balance}")

    print("*****************************")
            
def deposit_Money():
    global intial_balance
    Amount = int(input("Enter Your Ammount :"))

    if Amount > 0:
        intial_balance += Amount
        
        print(f"Your Deposit Money $ :{intial_balance}")
        # return Amount

        
       # return 0
    else:
        print("That is not valid ")

def Withdraw_Money():
    global intial_balance
    Amount=int(input("Enter your Amount :"))

    if Amount<intial_balance:
        intial_balance -= Amount 
                
        print(f"Your Withdraw money $ :{intial_balance:}")
    else:
        print("That's not vailid Ammount ")


def check_balance():
    print(f"Your balance is $ :")



def Transaction_History():
    pass
#    import datetime

# x = datetime.datetime.now()

# print(x)

        
          
            
def bank_menu():
    
    while True:
        print()
        print("=====BANK MENU======")
        print("1.create account")
        print("2.show intial_balance")
        print("3.Deposit Money")
        print("4.Withdraw Money")
        print("5.Check Blance")
        print("6.Transaction History")
        print("7.Exit")
        choice=input("enter your choice(1-6):")
        
        if choice =="1":
            create_account() 
            
        elif choice=="2":
            show_balance()         

        elif choice=="3":
            deposit_Money()
                  
        elif choice=="4":
           Withdraw_Money()  

        elif choice=="5":
            print(f"Your balance is $ :{intial_balance}")
    

        elif choice=="6":
           Transaction_History()
           
        else:
            print("Thank you for banking With use")

                    

login()


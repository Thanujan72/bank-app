import random
import os

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





import os

def get_customer_info():
    # Get customer information
    name = input("Enter your Name: ")
    address = input("Enter Your Address: ")
    username = input("Enter Your username: ") 
    password = input("Enter Your password: ")  
   
    return [name, address, username, password] 

def customer_next_id():
    if not os.path.exists("Customer_Details.txt"):
        return "C001"
    else:
        with open("Customer_Details.txt", 'r') as bank_01:
            lines = bank_01.readlines()
            if not lines:
                return "C001"
            last_line = lines[-1].strip() 
           
            last_id = last_line.split("|")[0].strip()

            if last_id.startswith("C"):
                try:
                   
                    next_id_num = int(last_id[1:]) + 1
                    return f"C{next_id_num:03d}" 
                except ValueError:
                    return "C001"
            else:
                return "C001"

def create_customer():
    
    customer = get_customer_info()  
   
    next_id = customer_next_id()  

   
    with open("Customer_Details.txt", 'a') as bank_01, open("users.txt", 'a') as user_file:
        
        bank_01.write(f"{next_id} | {customer[0]} | {customer[1]}\n")
       
        user_file.write(f"{customer[2]} | {customer[3]}\n")

    print(f"Customer {next_id} has been created successfully!")


    
    return admin()

def admin():
    while True:
        print("=========ADMIN_MENU=========")
        print("1. Create Customer")
        print("2. EXIT")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            print("Thank you")
            print("*****************************")
            return bank_menu()  
        else:
            print("Your choice is invalid. Please try again.")

def get_create_account():
    Holder_Name = str(input("Enter your Holder_Name: "))
    acc_Password = input("Enter your acc_Password: ")
    user_NIC = int(input("Enter your NIC number: "))
    Tele_phone = int(input("Enter your TELE_Number: "))
    Acc_No = random.randint(1000000000, 9999999999)  
    
    return [Holder_Name, acc_Password, user_NIC, Tele_phone, Acc_No]

def create_account():
    account = get_create_account()
    with open("acc_Details.txt", 'a') as acc_file:
        acc_file.write(f"{account[0]} | {account[1]} | {account[2]} | {account[3]} | {account[4]}\n")


        
def  show_balance():
    global intial_balance
    print(f"Your balance is $ :{intial_balance}")

    print("*****************************")
            
def deposit_Money():
    global intial_balance
    global Acc_No
    Amount = int(input("Enter Your Ammount :"))

    if Amount > 0:
        intial_balance += Amount
        
        print(f"Your Deposit Money $ :{intial_balance}")
        print("your deposited sacussfully")

        with open("transaction_history.txt", "a") as transaction_file :
            transaction_file.write({Acc_No}, {Amount})
    
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
    with open("transaction_history.txt",'r') as transaction_file:
        print(transaction_file.readlines())




    

        
        
            
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
        
        elif choice=="7":
            print()
            print("********************************************")
            print("Thank you for banking With use!")
        else:
            print("your choice invalid")

            print("****************************************")
                        

login()



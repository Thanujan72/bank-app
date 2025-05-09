def get_customer_info():
    name=input("Enter your Name: ")
    adderss=input("Enter Your Address: ")
    username=input("Enter Your username: ") 
    password=input("Enter Your password: ")  

   
    return  [name,adderss,username,password] 
     
def customer_next_id():
    if  not os.path.exists("Customer_Details.txt"):
        return "C001"
    else:
        with open("Customer_Details.txt", 'r') as bank_01:
            return f"C{int(bank_01.readlines()[-1].split(",")[0][1:])+1:03d}"
                
def create_customer():
    customer=get_customer_info()
    next_id=customer_next_id()
    with open("Customer_Details.txt", 'a') as bank_01,open ("users.txt,",'a')as user_file:
        bank_01.write(f" {next_id} | {customer[0]} | {customer[1]}\n ")
        user_file.write(f"{customer[2]} | {customer[3]}\n")
    print(customer)
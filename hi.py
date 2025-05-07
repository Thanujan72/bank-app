Customer_Details = {
    "Name": Customer_Name,
    "Password": customer_password,
    "NIC": customer_NIC,
    "ID": customer_ID
}


account_Details = {
    "Name": "John Doe",
    "Password": "pass123",
    "NIC": "123456789V",
    "ID": "ID001"
}

if account_Details == Customer_Details:
    print("Account verified.")
else:
    print("Details do not match.")
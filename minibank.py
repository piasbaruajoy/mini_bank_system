#এইটা একটা ছোট ব্যাংক সিস্টেম
#
#
#
#নিচে কিছু ডাটা সেমপ্ল নিলাম।
from datetime import date
from colorama import Fore,Style
bank_customer_details=[
    {
        "account_number":101,
        "name":"MD.Rohim",
        "age":30,
        "city":"Chittagong",
        "account_type":"Current Account",
        "current_amount":5000,
        "account_opening_date":"2024/05/21"
    },
    {
        "account_number":102,
        "name":"MD.Sakib",
        "age":25,
        "city":"Chittagong",
        "account_type":"Current Account",
        "current_amount":20000,
        "account_opening_date":"2023/05/15"
    },
    {   "account_number":103,
        "name":" Pranto ",
        "age":32,
        "city":"Chittagong",
        "account_type":"Current Account",
        "current_amount":200000,
        "account_opening_date":"2023/05/15"
    }
]
ok=False
admin_name="123"
admin_pass="123"
current_date = date.today()
def heading_blue():
    print(Fore.LIGHTBLUE_EX+"+==============================================================+")
    print("|                       H4X3R B4Nk        |",current_date,"|       |")
    print("+==============================================================+")
def heading_red():
    print(Fore.LIGHTRED_EX+"+==============================================================+")
    print("|                       H4X3R B4Nk        |",current_date,"|       |")
    print("+==============================================================+")
def heading_green():
    print(Fore.LIGHTGREEN_EX+"+==============================================================+")
    print("|                       H4X3R B4Nk        |",current_date,"|       |")
    print("+==============================================================+")
def heading_yellow():
    print(Fore.LIGHTYELLOW_EX+"+==============================================================+")
    print("|                       H4X3R B4Nk        |",current_date,"|       |")
    print("+==============================================================+")
#add new customer in the database
def add_new_cutomer():
    heading_red()
    user_name=input("Account Holder Name:")
    user_acc_number=int(input("Account number:"))
    for x in bank_customer_details:
        if(x["account_number"]==user_acc_number):
            print("Account Number allredy exsist please enter new one")
            user_acc_number=int(input("Account number:"))
        else:
            break
    user_age=int(input("Account Holder Age:"))
    user_location=input("Account Holder Location:")
    user_account_type=input("Account Type:")
    user_account_start=input("Account openning Date:")
    user_account_balance=int(input("Opening balance:"))
    new_user={
        "account_number":user_acc_number,
        "name":user_name,
        "age":user_age,
        "city":user_location,
        "account_type":user_account_type,
        "current_amount":user_account_balance,
        "account_opening_date":user_account_start
    }
    bank_customer_details.append(new_user)
#Show all user in the bank
def customer_details_display():
    print()
    print(Fore.LIGHTBLUE_EX+"+==============================================================+")
    print("|----------------------Customer Details---------",current_date,"---|")
    print("+==============================================================+")
    print(Fore.YELLOW+"|-----Name------|---AGE---|--Account_type--|--Current_balance--|")
    print("+==============================================================+")
    for x in bank_customer_details:
        print(Fore.LIGHTGREEN_EX + f"| {x['name']:<13} | {x['age']:^8} | {x['account_type']:<10} | {x['current_amount']:>14,.2f} |")
    print(Fore.YELLOW+"+==============================================================+",end=Style.RESET_ALL)
#search by Account number
def serch_acc_number():
    heading_yellow()
    print("|                        Searching :....                       |")
    print("+==============================================================+")
    search_data=int(input("|         Enter Account Number:"))
    print("+==============================================================+")
    print(Fore.YELLOW+"|-----Name------|---AGE---|--Account_type--|--Current_balance--|")
    print("+==============================================================+")
    found=False
    for account in bank_customer_details:
        if (account["account_number"]== search_data):
            print(Fore.LIGHTGREEN_EX + f"| {account['name']:<13} | {account['age']:^8} | {account['account_type']:<10} | {account['current_amount']:>14,.2f} |")
            print("+=============================================================+")
            found=True
            break
    if not found:
        print(Fore.RED+"Account ", search_data, "not found.")
def search():
    print("|                        Searching :....                       |")
    print("+==============================================================+")
    search_data=int(input("|         Enter Account Number:"))
    print(Fore.YELLOW+"+==============================================================+")
    print(Fore.YELLOW+"|-----Name------|---AGE---|--Account_type--|--Current_balance--|")
    print("+==============================================================+")
    found=False
    for account in bank_customer_details:
        if (account["account_number"]== search_data):
            print(Fore.LIGHTGREEN_EX + f"| {account['name']:<13} | {account['age']:^8} | {account['account_type']:<10} | {account['current_amount']:>14,.2f} |")
            print("+=============================================================+")
            found=True
            break
    if not found:
        print(Fore.RED+"Account ", search_data, "not found.")


#Deposit Money
def deposit_money():
    heading_green()
    acc_name=input("|    Enter Account Name:")
    acc_number=int(input("|    Enter Account Number:"))
    for data in bank_customer_details:
        if(data["account_number"]==acc_number and data["name"]==acc_name):
            deposit=int(input("|    how much money want to deposit:"))
            print("+==============================================================+")
            print(f"|           Current balance:{data['current_amount']}                             |")
            print("+==============================================================+")
            print("+-------------------After Depositing --------------------------+")
            data["current_amount"]=data["current_amount"]+deposit
            print(Fore.YELLOW+"+==============================================================+")
            print(Fore.YELLOW+"|-----Name------|---AGE---|--Account_type--|--Current_balance--|")
            print("+==============================================================+")
            print(Fore.LIGHTGREEN_EX + f"| {data['name']:<13} | {data['age']:^8} | {data['account_type']:<10} | {data['current_amount']:>14,.2f} |")
            print("+==============================================================+")
# 
# 
# Money Withdrow
def Money_withdrow():
    heading_red()
    acc_name=input("|    Enter Account Name:")
    acc_number=int(input("|    Enter Account Number:"))
    for data in bank_customer_details:
        if(data["account_number"]==acc_number and data["name"]==acc_name):
            withdrow=int(input("|    how much money want to withdrow:"))
            print("+==============================================================+")
            print(f"|           Current balance:{data['current_amount']}                             |")
            print("+==============================================================+")
            print("+-------------------After Withdrowing --------------------------+")
            data["current_amount"]=data["current_amount"]-withdrow
            print(Fore.YELLOW+"+==============================================================+")
            print(Fore.YELLOW+"|-----Name------|---AGE---|--Account_type--|--Current_balance--|")
            print("+==============================================================+")
            print(Fore.LIGHTGREEN_EX + f"| {data['name']:<13} | {data['age']:^8} | {data['account_type']:<10} | {data['current_amount']:>14,.2f} |")
            print("+==============================================================+")


#
#right now creating Menu 
#1. নতুন গ্রাহক যোগ করুন
#2. সব গ্রাহকের তথ্য দেখুন
#3. একাউন্ট নম্বর দিয়ে খুঁজুন
#4. টাকা জমা দিন
#5. টাকা উত্তোলন করুন
#6. প্রস্থান করুন
def system_start():
    while ok!=True:
        heading_blue()
        print("1.Add New Customer")
        print("2.All Customer details")
        print("3.serch by account number")
        print("4.Deposit Money")
        print("5.Withdraw Money")
        print("6.Exit()")
        action=int(input("Enter your chose:"))
        if(action==1):
            add_new_cutomer()
        elif(action==2):
            customer_details_display()
        elif(action==3):
            serch_acc_number()
        elif(action==4):
            deposit_money()
        elif(action==5):
            Money_withdrow()
        elif(action==6):
            exit()
        else:
            print("try again")
        #print(Fore.LIGHTMAGENTA_EX+"==============================================================")
        print()
        print() 
while ok!=True:
    account_user=input("Enter user Name:")
    account_pass=(input("Enter user Pass:"))
    if(account_user==admin_name and account_pass==admin_pass):
        system_start()
        ok=True
    else:
        print("Try again")
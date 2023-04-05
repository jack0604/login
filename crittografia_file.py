import os
def crittografia():
    while True:
        os.system('clear')
        os.system('figlet Crittografia')
        password = ""
        passwd = input("enter password --------> ")
        if passwd == password:
            os.system('clear')
            print("ok perfetto")
            
        else:
            os.system('clear')
            print("Password errata")
            exit
crittografia()
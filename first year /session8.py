proman = {
    "name1": "Prorootman",
    "password1": "root",

    "name2": "Proadmin",
    "password2": "admin",

    "name3": "Prouser",
    "password3": "user",
}

def login():

    name = input("enter your name: ")
    password = input("enter your passord: ")

    if (name == proman["name1"] and password == proman["password1"]):
        print("welcome, prorootman")

    elif (name == proman["name2"] and password == proman["password2"]):
        print("welcome, proadmin")

    elif (name == proman["name3"] and password == proman["password3"]):
        print("welcome, prouser")

    else:
        print("username or pass wrong")


login()




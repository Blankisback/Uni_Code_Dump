print("welcome to my chatbot")
months = ["january","february","march","april","may","june","july","august","september","october","november","december"]

name = input("enter your name: ")
surname = input("enter your surname: ")
monthbday = int(input("what month is your birthday (as a number): "))


print("hello {} {} ".format(name,surname))

if monthbday < 0:
    print("not a valid number:")
else:
    monthbday -= 1 
    realmonth = (months[monthbday])
    print("hello {}, your birthday is in {} ".format(name,realmonth))

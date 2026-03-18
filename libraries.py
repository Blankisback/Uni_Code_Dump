from datetime import datetime

dob = input("enter your birthday dd/mm/yyyy: ")

day, month, year = dob.split("/")

birthdate = datetime(int(year), int(month), int(day))

now = datetime.now()

dif = now - birthdate

totaldays =  dif.days
totalhours = int(dif.total_seconds() // 3600)
totalmin = int(dif.total_seconds() // 60)

print("you have lived {} days, {} hours, {} minutes.".format(totaldays,totalhours,totalmin))

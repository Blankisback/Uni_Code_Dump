import datetime

filename = "log.txt"

f = open(filename, "at")

print("file: {} opened".format(filename))

userstuff = input("Enter something to write to the file: ")

f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ":" + userstuff + "\n")
f.close()

f = open(filename, "r")

for x in f:
    print(x)

f.close
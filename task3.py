print("Miles to Kilometers (1)")
print("Kilometers to Miles (2)")
print("Convert Cm to Inches (3)")
print("Convert Inches to Cm (4)")

choice = int(input("which do you want to pick: "))
measurement = int(input("enter the measurement to convert: "))


def mtokm(measurement):
    mile = 1.609 #km
    return(measurement * mile)
    

def kmtom(measurement):
    km = 0.62137119
    return(km * measurement)

def cmtoin(measurement):
    cm = 2.54 #1 inch 
    return(cm * measurement)

def intocm(measurement):
    inch = 2.54 # 1 cm
    return(inch * measurement)


if choice == 1:
    print("{} miles to km is {}  km".format(measurement,mtokm(measurement)))

elif choice == 2:
    print("{} km to miles is {} miles".format(measurement,kmtom(measurement)))

elif choice == 3:
    print("{} cm to inches is {} inches".format(measurement,cmtoin(measurement)))

elif choice == 4:
    print("{} inches to cm is {} cm".format(measurement,intocm(measurement)))

else:
    print("out of range")



concerts = ["Ed Sheeran 1", "Taylor Swift", "Adele", "Madonna", "Rihanna"]

ticket = 0
found = False
name = ""
concertChoice = ""
ticketCost = 0


def setName():
    
    print("Please enter your name: ")
    userName = input()
    global name
    name = userName



def chooseConcert():

    print("Please choose a concert: ")
    print("---")

    for i in concerts:
        print(i)

    print("---")

        
    print("Concert Choice: ")
    userConcertChoice = input()

    global concertChoice

    concertChoice = userConcertChoice

def checkConcert():
    global found
    global concerts
    global concertsChoice
    
    for i in concerts:
        if i == concertChoice:
            found = True
            
def getConcert():
    chooseConcert()

    checkConcert()


def getTicketType():
    print("Ticket Type (Adult, Child, Student)")
    ticketType = input()
    return ticketType


def getPriceByType(ticketType):
    ticketPrice = 0
    
    if ticketType == "Adult":
        ticketPrice = 10
    elif ticketType == "Child":
        ticketPrice = 5
    elif ticketType == "Student":
        ticketPrice = 7
    
    return ticketPrice


def getTicketQuantity():
    print("How many tickets do you want to buy?")
    amount = int(input())
    return amount


def getTicketCost():
    global ticketCost
    
    ticketType = getTicketType()
    ticketPrice = getPriceByType(ticketType)
    amount = getTicketQuantity()
    
    ticketCost = ticketPrice * amount
		

def printTicket():
    global name
    global concertChoice
    global ticketCost
    global found
    
    if found:
        
        print("--- Printing Ticket ---")
        print("Ticket holder: " + name)
        print("Concert: " + concertChoice)
        print("Total ticket(s) price: £" + str(ticketCost))
    else:
        print("Concert not found")

    print("Thank you for using the Concert Ticket System")

 
# Main program to get Concert Tickets.

print("--- Welcome to the Concert booking system ---")

setName()

getConcert ()

getTicketCost()

printTicket()
    



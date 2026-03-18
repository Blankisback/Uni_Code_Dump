#Flight Ticket Program 2025

flights = ["London to Amsterdam", "Amsterdam to London", "London to Edinburgh", "Edinburgh to London", "London to Paris", "Paris to London"]

ticket = 0
found = False
name = ""
flightChoice = ""
ticketCost = 0


def setName():
    
    print("Please enter your name: ")
    userName = input()
    global name
    name = userName



def chooseFlight():

    print("Please choose a flight: ")
    print("---")

    for i in flights:
        print(i)

    print("---")

        
    print("Flight Choice: ")
    userFlightChoice = input()

    global flightChoice

    flightChoice = userFlightChoice

    


def checkFlight():
    global found
    global flights
    global flightChoice
    
    for i in flights:
        if i == flightChoice:
            found = True
            


def getTicketCost():

    global ticketCost
    ticketPrice = 0
    ticketType = ""
	
    print("Ticket Type (Adult, Child, Student)")
    ticketType = input()
	
    if ticketType == "Adult":
        ticketPrice = 50
		
    if ticketType == "Child":
        ticketPrice = 30
		
    if ticketType == "Student":
        ticketPrice = 40
	
    print("How many tickets do you want to buy?")

    amount = int(input())
        
    ticketCost = ticketPrice * amount
		


def printTicket():
    global name
    global flightChoice
    global ticketCost
    global found
    
    if found:
        
        print("--- Printing Ticket ---")
        print("Ticket holder: " + name)
        print("Flight: " + flightChoice)
        print("Ticket(s) Price: £" + str(ticketCost))
    else:
        print("Flight not found")

 


print("--- Welcome to the Flight booking system ---")

setName()

chooseFlight()
checkFlight()

getTicketCost()
printTicket()

print("Thank you for using the Flight Ticket System")
    

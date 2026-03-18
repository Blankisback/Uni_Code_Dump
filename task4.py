
concerts = ["Ed Sheeran 1", "Taylor Swift", "Adele", "Madonna", "Rihanna"]
ticket = 0
found = False
name = ""
concertChoice = ""
ticketCost = 0

# HIGH COHESION has a single use to get the users name
def setName():
    print("Please enter your name: ")
    userName = input()
    global name  # HIGH COUPLING: Uses global variable, creates dependency
    name = userName

# HIGH COHESION: Single responsibility - display concerts and get user choicek
def chooseConcert():
    print("Please choose a concert: ")
    print("---")
    for i in concerts:  # TIGHT COUPLING: Depends on global concerts list
        print(i)
    print("---")
    print("Concert Choice: ")
    userConcertChoice = input()
    global concertChoice  # TIGHT COUPLING: Uses global variable
    concertChoice = userConcertChoice

# HIGH COHESION: Single responsibility - validate concert choice
def checkConcert():
    global found  # TIGHT COUPLING: Multiple global dependencies
    global concerts
    global concertChoice
    for i in concerts:
        if i == concertChoice:
            found = True

# MODERATE COHESION: Combines two related operations (choose + check)
# TIGHT COUPLING: Depends on chooseConcert() and checkConcert() functions
def getConcert():
    chooseConcert()
    checkConcert()

# HIGH COHESION: Single responsibility - calculate ticket cost
def getTicketCost():
    global ticketCost  # TIGHT COUPLING: Uses global variable
    ticketPrice = 0
    ticketType = ""
    print("Ticket Type (Adult, Child, Student)")
    ticketType = input()
    if ticketType == "Adult":
        ticketPrice = 10
    if ticketType == "Child":
        ticketPrice = 5
    if ticketType == "Student":
        ticketPrice = 7
    print("How many tickets do you want to buy?")
    amount = int(input())
    ticketCost = ticketPrice * amount

# HIGH COHESION: Single responsibility - display ticket information
def printTicket():
    global name  # TIGHT COUPLING: Depends on multiple global variables
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

# Main program to get Concert Tickets
# TIGHT COUPLING: All functions are tightly coupled through global variables
print("--- Welcome to the Concert booking system ---")
setName()
getConcert()
getTicketCost()
printTicket()
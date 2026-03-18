def long_date(date="01012000"):
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:8])

    if year < 1:
        print("invalid date")

    if month < 1 or month > 12:
        print("valid date")

    days_in_month = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

    months = ["jan", "feb", "mar", "apr", "may", "jun","jul", "aug", "sep", "oct", "nov", "dec"]


    if day < 1 or day > days_in_month[month - 1]:
        print("invalid date")

    print(f"{day} {months[month - 1]} {year}")
    print("this is a valid date")



date_input = input("Enter date (ddmmyyyy): ")
print(long_date(date_input))

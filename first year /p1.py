def aifunction():

    print("welcome to the chatbot")

    again = True
    while again == True:

        text = input("enter text: ")
        if text == "hi" or "hello":
            print("hello i hope your having a good day")
        elif text == "how are you" or "hru":
            print("i am good wbu")
        elif text == "how old are you":
            print("i was jus born")
        else:
            print("idk")

        again = input("do you wanna play again: ")
        if again == "yes":
                again == True
        else:
            print("bye")
            break

aifunction()
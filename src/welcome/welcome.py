
running = True
activateDebugSequence = True
print("Welcome the Python3.11 Interactive Code Testing")


def banner() -> str:
    return "Hi!"


banner()
print()


# def debug_sequence(i="y", a="y") -> None:
#    if i != "y":
#        if a != "y":
#            debug = False
#        elif a == "y":
#            debug = True
#   if activateDebugSequence and input("Would you like to activate debug mode? [y/N]: ").lower() == "y":
#        debug = True


# debug_sequence()
def Session1() -> None:
    print("This is session 1")


while running:

    try:
        Session_Ask = 1
        if Session_Ask == 1:
            running = False
            Session1()
        elif Session_Ask > 1:
            raise NotImplementedError
    except ValueError:
        print("Not a valid number. Please try Again.")
    finally:
        print("Thank you for using PyCode Testing! Have a nice day!")

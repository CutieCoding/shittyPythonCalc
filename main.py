import functions
from functions import *

userList = []

def main(): #interface
    operation = input("a, s, m, d: ")
    if operation == "a": #uses an if statement bcs theres only like 5 different things it can do
        add1()
        main()
    elif operation == "s":
        sub1()
        main()
    elif operation == "m":
        mul1()
        main()
    elif operation == "d":
        div1()
        main()
    else:
        print("invalid operation")
        main()

main() #run main
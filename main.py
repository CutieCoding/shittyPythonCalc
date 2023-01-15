userList = []

def add1():
    numToAdd = input("input a number: ")
    try: #using exception handling to my advantage, if it cant turn the input into an integer it "errors" by calling that function, else continues to add numbers
        numToAdd = int(numToAdd)
    except:
        print("\n", add2(), "is your answer! :D\n")
    else:#if it can turn the input into an int, it reruns the function to allow more inputs
        userList.append(numToAdd)
        add1()

def add2(): #function that gets called when something other than an int is inputted
    finalNum = 0 #inits variable
    for x in range(len(userList)): #iterates over list, adding each number in the list to finalNum
        finalNum = finalNum + userList[x]
    return finalNum

def sub1():
    numToSub = input("input a number: ")
    try: #using exception handling to my advantage, if it cant turn the input into an integer it "errors" by calling that function, else continues to add numbers
        numToSub = int(numToSub)
    except:
        print("\n", sub2(), "is your answer :D\n")
    else:#if it can turn the input into an int, it reruns the function to allow more inputs
        userList.append(numToSub)
        sub1()

def sub2(): #function that gets called when something other than an int is inputted
    finalNum = 0 #inits variable
    for x in range(len(userList)): #iterates over list
        if x == 0:
            finalNum = finalNum + userList[x]#adds the first number to finalnum, maths is weird
        else: 
            finalNum = finalNum - userList[x]#now it starts subtracting
    return finalNum

def mul1():
    numToMul = input("input a number: ")
    try: #using exception handling to my advantage, if it cant turn the input into an integer it "errors" by calling that function, else continues to add numbers
        numToMul = int(numToMul)
    except:
        print("\n", mul2(), "is your answer :D\n")
    else:#if it can turn the input into an int, it reruns the function to allow more inputs
        userList.append(numToMul)
        mul1()

def mul2(): #function that gets called when something other than an int is inputted
    finalNum = 0 #inits variable
    for x in range(len(userList)): #iterates over list
        if x == 0:
            finalNum = finalNum + userList[x]#adds the first number to finalnum, maths is weird
        else: 
            finalNum = finalNum * userList[x]#now it starts multiplying
    return finalNum

def div1():
    numToDiv = input("input a number: ")
    try: #using exception handling to my advantage, if it cant turn the input into an integer it "errors" by calling that function, else continues to add numbers
        numToDiv = int(numToDiv)
    except:
        print("\n", div2(), "is your answer :D\n")
    else:#if it can turn the input into an int, it reruns the function to allow more inputs
        userList.append(numToDiv)
        div1()

def div2(): #function that gets called when something other than an int is inputted
    finalNum = 0 #inits variable
    for x in range(len(userList)): #iterates over list
        if x == 0:
            finalNum = finalNum + userList[x]#adds the first number to finalnum, maths is weird
        else: 
            finalNum = finalNum / userList[x]#now it starts dividing
    return finalNum

def main(): #interface
    operation = input("a, s, m, d: ")
    if operation == "a": #uses an if statement bcs theres only like 5 different things it can do
        add1()
        for x in range(len(userList)): #VERY dirty way to clear the list because im retarded
            userList.pop()
        main()
    elif operation == "s":
        sub1()
        for x in range(len(userList)): #VERY dirty way to clear the list because im retarded
            userList.pop(0)
        main()
    elif operation == "m":
        mul1()
        for x in range(len(userList)): #VERY dirty way to clear the list because im retarded
            userList.pop(0)
        main()
    elif operation == "d":
        div1()
        for x in range(len(userList)): #VERY dirty way to clear the list because im retarded
            userList.pop(0)
        main()
    else:
        print("invalid operation")
        main()


main() #run main
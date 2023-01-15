userList = []

def sub1():
    numToSub = input("a number: ")
    try: #using exception handling to my advantage, if it cant turn the input into an integer it "errors" by calling that function, else continues to add numbers
        numToSub = int(numToSub)
    except:
        print(sub2())
    else:#if it can turn the input into an int, it reruns the function to allow more inputs
        userList.append(numToSub)
        sub1()

def sub2(): #function that gets called when something other than an int is inputted
    finalNum = 0 #inits variable
    for x in range(len(userList)): #iterates over list, adding each number in the list to finalNum
        if x == 0:
            finalNum = finalNum + userList[x]
        else: 
            finalNum = finalNum - userList[x]
    return finalNum

def main(): #interface
    operation = input("a, s, m, d: ")
    if operation == "s": #uses an if statement bcs theres only like 5 different things it can do
        sub1()
        for x in range(len(userList)): #VERY dirty way to clear the list because im retarded
            userList.pop(0)
        main()
    else:
        print("invalid operation")
        main()


main() #run main
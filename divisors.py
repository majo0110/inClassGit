def divisors(userNum):
    divisorList = []
    for i in range (1, userNum):
        if( (userNum % i) == 0 ):
            divisorList.append(i)

def main():
    userInput = input("Enter a number: ")

    try:
        userInt = int(userInput)
        if(userInt == 0):
            print("You have chosen 0. No input")
        divisors(userInt)

    except ValueError:
        print("You did not enter a valid number. Program will exit")



if __name__ == "__main__":
    main()

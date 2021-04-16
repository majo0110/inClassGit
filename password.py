def genPassword(userInput):
    pass

def main():
    userInput = input("Enter a number: ")

    try:
        userInt = int(userInput)
        if(userInt == 0):
            print("You have chosen 0. No input")

    except ValueError:
        print("You did not enter a valid number. Program will exit")

if __name__ == "__main__":
    main()

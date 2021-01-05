#Robert Brandl
#Goal: Utilize random class to simulate lottery system (Pick 3), conditional statements and looping
import random

def lotteryGenerator():
    pick1 = random.randint(0,9)
    pick2 = random.randint(0,9)
    while pick2 == pick1:
        pick2 = random.randint(0,9)
    pick3 = random.randint(0,9)
    while pick3 == pick1 or pick3 == pick2:
        pick3 = random.randint(0,9)
    print("The winning numbers are: ", pick1, ", ", pick2, ", ", pick3)
    return [pick1,pick2,pick3]

def numberGuess():
    input1 = -1
    input2 = -1
    input3 = -1
    while input1 < 0 or input1 > 9:
        try:
            input1 = int(input("Input your first guess number:\n"))
        except:
            print("Invalid input - enter an integer value between 0 and 9")
    while input2 < 0 or input2 > 9:
        try:
            input2 = int(input("Input your second guess number:\n"))
        except:
            print("Invalid input - enter an integer value between 0 and 9")
    while input3 < 0 or input3 > 9:
        try:
            input3 = int(input("Input your third guess number:\n"))
        except:
            print("Invalid input - enter an integer value between 0 and 9")
    print("Your numbers are: " + str(input1) + ", " + str(input2) + ", " + str(input3))
    return [input1,input2,input3]

def runLottery():
    choice = "yes"
    while choice == "yes":
        print("Welcome to Pick 3 Lottery. You will first select your numbers, from 0 to 9, to compare against the winning numbers")
        guessArr = numberGuess()
        print("\nThe system will now generate the winning numbers\n")
        winArr = lotteryGenerator()
        matches = 0
        if guessArr[0] in winArr: matches += 1
        if guessArr[1] in winArr: matches += 1
        if guessArr[2] in winArr: matches += 1
        if matches == 0: print("Sorry, your numbers did not match the winning numbers.")
        if matches == 1: print("Good attempt! Your numbers matched 1/3 winning numbers.")
        if matches == 2: print("Good job! Your numbers matched 2/3 winning numbers.")
        if matches == 3: print("Congratulations! All of your numbers matched the winning numbers! You won!")
        choice = (input("Would you like to play again?\n")).lower()
    print("Thanks for playing!")
    
if __name__ == "__main__" : runLottery()  
    

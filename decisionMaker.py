#Robert Brandl
#Goal: create a decision maker program that uses a decision with factors and rankings, looping and try/except, heavy-focus on user input

def decisionMaker():
    intro()
    choice1 = input("What is the first choice in your decision?\n")
    choice2 = input("What is the other choice in your decision?\n")
    print("Next, you will list factors that influence the decision. Press enter when you are finished entering factors.\n")
    factor = "k"
    factors = []
    factorPosOrNeg = []
    factorRankings = []
    factorValueC1 = 0
    factorValueC2 = 0
    choice1Counter = 0
    choice2Counter = 0
    factor = input("Enter a factor: \n")
    factors.append(factor) 
    while factor != '':
        try:
            posOrNeg = int(input("Input the number matching the factor's persuasion: \n1) Supports choice 1: " + choice1 + "\n2) Opposes choice 1: " + choice1 + "\n3) Supports choice 2: " + choice2 + "\n4) Opposes choice 2: " + choice2 + "\n"))
        except:
            print("Invalid Input. Input an integer!")
            posOrNeg = int(input("Input the number matching the factor's persuasion: \n1) Supports choice 1: " + choice1 + "\n2) Opposes choice 1: " + choice1 + "\n3) Supports choice 2: " + choice2 + "\n4) Opposes choice 2: " + choice2 + "\n"))
        while posOrNeg < 1 or posOrNeg > 4:
            print("Invalid - enter a number between 1 and 4")
            posOrNeg = int(input("Input the number matching the factor's persuasion: \n1) Supports choice 1: " + choice1 + "\n2) Opposes choice 1: " + choice1 + "\n3) Supports choice 2: " + choice2 + "\n4) Opposes choice 2: " + choice2 + "\n"))
        factorPosOrNeg.append(posOrNeg)
        if posOrNeg == 1: factorValueC1 = 1
        elif posOrNeg == 2: factorValueC1 = -1
        elif posOrNeg == 3: factorValueC2 = 1
        elif posOrNeg == 4: factorValueC2 = -1
        try:
            rank = int(input("Input the number matching the factor's importance in the decision: \n1) Not Very Important\n2) Somewhat Important\n3) Important\n4) More Important\n5) Very Important\n"))
        except:
            print("Invalid Input. Input an integer!")
            rank = int(input("Input the number matching the factor's importance in the decision: \n1) Not Very Important\n2) Somewhat Important\n3) Important\n4) More Important\n5) Very Important\n"))
        while rank < 1 or rank > 5:
            print("Invalid - enter a number between 1 and 5")
            rank = int(input("Input the number matching the factor's importance in the decision: \n1) Not Very Important\n2) Somewhat Important\n3) Important\n4) More Important\n5) Very Important\n"))
        factorRankings.append(rank)
        factorValueC1 *= rank
        factorValueC2 *= rank
        choice1Counter += factorValueC1
        choice2Counter += factorValueC2
        factor = input("\nEnter a factor: \n")
        factors.append(factor)
    result = choice1Counter + choice2Counter
    if result > 0:
        print("The program has determined that choice 1 is the correct option: " + choice1)
    elif result < 0:
        print("The program has determined that choice 2 is the correct option: " + choice2)
    else:
        print("The results are inconclusive. The benefits and drawbacks of both choices are equivalent.")

def intro():
    print("Welcome to the Decision-Maker Program, which will use a ranking system that \nanalyzes benefits and drawbacks of the decision you are making. The program \nonly works for decisions with 2 choices, such as 'Should I go to community \ncollege?' You will repeatedly be asked factors that influence your decision, \nclassify them as pros or cons, and determine the factor's importance in the \ndecision. The program will then combine the factors using positive and negative \nvalues for each factor, and determine whether you should go through with the \ndecision or not.\n")
    
if __name__ == "__main__" : decisionMaker()

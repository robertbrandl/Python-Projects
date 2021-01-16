#Robert Brandl
#Goal: intro to datetime class, formatting, list splicing, absolute value, determining age (in years) from birthdate
import datetime

#use .today() to access current date with time
currentdate = datetime.datetime.today()

#formatted to get monthdayyear format
cdateformatted = datetime.datetime.today().strftime('%d%m%Y')
cmonth = int(cdateformatted[2:4])
cday = int(cdateformatted[0:2])
cyear = int(cdateformatted[4:8])



def ageCalculator():
    print("The program will determine your current age based off of your birth date")
    day = int(input("What day were you born? (Input as a number)\n"))
    month = int(input("What month were you born? (Input as a number)\n"))
    year = int(input("What year were you born? (Input as a number)\n"))
    today = currentdate
    print(today.year - year)
    print((today.month, today.day) < (month, day))
    age = today.year - year - ((today.month, today.day) < (month, day))
    print("Your current age: " + str(age))
if __name__ == "__main__" : ageCalculator()

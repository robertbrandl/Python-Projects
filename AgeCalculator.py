#Robert Brandl
#Goal of project: intro to datetime class, formatting, determining age from birthdate
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
    agey = cyear - year
    agem = abs(cmonth-month)
    aged = abs(cday-day)
    print("Your age: ", agey, " years, ", agem, " months, ", aged, " days old")

if __name__ == "__main__" : ageCalculator()

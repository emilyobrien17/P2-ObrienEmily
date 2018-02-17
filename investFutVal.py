# futval.py
#  A program to compute the value of an investment
#  carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal:  "))
    apr = eval(input("Enter the annual interest rate:  "))
    years = eval(input("Enter the number of years for investment:  "))
    addPerYear = eval(input("Enter how much you want to add to your investment per year:  "))
    period= eval(input("Enter period per year:  "))

    for i in range(years * period):
        principal = principal * ((1 + apr)/period)
        principal = principal + addPerYear

    print("The result after ", years, " years is:", principal)


main()

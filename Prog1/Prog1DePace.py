#
# Name: Kyle DePace
# prog1DePace.py
# Purpose: This program will convert any number of temperatures to fahrenheit from celsius
#
# Input: Temperatures in Celsius
#
# Output: Temperatures in Fahrenheit
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


def main():
    print("Welcome to converter! I will convert temperatures for you.")  # Greeting
    print()
    # Get the number of runs
    runs = int(input("How many numbers would you like to convert? "))
    # Loops "runs" amount of times
    for i in range(runs):
        # Gets temp in celsius from user
        cel = float(input("Enter a temperature in celsius. "))
        # Converts temp to fahrenheit
        fah = cel * 9/5 + 32
        # Prints the results from one loop
        print(cel, "degrees celsius is equal to", fah, "degrees fahrenheit")
        print()
    exit()


main()

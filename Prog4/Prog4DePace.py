#
# Name: Kyle DePace
# Prog4DePace.py
# Purpose: Simulate a casino game where if a 7 is rolled the user profits $3 and if an 11 is rolled the user profits $2
#
# Input: The number of dollars to gamble
#
# Output: The number of plays, this turn's rolls, and balance after each round
#
# Certification of Authority: I certify that this lab is entirely my own work.
#

from random import randrange


def main():
    # Greeting
    print("Welcome, player, to the Lucky Seven Eleven game!\nBet a buck - if you roll a 7, you win $3!\nIf you roll an 11, you win $2!\n")

    # Get the bet from the user
    balance = int(input("How many dollars are you willing to bet (1-100)? "))
    while balance < 1 or balance > 100:  # Check for validity
        balance = int(input("Invalid amount. Please enter a number between 1 and 100: "))

    # Initialize variables
    plays = 0
    maxTurnNum = 0
    maxBalance = balance

    # Begin rolling until out of money
    while balance > 0:

        # Increment the number of plays
        plays += 1

        # Roll the two dice (Numbers 1 to 6, 7 not included)
        die1 = randrange(1, 7)
        die2 = randrange(1, 7)
        roll = die1 + die2

        # Modify balance / Do payouts
        if roll == 7:
            balance += 3
        elif roll == 11:
            balance += 2
        else:
            balance -= 1

        # Check for a new max, if so save it in the variables
        if balance > maxBalance:
            maxBalance = balance
            maxTurnNum = plays

        # Print results from the turn
        print("Play {}\t\tdie1 = {}\tdie2 = {}\tPot = {}".format(plays, die1, die2, balance))
    # End of game stats print
    print("You are broke after {} rolls.".format(plays))
    print("You should have quit after {} rolls when you had ${}.".format(maxTurnNum, maxBalance))


main()

##
# Name: Kyle DePace
# Prog6DePace.py
# Purpose: This program allows a user to input data about the movies they wish to buy and calculate the cost
##
# Input: The User's ID, name, and number of movies, and for each movie, the length and the rating.
##
# Output: The user's name, id, movie purchased, cost of movies, service charge, and total due
# At the end it will output, the number of customers, the highest charge and the id that purchased it, the lowest charge and the id that purchased it, the total downloads, and the average purchase amount.
##
# Certification of Authority: I certify that this lab is entirely my own work.
##


def main():
    # Greeting
    print("Welcome to the Kyle's Movie Store. You can buy movies here.\n")

    # Initialize the running statistics
    custID = 1
    numCustomers = 0
    highestCharge = 0
    highestChargeID = 0
    lowestCharge = 99999999999
    lowestChargeID = 0
    totalMovies = 0
    totalRevenue = 0

    # Only run while the customers ID is not 0
    while custID != 0:
        # Get id from user and validate input
        custID = int(input("What is your customer ID? "))
        while custID != 0 and custID < 25000 or custID > 99999:
            custID = int(input("What is your customer ID? "))

        # if user enters 0 we want to exit the loop without having to calculate
        if custID != 0:
            numCustomers += 1
            # Get name and number of movies(validated)
            custName = input("What is your name? ")
            numMovies = int(input("How many movies do you want to order? "))
            while numMovies < 0:
                numMovies = int(input("How many movies do you want to order? "))

            # Add the number of movies to the running total
            totalMovies += numMovies
            print()

            # Get user's input for the length and rating of the movie
            cost = chooseMovies(numMovies)

            # Get the service charge for the user
            serviceCharge = calcServiceCharge(numMovies, cost)

            # Calculate the total with tax
            totalDue = calcTotalDue(cost, serviceCharge)

            # Print the results in an organized way
            outputResults(custName, custID, numMovies, cost, serviceCharge, totalDue)

            # Check if there are any records broken by this customer
            if totalDue > highestCharge:
                highestCharge = totalDue
                highestChargeID = custID
            if totalDue < lowestCharge:
                lowestCharge = totalDue
                lowestChargeID = custID

            # Add the total due to the running total
            totalRevenue += totalDue
    # Print the data from the "big" loop once the customer enters 0 as the ID
    outputSummary(numCustomers, highestCharge, highestChargeID, lowestCharge, lowestChargeID, totalMovies, totalRevenue)

# chooseMovies
#
# This function gets input from the user about the movies they want to buy
#
# Parameters -
# numMoviesOrdered: The number of movies the customer wants to order
#
# Returns: The total cost of all the movies the customer wants


def chooseMovies(numMoviesOrdered):
    totalCost = 0
    for i in range(numMoviesOrdered):
        # Get the length of the movie and validate it
        movieLength = int(input("How long is the movie (in minutes)? "))
        while movieLength < 1 or movieLength > 240:
            movieLength = int(input("How long is the movie (in minutes)? "))

        # Start rate at 0 to enter the loop
        rate = 0
        while rate == 0:
            rating = input("What is the rating? ").upper()
            if rating == "G":  # 3.9 cents per hour
                rate = 3.9
            elif rating == "PG":  # 5.4 cents per hour
                rate = 5.4
            elif rating == "R":  # 6.8 cents per hour
                rate = 6.8
            elif rating == "X":  # 27.3 cents per hour
                rate = 27.3
            elif rating == "O":  # 4 cents per hour
                rate = 4
        totalCost += movieLength * rate / 100  # rate is in cents per minute and must be converted to dollars per minute
        print()
    return totalCost

# calcServiceCharge
#
# This function calculates the service charge on the movies ordered
#
# Parameters -
# numMoviesOrdered: The number of movies the customer wants to order
# totalCost: The cost of the movies without tax or service charge applied
#
# Returns: The service charge as a float


def calcServiceCharge(numMoviesOrdered, totalCost):
    if numMoviesOrdered < 4:  # Movies: 1-3
        fee = .18
    elif numMoviesOrdered < 8:  # Movies: 4-7
        fee = .15
    elif numMoviesOrdered < 12:  # Movies: 8-11
        fee = .11
    else:  # Movies: 12 - Infinity
        fee = .05
    return totalCost * fee

# calcTotalDue
#
# This function calculates the total amount due on a purchase
#
# Parameters -
# movieCost: The cost of the movies without any fees or taxes applied
# serviceCharge: The service charge of the movies
#
# Returns: returns the total amount due with taxes and fees applied


def calcTotalDue(movieCost, serviceCharge):
    # 7% tax on the total of the movie cost and service charge
    return 1.07 * (movieCost + serviceCharge)

# outputResults
#
# This function prints details on an individual customers transaction
#
# Parameters -
# name: the customers name
# id: the customers id
# numPurchased: the amount of movies purchased
# totalCost: the cost of the movies
# serviceCharge: the service charge
# totalDue: the total amount due
#
# Returns: None


def outputResults(name, id, numPurchased, totalCost, serviceCharge, totalDue):
    print("Customer Name: {}".format(name))
    print("Customer ID: {}".format(id))
    print("Number of Movie Purchased: {}".format(numPurchased))
    print("Cost of Movies: ${0:0.2f}".format(totalCost))
    print("Service Charge: ${0:0.2f}".format(serviceCharge))
    print("Total Due: ${0:0.2f}".format(totalDue))
    print()

# outputSummary
#
# This function prints details on a group of customers transactions
#
# Parameters -
# numCustomers: the number of customers
# highestCharge: the highesst charged amount
# highestChargeID: the highest charged id
# lowestCharge: the lowest charged amount
# lowestChargeID: the lowest charged id
# totalMovies: the number of movies purchased in total
# totalRevenue: the total of all purchases
#
# Returns: None


def outputSummary(numCustomers, highestCharge, highestChargeID, lowestCharge, lowestChargeID, totalMovies, totalRevenue):
    print()
    print("Number Processed: {}".format(numCustomers))
    print("Highest Charge: ${0:0.2f}".format(highestCharge))
    print("ID of highest charge: {}".format(highestChargeID))
    print("Lowest Charge: ${0:0.2f}".format(lowestCharge))
    print("ID of lowest charge: {}".format(lowestChargeID))
    print("Total Downloads: {}".format(totalMovies))
    print("Average of purchase amount: ${0:0.2f}".format(totalRevenue / numCustomers if numCustomers != 0 else 0))  # Ternary operator prevents division by zero


main()

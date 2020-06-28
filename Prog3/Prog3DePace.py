#
# Name: Kyle DePace
# Prog3DePace.py
# Purpose: To calculate the cost of an online music store
#
# Input: Last name, First name, Base cost per song, Number of songs
#
# Output: Name, Number of songs, Price per song, Service charge, Taxes owed, total charges
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


def main():
    # Greeting
    print("Welcome to the music shop. You can download songs here.\n")

    # Get user details
    last = input("What is your last name? ")
    first = input("What is your first name? ")

    # Check for invalid inputs < 0
    base = float(input("What is the base cost per song? $"))
    while base <= 0:
        base = float(input("What is the base cost per song? It has to cost something... $"))

    # Check for invalrid inputs, at least 1 song
    numSongs = int(input("How many songs would you like to download? "))
    while numSongs < 1:
        numSongs = int(input("How many songs would you like to download? At least one..."))

    # Calculate service charge
    if(numSongs >= 6):  # 6 or more songs
        serviceCharge = base * numSongs * .07
    elif(numSongs > 3):  # More than 3 but less than 6
        serviceCharge = base * numSongs * .10
    elif(numSongs > 0):  # More than 0 but less than or equal to 3
        serviceCharge = base * numSongs * .13
    else:
        print("You do not want to buy any songs")  # Shouldn't happen because of the checks earlier

    # Calculate the tax
    netPayment = serviceCharge + base * numSongs
    if(netPayment < 0):
        print("We do not buy from you")  # Shouldn't happen because of the checks earlier
    elif(netPayment <= 5.00):  # Not more than 5.00s
        tax = 0
    elif(netPayment <= 7.50):  # More than 5.00 but not more than 7.50
        tax = netPayment * .045
    elif(netPayment <= 9.99):  # More than 7.50 but not more than 9.99
        tax = netPayment * .0725
    else:  # More than 9.99
        tax = netPayment * .09

    # Print the bill
    print("\nName: {} {}".format(first, last))
    print("Number of Songs Purchased: {}".format(numSongs))
    print("Price per Song:\t ${0:0.2f}".format(base))
    print("Service Charge:\t ${0:0.2f}".format(serviceCharge))
    print("Taxes Owed:\t ${0:0.2f}".format(tax))
    print("Total Charge:\t ${0:0.2f}".format(netPayment + tax))


main()

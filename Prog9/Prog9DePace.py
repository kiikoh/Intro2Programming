#
# Name: Kyle DePace
# Prog9DePace.py
# Purpose: Manage a users cart and display information about the Items in it
#
# Input: Name of a file which contains the name quantity and price of an item. The user may then use a menu.
#
# Output: Depending on the users choice it can add, delete and print items from the cart.
#           You can find out how many items are in the cart and the total cost of the cart.
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


from itemDePace import Item

# 1. addItem
#
# Adds an item to the list of items
#
# Parameters:
#       aList - The list of items to add to
#
# Returns: None
def addItem(aList):
    print("Please provide information about the item to add.")
    itemName = input("Please enter the name: ")
    itemQuantity = int(input("Please enter the quantity: "))
    while itemQuantity < 0:
        itemQuantity = int(input("Please enter the quantity: "))
    itemPrice = float(input("Please enter the unit price: "))
    while itemPrice < 0:
        itemPrice = float(input("Please enter the unit price: "))
    aList.append(Item(itemName, itemQuantity, itemPrice))
    print()
    print(itemName, "has been added to the cart.")


# 2. removeItem
#
# Removes an item from the list of items
#
# Parameters:
#       aList - The list of items to remove from
#       itemName - The name of the item to remove
#
# Returns: None
def removeItem(aList, itemName):
    # This will tell us if we removed an item
    removedOne = False
    # Iterate through the array backwards so we dont shift indexes upon deletion
    for i in range(len(aList) - 1, -1, -1):
        if aList[i].getName().upper() == itemName.upper():
            aList.pop(i)
            removedOne = True
    if not removedOne:
        print(f"Sorry, but your cart does not contain the item {itemName}")
    else:
        print(f"Removed {itemName} from the cart.")


# 3. printList
#
# Prints the list of items
#
# Parameters:
#       aList - The list of items to print
#
# Returns: None
def printList(aList):
    # Make sure the list has values
    if listIsEmpty(aList):
        print("The list is empty")
    else:
        for val in aList:
            print(val)


# 4. searchList
#
# Searches the list for an item by name
#
# Parameters:
#       aList - The list of items to search in
#       itemName - The name of the item to search for
#
# Returns: The item or None if it cannot be found
def searchList(aList, itemName):
    foundItem = None
    for item in aList:
        if item.getName().upper() == itemName.upper():
            foundItem = item
    return foundItem


# 5. totalQuantity
#
# Calculates the total number of items in the list
#
# Parameters:
#       aList - The list of items to count
#
# Returns: The number of items in the list
def totalQuantity(aList):
    count = 0
    for item in aList:
        count += item.getQuantity()
    return count


# 6. totalCost
#
# Calculates the total cost of the items in the list
#
# Parameters:
#       aList - The list of items to total their cost
#
# Returns: The cost of the items in the list
def totalCost(aList):
    total = 0
    for item in aList:
        total += item.getPrice() * item.getQuantity()
    return total


# 7. listIsEmpty
#
# Determines if the list is empty or not
#
# Parameters:
#       aList - The list
#
# Returns: True if the list is empty
def listIsEmpty(aList):
    return len(aList) == 0


# showMenu
#
# Prints the menu
#
# Parameters: None
#
# Returns: None
def showMenu():
    print("1. Add an item to the list")
    print("2. Delete an item from the list")
    print("3. Print each item in the list")
    print("4. Search for a user-specified item in the list")
    print("5. Count the total number of items in the list")
    print("6. Total the cost of the items in the list")
    print("7. Determine whether the list is empty")
    print("8. Clear the list")
    print("0. Quit")


def main():
    print("Welcom to Scam's Warehouse Club!")

    # Open the input data file
    inputFile = open(input("Please enter the path and name for the data file: "), "r")
    print("Thank you")

    # Get the number of items in the file
    numItems = int(inputFile.readline())

    # For the number of items in the file, create an item
    cart = []
    for i in range(numItems):
        name = inputFile.readline().strip()
        quantity = int(inputFile.readline())
        price = float(inputFile.readline())
        # Append the item to the cart
        cart.append(Item(name, quantity, price))

    # Show the menu and ask for the first time
    print()
    showMenu()
    option = input("Select an option from the menu: ")
    print()

    # Unless the user quits we will loop
    while option != "0":
        # Do the appropriate action for each option
        if option == "1":
            addItem(cart)
        elif option == "2":
            removeItem(cart, input("Please enter the name of the item to delete from your cart: "))
        elif option == "3":
            printList(cart)
        elif option == "4":
            # Search list will return None if the item is not found
            result = searchList(cart, input("Enter an item name to search for: "))
            if result is None:
                print("No items found")
            else:
                print(result)
        elif option == "5":
            print("There are", totalQuantity(cart), "items in the cart")
        elif option == "6":
            print("The total cost of the cart is ${:0.02f}".format(totalCost(cart)))
        elif option == "7":
            if listIsEmpty(cart):
                print("The list is empty")
            else:
                print("The list is not empty")
        elif option == "8":
            # Set the cart to an empty list
            cart = []
            print("The list has been emptied")
        else:  # If we reach here, they chose an invalid option
            print("Invalid choice.")
        print()

        # Show the menu and ask again
        showMenu()
        option = input("Select an option from the menu: ")
        print()

    print("Goodbye")


main()

#
# Name: Kyle DePace
# Prog8DePace.py
# Purpose: To print and modify the creation of rectangles
#
# Input: "WHFAPTDOQ" will each do its own function in the menu
#
# Output: Variously sized rectangles depending on the users input
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


from rectangleDePace import Rectangle

# showMenu
#
# This function prints the menu options
def showMenu():
    print("W: Assign the Width")
    print("H: Assign the Height")
    print("F: Assign the Fill Style")
    print("A: Calculate the Area")
    print("P: Calculate the Perimeter")
    print("T: Text Description of the Rectangle")
    print("D: Draw the Rectangle")
    print("O: Draw the Outline of the Rectangle")
    print("Q: Quit")


def main():
    # Greet the user
    print("Welcome to the rectangle factory!")

    # Create the rectangle object
    rect = Rectangle()

    # Show the menu and prompt the user
    showMenu()
    option = input("Select an option from the menu: ").upper()[0]
    print()

    # Unless the user quits we will loop
    while option != "Q":
        # Do the appropriate action for each option
        if option == "W":
            result = rect.setWidth(int(input("Enter a new width: ")))
            # The result is None if it was successfully changed, if it isnt it failed and we need to try again
            while result is not None:
                result = rect.setWidth(int(input("Invalid. Enter a new width: ")))
        elif option == "H":
            result = rect.setHeight(int(input("Enter a new height: ")))
            # The result is None if it was successfully changed, if it isnt it failed and we need to try again
            while result is not None:
                result = rect.setHeight(int(input("Invalid. Enter a new height: ")))
        elif option == "F":
            rect.setFillStyle(input("Enter a fill style: "))
        elif option == "A":
            print("The area is:", rect.calcArea())
        elif option == "P":
            print("The perimeter is:", rect.calcPerimeter())
        elif option == "T":
            print(rect)
        elif option == "D":
            rect.drawRectangle()
        elif option == "O":
            rect.drawOutline()
        else:  # If we reach here, they choose an invalid option
            print("Invalid choice.")
        print()
        showMenu()
        option = input("Select an option from the menu: ").upper()[0]
        print()

    print("Goodbye")


main()


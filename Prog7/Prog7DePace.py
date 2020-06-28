##
## Name: Kyle DePace
## Prog7DePace.py
## Purpose: This program has mutliple calculators that takes sets of number or letters as inputs
##
## Input: The menu takes HMTG or Q and each program will take a set of values to be processed
##
## Output: Averages, highs, lows, whether or not there are more postiives, the nubmer of occurences in a list, the grade from a multiple choice test
##
## Certification of Authority: I certify that this lab is entirely my own work.
##

# chooseFromMenu
#
# This function helps with getting the user's choice
#
# Returns: the highest number in the array
def chooseFromMenu():
    # Print the menu
    print("H) Handle Grades")
    print("M) More Positives or Negatives")
    print("T) How Many Times?")
    print("G) Grade a Quiz")
    print("Q) Quit")

    # Only take the first letter and make it always capital
    userIn = input("Select an option from the menu: ")[0].upper()
    print()

    # Check if the letter matches the possible values
    if not userIn in "HMTGQ":
        print("Invalid Choice.\n")
        return chooseFromMenu()  # Use recursion to keep asking if the answer is invalid

    # Only reaches this point if the input is valid
    return userIn


# low
#
# This function returns the lowest number in an array
#
# Parameters:
#   arr: the array to check for the lowest number
#
# Returns: the lowest number in the array
def low(arr):
    #Initialize the lowest value
    low = arr[0]

    #Loop through the entire array
    for val in arr:
        if val < low:
            low = val
    
    #return the lowest value
    return low


# high
#
# This function returns the highest number in an array
#
# Parameters:
#   arr: the array to check for the highest number
#
# Returns: the highest number in the array
def high(arr):
    #Initialize the highest value
    high = arr[0]

    #Loop through the entire array
    for val in arr:
        if val > high:
            high = val

    # return the lowest value
    return high


# average
#
# This function calculates the average for the array
#
# Parameters:
#   arr: the arr to average
#
# Returns: the average of the number array
def average(arr):
    #initialize the sum to 0
    count = 0

    #Increment the sum by the value of each item in array
    for val in arr:
        count += val

    # Divide the sum by the number of values
    average = count / len(arr)

    #return the average
    return average


# handleGrades
#
# This function gets the input for the "H" option
def handleGrades():
    #Print the greeting for the subprogram
    print("Starting Grade Handler...\n")

    #Start with an empty list
    grades = []

    #Take exactly 10 integers
    for i in range(1, 11):
        grades.append(int(input("Enter grade {}: ".format(i))))

    #Print the results
    print("The highest grade is a", high(grades))
    print("The lowest grade is a", low(grades))
    print("The average grade is a", average(grades))


# isMorePosOrNeg
#
# This function determines if there are more positives or negatives in an array
#
# Parameters:
#   arr: the arr to check for pos or negs
#
# Returns: an arr containing the more popular number type, full array for tie
def isMorePosOrNeg(arr):
    #Create two arrays to store the values
    pos = []
    neg = []

    #Go through the array and places the values in their appropriate lists
    for val in arr:
        # Dont do anything for 0
        if val > 0:
            pos.append(val)
        elif val < 0:
            neg.append(val)

    #Determine what to print and return
    if len(pos) > len(neg):
        print("There are more positives")
        return pos
    elif len(pos) < len(neg):
        print("There are more negatives")
        return neg

    #If it reaches here there is an equal amount of
    print("There are the same amount of positives and negatives")
    return arr


# posOrNeg
#
# This function gets input for the "M" option
def posOrNeg():
    #Print the greeting for the subprogram
    print('Starting "Is the more positives or negatives?"...\n')

    #Create a list to store the users inputs
    numbers = []

    #Get the inputs
    value = input("Enter Integer 1: (Enter to stop) ")
    while len(numbers) < 9 and value != "":
        numbers.append(int(value))
        value = input("Enter Integer {}: (Enter to stop) ".format(len(numbers) + 1))
    if value != "":
        numbers.append(int(value))

    #Print the output from the helper method
    print(isMorePosOrNeg(numbers))


# howManyTimes
#
# This function manages the input for "T" option
def howManyTimes():
    #Print the gretting for the subprogram
    print('Starting "How many times?"...\n')

    #Create a list for uses inputs
    numbers = []

    #Get the user's inputs
    value = int(input("Enter negative integer 1 (pos to stop): "))
    while len(numbers) < 9 and value < 0:
        numbers.append(value)
        value = int(input("Enter negative integer {} (pos to stop): ".format(len(numbers) + 1)))
    if value < 0:
        numbers.append(value)

    #Get the target to search for
    target = int(input("Please enter a target value: "))

    #Use the helper method
    occurences(numbers, target)


# occurences
#
# This function provides the number of times an element appears in an array
#
# Parameters:
#   arr: the array to search within
#   target: the item which should be counted in the array
def occurences(arr, target):
    #Start the counter at zero
    count = 0

    #If the value matches the target, add 1 to the count
    for val in arr:
        if val == target:
            count += 1
    #Print the required information using format
    print("\nThe number {} appears {} time(s) in {}".format(target, count, arr))


# getQuizResponses
#
# This function handles getting the input for the quiz subprogram including validation
#
# Returns: the provided input
def getQuizResponses():
    #Create an empty list
    answers = []
    
    #Loop 8 times to get input, I use 1-9 to assist in saying which answer is being asked
    for i in range(1, 9):
        #Get the answer and validate that it is "ABCD"
        ans = input("Enter answer {}: ".format(i)).upper()[0]
        while not ans in "ABCD":
            print("Invalid answer. Choose ABCD.")
            ans = input("Enter answer {}: ".format(i)).upper()
        #Append the answer to the array
        answers.append(ans)
    print()
    #Return the answers as a list with 8 elements containing only letters a b c d
    return answers


# percentToGrade
#
# This function transform a percentage to a letter grade
#
# Parameters:
#   percent: the grade percent (from 0-100)
#
# Returns: the letter grade corresponding to the percent
def percentToGrade(percent):
    #Use an if to turn a percent grade into a letter grade from the syllabus
    #Elif is not required because it returns on the first time it is matched
    if percent < 60:
        return "F"
    if percent < 65:
        return "D"
    if percent < 68:
        return "D+"
    if percent < 70:
        return "C-"
    if percent < 75:
        return "C"
    if percent < 78:
        return "C+"
    if percent < 80:
        return "B-"
    if percent < 85:
        return "B"
    if percent < 88:
        return "B+"
    if percent < 90:
        return "A-"
    return "A"


# compareAnswers
#
# This function calculates the number of matches between the two arrays
#
# Parameters:
#   answers: an array with the students "scantron" results
#   answkey: an array with the teachers answer key
#
# Returns: the number of correct answers in the arrays
def compareAnswers(answers, anskey):
    #Start the nunmber of correct answers at 0
    correct = 0

    #Loop through the 8 elements
    for i in range(8):
        #Check if they are in the same place in both arrays, increment the number correct
        if answers[i] == anskey[i]:
            correct += 1
    
    #return the number of correct questions
    return correct


# gradeQuiz
#
# This function handles the output of the grade of the student
def gradeQuiz():
    #Print the greeting for the subprogram
    print("Starting Quiz Grader...\n")

    #Use the helper to get the students answers
    print("Enter student answers.")
    student = getQuizResponses()

    #use the helper to get the answer key
    print("Enter the answer key.")
    key = getQuizResponses()

    #Use the helper to determine who is correct and calculate percentage
    percentCorrect = compareAnswers(student, key) / 8 * 100
   
    #Turn the percent into a letter grade
    letterGrade = percentToGrade(percentCorrect)

    #Print the output
    print("The student scored a {0:0.1f}% which is a(n) {1}".format(percentCorrect, letterGrade))


# main
# This function starts the loop which runs the program until the user enters option "Q"
def main():
    #Print a greeting
    print("Welcome to the multi-calculator!\n")
    
    #Always loop until the we break out of the loop
    while True:
        #Use the helper to get a valid selection from the user
        option = chooseFromMenu()

        #Start a subprogram according to the user
        if option == "H":
            handleGrades()
        elif option == "M":
            posOrNeg()
        elif option == "T":
            howManyTimes()
        elif option == "G":
            gradeQuiz()
        elif option == "Q":
            break
        print()

    #Say bye
    print("Goodbye!")


main()

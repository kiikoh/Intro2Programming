#
# Name: Kyle DePace
# Prog5DePace.py
# Purpose: To calculate taxes for multiple people aat once taking input from a file
#
# Input: The path for a file containing the number fo taxpayer on the first line,
#           then their taxpayer ID, filing status, gross income, and number of exemptions
#
# Output: For each user: Taxpayer ID, Filing Status, Taxable Income, Tax rate, and Taxes Owed
#         At the end: Number of tax payers, Highest tax amount, ID of highest tax amount, Total number of taxes paid and Average tax amount
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


def main():
    # Greet the user
    print("Welcome to the tax rate calculator. I will calculate taxes from a file.")

    file = open(input("Enter a filename for input: "), "r")

    numTaxpayers = int(file.readline())
    highestTax = 0
    highestTaxID = -1
    totalTaxes = 0

    for i in range(numTaxpayers):
        # Read the data from the file
        taxID = int(file.readline())
        status = file.readline().strip().upper()
        grossIncome = float(file.readline())
        exemptions = int(file.readline())

        # Calculate the amount of taxable income
        taxableIncome = grossIncome - 4250 - exemptions * 1600

        # Get the tax rate the taxpayer will pay
        if status == "S":
            status = "Single"
            if taxableIncome < 15000:
                rate = .14
            elif taxableIncome <= 50000:
                rate = .22
            else:
                rate = .31
        elif status == "M":
            status = "Married Filing Jointly"
            if taxableIncome < 25000:
                rate = .12
            elif taxableIncome <= 135000:
                rate = .20
            else:
                rate = .29
        elif status == "H":
            status = "Head of Household"
            if taxableIncome < 30000:
                rate = .13
            elif taxableIncome <= 70000:
                rate = .21
            else:
                rate = .30

        # Calculate the amount owed
        taxesOwed = taxableIncome * rate
        if taxesOwed < 0:  # If taxable income is less than 0 no taxes are owed
            taxesOwed = 0

        # Store the highest taxes owed
        if highestTax < taxesOwed:
            highestTax = taxesOwed
            highestTaxID = taxID

        # Sum the total taxes owed
        totalTaxes += taxesOwed

        # Print out the results
        print("\nTaxpayer ID: {}".format(taxID))
        print("Filing status: {}".format(status))
        print("Taxable Income: ${0:0.2f}".format(taxableIncome))
        print("Tax Rate: {}%".format(int(rate*100)))
        print("Taxes Owed: ${0:0.2f}".format(taxesOwed))

    # Calculate the average taxes
    avgTaxes = totalTaxes / numTaxpayers
    # Print out the results
    print("\nSummary: ")
    print("Number of Taxpayers processed: {}".format(numTaxpayers))
    print("Highest tax amount: ${0:0.2f}".format(highestTax))
    print("Taxpayer ID of highest tax : {}".format(highestTaxID))
    print("Total amount of taxes paid: ${0:0.2f}".format(totalTaxes))
    print("Average tax amount: ${0:0.2f}".format(avgTaxes))


main()

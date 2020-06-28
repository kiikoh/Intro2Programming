#
# Name: Kyle DePace
# Prog2DePace.py
# Purpose: This program will give a tweet a score so it can be
#          ranked on a twitter user's timeline
#
# Input: The # of retweets, replies, and days since the tweet was posted
#
# Output: The score for the tweet
#
# Certification of Authority: I certify that this lab is entirely my own work.
#


def main():
    # User friendly greeting
    print("This program will compute the score for a promoted tweet.")
    print()

    # Get inputs from the user
    retweets = int(input("Please enter the number of RTs: "))
    replies = int(input("Please enter the number of @ replies: "))
    # Days are float ex) it could be a day and 5 hours
    days = float(input("Please enter the number of days since the tweet was posted: "))
    dayScore = 2 / days**3
    retweets = retweets * .3333
    replies = replies * .3333
    dayScore = dayScore * .3333

    # Calculate the score
    score = (retweets + replies + dayScore)  # would have divided by 3 for more accuracy

    # Output the score
    print("Your tweet's score is", score, "\nThank you for calculating your score")


main()

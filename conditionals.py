"""
Simple Conditional Statements in Python
---------------------------------------

This script demonstrates:
1. A simple `if..else` statement for handling user input.
2. A nested `if..elif..else` statement for handling multiple conditions.
3. Proper use of string methods and logical operators.

"""

# Implement a simple if..else.. statement
userReply = input("Do you need to ship a package? (Enter yes or no): ")

if userReply == "yes":
    print("We can hep you ship that package")
else:
    print("Please comeback when you need to ship a package. Thank you.")


# Implement a nested if statement i.e if..elif..else.. statement
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy): ")

if userReply.lower() in ["stamps", "stamp"]:
    print("We have many stamps to choose from.")
elif userReply.lower() in ["envelope", "envelopes"]:
    print("We have many envelopes sizes to choose from")
elif userReply.lower() in ["copy", "copies"]:
    copies = input("How many copies would you like? (Enter a number): ")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, Please come again.")
        
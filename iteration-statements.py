"""
While and For Loop Demonstration
-----------------------------------------

This script includes:
1. A simple number guessing game using a `while` loop.
   - The script generates a random number between 1 and 10.
   - The user tries to guess the number, receiving feedback on their guess.
   - Distance hints ("Warm", "Cold", "Neutral") guide the user.
   
2. A basic `for` loop demonstration.
   - The script counts from 1 to 10 and prints each number.
"""

# Import random module
import random

print("Welcome to Guess the Number!")
print("----"*10)
print("The rules are simple. I will think of a number between 1 to 10, and you will try to guess it")

randomNumber = random.randint(1,10)

#Initializing the check bool variable
isGuessRight = False

# Game Logic : While Loop
while isGuessRight != True:
    guess = int(input("Guess the number : "))
    
    distance_from_answer = abs(randomNumber - guess)
    
    if int(guess) == randomNumber:
        print(f"You have guessed {guess} which is the correct number : {randomNumber}")
        isGuessRight = True
    else:
         print(f"You have guessed {guess}. Incorrect. Try Again")
         if distance_from_answer < 2:
             print("Warm")
         elif distance_from_answer >5:
             print("Cold")
         else:
             print("Neutral")

# For Loop Implementation Example
print("This script counts 1 to 10!")
print("---"*10)

for x in range(0,10):
    print(x+1)
    
    

    
    

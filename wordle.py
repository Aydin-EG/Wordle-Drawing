import random

word_list = []

with open("valid-wordle-words.txt") as words:
    for line in words:
        word_list.append(line.rstrip("\n"))
    
answer = random.choice(word_list)
numbers = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
guess_number = 0

def turn():
    global guess_number
    guess = input(numbers[guess_number] + " guess: ").lower()
    if (len(guess) != 5):
        print("enter a 5 letter word")
        turn()
    elif guess in word_list:
        print("valid guess")

        if (guess == answer):
            print("you win!")
        else:
            clue = ""

            for index, x in enumerate(guess):
                if (x == answer[index]):
                    clue += x.upper()
                elif(x in answer):
                    clue += x.lower()
                else:
                    clue += "_"

            print(clue)
        if (guess_number > 4):
            print("you have ran out of guesses! The word was:", answer)
        else:
            guess_number += 1
            turn()
    else:
        print("word not in list, enter a valid word")
        turn()

print("Welcome to wordle. A lowercase letter is yellow and uppercase is green.")
turn()
# ################### Scope ####################

# enemies = 1


# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

list_of_numbers = []
for number in range(1, 101):
    list_of_numbers.append(number)


def difficulty_level():
    difficulty_level = input(
        "Choose your difficulty level: type 'easy' for easy mode, type 'hard' for hard mode:  ")

    if difficulty_level == 'easy':
        guesses = 10
    elif difficulty_level == 'hard':
        guesses = 5

    return guesses


def number_guess():
    play_again = False
    while not play_again:
        print("Welcome to the number guessing game!")
        guesses = difficulty_level()

        hidden_number = random.choice(list_of_numbers)

        while guesses != 0:
            guessed = int(input("Guess a number between 1 and 100:  "))
            if hidden_number > guessed:
                guesses -= 1
                print(f"It's greater. Number of guesses remaining: {guesses}\n")
            elif hidden_number < guessed:
                guesses -= 1
                print(f"It's smaller. Number of guesses remaining: {guesses}\n")
            elif hidden_number == guessed:
                print(f"You won the hidden number is {hidden_number}")
                guesses = 0
            elif guesses == 0:
                print(
                    f"You lose. The hidden number was {hidden_number} remaining guesses: {guesses}")
        another_game = input("Do you want to play again? type 'yes' to play again or 'no' to quit: ")
        if another_game == 'yes':
            number_guess()
        elif another_game == 'no':
            play_again = True


number_guess()

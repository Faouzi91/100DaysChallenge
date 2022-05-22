# #Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# # chosen_word = word_list[random.randint(0,len(word_list)-1)]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.

# display = []
# #For each letter in the chosen_word, add a "_" to 'display'.

# for char in chosen_word:
#   display += "_"
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# print(display)

# guess = input("Guess a letter: ").lower()

# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# index = 0
# for letter in chosen_word:
#     if letter == guess:
#         display[index] = guess
#     else:
#         print("Wrong")
#     index += 1


# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

# print(display)

# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


# # Step 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# # Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# # # TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# # while display.__contains__("_"):
# #     guess = input("Guess a letter: ").lower()

# # # Check guessed letter
# #     for position in range(word_length):
# #         letter = chosen_word[position]
# # #     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
# #         if letter == guess:
# #             display[position] = letter
# #         if position == word_length - 1:
# #             print(display)


# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#         if position == word_length - 1:
#             print(display)

# print("You win!")


# #Step 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #Set 'lives' to equal 6.
# lives = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1.
#     if guess not in chosen_word:
#         lives -= 1
#         #If lives goes down to 0 then the game should stop and it should print "You lose."
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

#     print(stages[lives])



#Step 5

import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed this letter. Guessed letter: {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(
            f"This letter is not in the chosen word. Guessed letter: {guess}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stages = hangman_art.stages
    print(stages[lives])

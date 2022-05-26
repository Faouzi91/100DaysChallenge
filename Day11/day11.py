############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
from replit import clear
from art import logo


def sum(num1, num2):
  return num1 + num2


def blackjack():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_choice = []
  cpu_choice = []
  hidden_card = []
  cpu_num = 0
  user_num = 0
  for i in range(0, 2):
    user_choice.append(random.choice(cards))
    cpu_choice.append(random.choice(cards))

  # hidden_card = cpu_choice.copy()
  # The op and the bottom does the same
  # On the botton we are slicing the list with [:]
  hidden_card = cpu_choice[:]
  hidden_card[1] = "_"
  print(user_choice, hidden_card)

  sum_user = sum(user_choice[0], user_choice[1])
  computer = sum(cpu_choice[0], cpu_choice[1])
  print(f"User: {sum_user}   Computer: {hidden_card[0]}")

  should_continue = False

  while not should_continue:
    if sum_user < 21:
      draw_more = input(
          "Do you want to get another card? Type 'y' to continue or type 'n' to stop: ")
      if draw_more == "y":
        user_num = random.choice(cards)
        sum_user = sum(sum_user, user_num)
        print(sum_user)
        if sum_user > 21:
          print(
              f"You exceeded the required score! You lose. Your score is {sum_user}")
          should_continue = True
        elif sum_user == 21:
          should_continue = True
      elif draw_more == "n":
        while computer < 16:
          cpu_num = random.choice(cards)
          computer = sum(computer, cpu_num)
          if computer > 16 and cpu_num == 11:
            computer -= 10
          if 11 in cpu_choice and computer > 21:
            cpu_choice[cpu_choice.indexof(11)] = 1
            computer = computer - 10
          print(computer)
          if computer > 21:
            print(f"You win!!! user: {sum_user} computer: {computer}")
        should_continue = True
    elif sum_user == 21:
      should_continue = True

  if sum_user == 21 and computer < 21:
    print("You win!!")

  if sum_user == 21 and computer == 21:
    print("You lose.")
    print(f"Your total is {user_choice} and the computer total is {computer}")
  elif sum_user == computer:
    print("It's a draw")
  elif sum_user < computer and computer <= 21:
    print(f"You lose. user: {sum_user} computer: {computer}")
  elif sum_user > computer and sum_user <= 21:
    print(f"You win!!! user: {sum_user} computer: {computer}")
  play_again = input(
      "Do you want o continue?: type 'yes' to continue or type 'no' to exit: ")
  if play_again == "yes":
    clear()
    return blackjack()
  else:
    should_continue = True


blackjack()

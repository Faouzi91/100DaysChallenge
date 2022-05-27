# select two random asset in the dictionary
# compare 2 asseeets and find the highest value
# if you win, Keep the second asset in other to ccompare it to the next random asset
# increment the score by 1 each time you win and keep the flow going until you lose
# if you lose shsow the show the score and exit the game
import random
from replit import clear
from art import logo, vs
from game_data import data


def generate_random():
  person = random.choice(data)
  return person


def game():
  A = generate_random()
  name = A["name"]
  followers_count = A["follower_count"]
  description = A["description"]
  country = A["country"]
  B = generate_random()
  name_b = B["name"]
  followers_count_b = B["follower_count"]
  description_b = B["description"]
  country_b = B["country"]

  score = 0
  game_over = False
  while not game_over:
    print(logo)
    if score > 0:
      print(f"You're right! Current score: {score}")
    print(f"Compare A: {name}, a {description}, from {country}.")
    print(vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (choice == "a" and (followers_count > followers_count_b)) or (choice == "b" and (followers_count < followers_count_b)):
      A = B
      name = A["name"]
      followers_count = A["follower_count"]
      description = A["description"]
      country = A["country"]
      B = generate_random()
      if A == B:
        B = generate_random()
      name_b = B["name"]
      followers_count_b = B["follower_count"]
      description_b = B["description"]
      country_b = B["country"]
      score += 1
      clear()
    elif (choice == "a" and (followers_count < followers_count_b)) or (choice == "b" and (followers_count > followers_count_b)):
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final score: {score}")
      play_again = input("Do you want to play again? Type 'yes' or 'no': ")
      if play_again == 'yes':
        clear()
        game()
      else:
        game_over = True
    else:
      score += 1


game()

import random


def start_game():
  print("Welcome to the Number Guessing Game")
  random_number = int(random.randint(1,9))
  attempt = 0
  print("\nThe random number is " + str(random_number)) #temporary
  while True:
    guess_number = input("Pick a number between 1 to 10: ")
    guess_number = int(guess_number)
    print("Guess number is = {}.\n".format(guess_number))
    attempt += 1

    if guess_number == random_number:
      break
    elif guess_number < random_number:
      print("Your guess number is LOWER than the answer!")
    elif guess_number > random_number:
      print("Your guess number is HIGHER than the answer!")
  return(attempt)

attempt = start_game()
print("CONGRATULATIONS, you got it! It took you {} tries".format(attempt))


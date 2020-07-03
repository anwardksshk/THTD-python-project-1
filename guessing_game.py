import random
high_score = None
attempt = None

def start_game(high_score):
  random_number = int(random.randint(1,10))
  attempt = 0
  print("The current high score is {}".format(high_score))
  #temporary
  print("\nThe random number is " + str(random_number)) 

  while True:
    guess_number = ""
    try:
      guess_number = int(input("\nPick a number between 1 to 10: "))
      if guess_number > 10 or guess_number < 1:
        raise ValueError("Your guess is outside the guessing range! Try again!")
    except ValueError as err:
      print("That is an invalid value! Please try again.")
      print("({})".format(err))
    except NameError:
      print("Name Error: Please try again.")
    else:
      print("Guess number is = {}.\n".format(guess_number))
      attempt += 1
      if guess_number == random_number:
        break
      elif guess_number < random_number:
        print("Your guess number is LOWER than the answer!")
      elif guess_number > random_number:
         print("Your guess number is HIGHER than the answer!")

  return(attempt)

print("Welcome to the Number Guessing Game")
attempt = start_game(high_score)
print("CONGRATULATIONS, you got it! It took you {} tries.".format(attempt))
if high_score == None or high_score > attempt:
  high_score = attempt
  print("You set a record! The new high score to beat is {}!".format(high_score))



play_again = input("\nWould you like to play again? (Y/N) -> ")
while play_again.lower() != 'n':
    attempt = start_game(high_score  )
    print("CONGRATULATIONS, you got it! It took you {} tries\n".format(attempt))
    if high_score == None or high_score > attempt:
      high_score = attempt
      print("You set a record! The new high score to beat is {}!".format(high_score))
    play_again = input("\nWould you like to play again? (Y/N) -> ")

print("===END GAME===")
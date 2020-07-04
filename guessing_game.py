import random
high_score = None
attempt = None

def welcome():
  print("Welcome to the Number Guessing Game")

def start_game(top_score):
  random_number = int(random.randint(1,10))
  attempt = 0
  print("The current high score: {}".format(high_score))
  while True:
    guess_number = ""
    try:
      guess_number = int(input("\nPick a number between 1 to 10: "))
      if guess_number > 10 or guess_number < 1:
        raise ValueError("Your guess is outside the guessing range! Try again!")
    except ValueError as err:
      print("That is an invalid value! Please try again.")
      print("({})".format(err))
    else:
      attempt += 1
      if guess_number == random_number:
        break
      elif guess_number < random_number:
        print("Your guess number is LOWER than the answer!")
      elif guess_number > random_number:
         print("Your guess number is HIGHER than the answer!")

  return(attempt)

def congratulations(number):
  print("CONGRATULATIONS, you got it! It took you {} tries.".format(number))


def set_highscore(current_score,top_score):
  global high_score
  if top_score == None or top_score >= current_score:
    high_score = current_score
    print("You set a record! The new high score to beat is {}!".format(high_score))
    
def endgame():
  print("===END GAME===")

def start_again():
  global high_score, attempt
  play_again = input("\nWould you like to play again? (Y/N) -> ")
  while play_again.lower() != 'n':
    attempt = start_game(high_score)
    congratulations(attempt)
    set_highscore(attempt,high_score)
    play_again = input("\nWould you like to play again? (Y/N) -> ")


# <==========================MAIN PROGRAM=============================>
welcome()
attempt = start_game(high_score)
congratulations(attempt)
set_highscore(attempt,high_score)
start_again()

endgame()
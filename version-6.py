import random as rd

play = True

while play:
  guesses_made = []
  counter = 5
  magic_number = rd.randint(1, 100)
  print(magic_number)
  
  guess = int(input("Guess a number between 1 and 100: "))


  while guess != magic_number and counter > 0:
    counter -= 1
    guesses_made.append(guess)
    print("Incorrect.")
    if guess > magic_number:
      print("Your guess was too high.")
    else:
      print("Your guess was too low.")
    print("%s guesses remain." % (counter))
    print("")
    if counter == 0:
      print("You lose!")
      break
    else:
      print("You have already guessed: %s" % guesses_made)
      guess = int(input("Guess again: "))
    
  else:
    print("You win!")
  
  play = input("Would you like to play again? (y/n)")
  
  if play == "y":
    play = True
  else:
    play = False
    

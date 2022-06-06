secret_word = "hi"
your_guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while your_guess != secret_word and not(out_of_guess):
   if guess_count < guess_limit:
      your_guess = input("Guess the animal name: ")      
      guess_count += 1
   else:
        out_of_guess = True
if out_of_guess:        
    print("Yow Lose")
else:
    print("You Win")
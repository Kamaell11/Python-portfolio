import random



def computer_guess(our_guess):
    
    chances = int(3 + ( our_guess / 20)) #optimal number of chances in my opinion
    guess = 0   
    print(f"I still have {chances} chances")
    while guess != our_guess and chances > 0:

        guess = random.randint(1 , guess_range)


        clue = input(f"My guess is {guess} if it's lower number type L, if it's higher type H or C if I guessed! : ")

        if clue == "L":
            guess = random.randint(1 , (guess-1))
            chances -= 1
            print(f"I still have {chances} chances")
            

        elif clue == "H":
            guess = random.randint((guess+1), guess_range)
            chances -= 1
            print(f"I still have {chances} chances")

        elif clue == "C":
            print("I have guessed!")


        if chances == 0:
            print("Game over, I lost!")

    
            
guess_range = int(input('Type the range of the numbers for computer to guess: '))
our_guess = int(input('Type the number for computer to guess: '))


computer_guess(our_guess)
import random

def guess(x):
    random_number = random.randint(1 , x)
    chances = int(3 + ( x / 20)) #optimal number of chances in my opinion
    guess = 0
    print(f"You still have {chances} chances")
    while guess != random_number and chances > 0:
        if chances == 0:
            print("Game over, You lost!")
        guess = int(input(f'Guess the number beetween 1 and {x}: '))


        if guess < random_number:
            print("Try higher!")
            chances -= 1
            print(f"You still have {chances} chances")
            

        elif guess > random_number:
            print("Try smaller")
            chances -= 1
            print(f"You still have {chances} chances")

        else:
            print("You have quested the number!")
            
    
    

x = int(input("Type last number of range: "))
        
guess(x)


    
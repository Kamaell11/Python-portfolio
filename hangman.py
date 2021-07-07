import random
import string
words = ["haslo", "pies", "ocean", "Konstantynopol"]

def get_valid_word(words):
    word = random.choice(words)  #chose one word to guess from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def play_hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #guessed by user

    chances = 5

   
    while len(word_letters) > 0 and chances > 0:
        # letters used by user
        
        print("You still  have: {chances}, chances left and You've used these letters: ".join(used_letters))

        # currently word status, with guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
       
        print("Current word to guess is: ".join(word_list))

        user_letter = input('Type a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                chances -=  1  
                print(f"This letter {user_letter} is not in the word ")

        elif user_letter in used_letters:
            print("Please try another letter, You tried this one")

        else:
            print("Type a valid letter, please")

    
    if chances == 0:
        
        print(f"You've lost! The word to guess was: {word}")
    else:
        print(f"Congratulations! You've guessed the word {word}")


play_hangman()


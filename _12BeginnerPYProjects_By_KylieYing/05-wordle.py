import random
import string
from wordlistExample import wordlist

def get_valid_word(wordlist):
    word = "-"
    while '-' in word or "" in word:
        word = random.choice(wordlist)
    return word.upper()

def wordle():
    word = get_valid_word(wordlist)
    words = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    while len(words) > 0:
        print("These Letters Are Already Picked: ", "".join(used_letters))
        wordle_list = [letter if letter in used_letters \
                              else "_" \
                              for letter in word]
        print("Current Word: ", "".join(wordle_list))
        user_guess = input("A single letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if used_letters in words:
                words.remove(used_letters)
        elif user_guess in used_letters:
            print("You had this before")
        else:
            print("None of them works")

print(len(random.choice(wordlist)))

import random
import string
from wordlistExample import wordlist

def get_valid_word(wordlist):
    wordChoice = random.choice(wordlist)
    while "-" in wordChoice or " " in wordChoice:
        wordChoice = random.choice(wordlist)
    return wordChoice.upper()

def wordle():
    word = get_valid_word(wordlist)
    words = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    countNum = len(word) + 3

    while countNum:
        countNum = countNum - 1
        print("These Letters Are Already Picked: ", "".join(used_letters))
        wordle_list = [letter if letter in used_letters \
                              else "_" \
                              for letter in word]
        print("Current Word: ", " ".join(wordle_list))
        user_guess = input("A single letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if used_letters in words:
                words.remove(used_letters)
        elif user_guess in used_letters:
            print("You had this before")
        elif "_" not in " ".join(wordle_list):
            print("You nailed it")
    print(f"You lost, the word is {word}")

    

if __name__ == "__main__":
    wordle()
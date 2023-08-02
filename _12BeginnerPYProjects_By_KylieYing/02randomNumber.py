import random

def guess(user_input):
    random_num = random.randint(1, user_input)
    _guessing = 0
    while _guessing != random_num:
        _guessing = int(input(f"Guess a number: "))
        if _guessing < random_num:
            print("try something bigger")
        elif _guessing > random_num:
            print("Try something smaller")
        
    print("u got it")

def computer_guess(user_input):
    min, max = 0, user_input
    response = ""
    _guessing = random.randint(min, max)
    while response != "c":
        response = input(f"Is { _guessing} too hifigh (H), too low (L), or correct (C)").lower()
        if response == "h":
            max = _guessing
            _guessing = random.randint(min, _guessing - 1)

        elif response == "l":
            min = _guessing
            _guessing = random.randint(_guessing + 1, max)
    print("OK")


user_input = int(input("終極密碼範圍： "))
guess(user_input)
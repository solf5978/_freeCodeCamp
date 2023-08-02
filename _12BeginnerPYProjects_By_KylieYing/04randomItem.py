import random

def play():
    player = input(" r4Rock, p4Paper, s4Scissors What's your draw: ").lower()
    ai = random.choice(["r", "p", "s"])
    return competit(player, ai)

def competit(player, ai):
    print(player, ai)
    if player == ai:
        return play()
    elif (player == "r" and ai == "s") or \
        (player == "p" and ai == "r") or \
        (player == "s" and ai == "p"):
        print("you win")
    else:
        print("you lost")

play()
        
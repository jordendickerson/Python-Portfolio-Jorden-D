import blackjackClasses as bj
from commonGameFunctions import *
import commonGameFunctions as cgf
from blackjackClasses import *
import random


def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = ask_number("How many players? (1-7)")
    for i in range(int(number)):
        name = input("Enter the players name")
        names.append(name)
    game = Bj_Game(names)
    again = None
    while again != "n":
        game.play()
        again = ask_yes_no("\nDo you want to play again? (y/n)")

main()
import blackjackClasses as bj

from commonGameFunctions import *
from warClass import *

import random


def main():
    p1 = input("What is Player One's name? ")
    p2 = input("What is Player Two's name? ")
    table = Table([p1, p2])
    table.deal_cards()
    table.play_all()
    exit = input("press any key to exit")

def print_underline(string, line):
    print('\n{}\n{}'.format(string, line * len(string)))




main()
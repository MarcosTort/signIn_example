from colorama import init, Fore
import data
import random


def ShowOptions():
    while True:
        init(autoreset=True)
        print('Choose a behaviour')
        print(Fore.GREEN + '1- Positive')
        print(Fore.RED + '2- Negative')
        choice = int(input())
        if choice == 1:
            lists = data.validData

        elif choice == 2:
            lists = random.choice(data.negative)

        else:
            print('Choose 1 or 2')
        return lists

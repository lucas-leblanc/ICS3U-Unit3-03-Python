# Copyright (c) 2022 Lucas LeBlanc All rights reserved.
#
# Created by: Lucas LeBlanc
# Created on: Oct 2022
# ICS3U-Unit3-03.py File, learning if...then...else... statements in python.

import random


def main():

    # input and variables
    random_number = random.randint(0, 9)
    guess_number = int(input("Guess the number from 0 to 9: "))

    # process and output
    if guess_number == random_number:
        print("\nYou guessed right.")
    else:
        print("\nYou guessed wrong, the number was {}.".format(random_number))

    print("\n\nDone.")


if __name__ == "__main__":
    main()

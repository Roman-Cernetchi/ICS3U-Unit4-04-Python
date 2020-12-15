#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program finds the magic number

import random


def main():
    # This function calculates the magic number

    random_number = random.randint(0, 9)  # A number between 0 and 9
    print("")

    # process
    while True:
        # Input
        chosen_integer_string = input("Enter a number between 0 and 9: ")
        try:
            chosen_number = int(chosen_integer_string)

            assert chosen_number >= 0

            if random_number > chosen_number:
                print("Too low, please try again")
            elif chosen_number > random_number:
                print("Too high, please try again")
            else:
                print("Correct!")
                break

        except AssertionError:
            print("Integer wasn't positive")
        except Exception:
            print("This was not an integer")


if __name__ == "__main__":
    main()

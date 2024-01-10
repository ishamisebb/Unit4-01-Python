#!/usr/bin/env python3
# Created by: Ishami Sebgoya
# Created on: November 14, 2023
# This program adds up numbers in a loop for a sum


def main():
    try:
        # initialize the loop counter and sum
        loop_counter = 0
        sum_result = 0

        # get the user number as a string
        user_input = input("Enter a positive number: ")
        user_number = int(user_input)
        print("")

        # calculate the sum of all numbers from 0 to user number
        while loop_counter <= user_number:
            sum_result += loop_counter
            print("Tracking {0} times through loop.".format(loop_counter))
            loop_counter += 1

        print("")
        print(
            "The sum of the numbers from 0 to {} is: {}.".format(
                user_number, sum_result
            )
        )
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()

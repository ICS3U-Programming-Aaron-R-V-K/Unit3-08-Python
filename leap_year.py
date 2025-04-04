# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 04, 2025
# Determines if the year is a leap year or not


def main():
    # Initial explanation to the user
    print("\nDetermines if the year is a leap year or not")

    # Get user year as a string
    year_num = input("Enter a year: ")

    # Try catch statement to validate the user input as an integer
    try:
        year_int = int(year_num)

        # Nested If statements
        #  If statement if the year number as int is 0 or less than 0, so they enter a positive number
        if year_int > 0:

            # If statement if year number as int is divisible by four
            if year_int % 4 == 0:

                # If statement if year num as int is divisible by 100
                if year_int % 100 == 0:

                    # If statement if year num as int is divisible by 400
                    if year_int % 400 == 0:
                        print("{}, Is a leap year".format(year_int))
                    else:
                        print("{}, Is not a leap year".format(year_int))
                else:
                    print("{}, Is a leap year".format(year_int))
            else:
                print("{}, Is not a leap year".format(year_int))
        else:
            print("Enter a positive number")

    # Exception for Try catch if it is an invalid input
    except Exception:
        print("{}, Is an invalid input".format(year_num))

    # Finally statement for every answer
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

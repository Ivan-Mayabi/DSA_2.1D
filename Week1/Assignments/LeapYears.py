""""Exercise 2: """
def is_leap() -> bool:
    # Display a prompt for a year
    print("Please input the year on the next line: ")
    print()
    # Define the year variable and allow it to take in input, type cast to int
    year: int = int(input())

    # Define the return
    leap_year: bool

    # Do the check
    # If it is divisible by 4 do these tests
    if (year % 4) == 0:
        # If it is divisible by 4 and also by 100 do these tests
        if (year % 100) == 0:
            # If it is divisible by 4, 100 and 400 -> it is Leap
            if (year % 400) == 0:
                leap_year = True
                # If it is divisible by 4, 100 and not by 400 -> not Leap
            else:
                leap_year = False
        # If it is divisible by 4 only -> leap
        else:
            leap_year = True
    # If it is not divisible by 4 -> it is not Leap
    else:
        leap_year = False
    #Return the leap year
    return leap_year

#Execute the program
print(is_leap())
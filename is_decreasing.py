# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-26-2022
# Description: Recursive function that take parameter as list of numbers and returns true if the elements of the list
# are strictly decreasing and False if otherwise.

def is_decreasing(numbers):
    """Returns true if list of numbers given are strictly decreasing, otherwise returns false."""
    if len(numbers) <= 1:
        return True
    elif numbers[0] > numbers[1]:
        return is_decreasing(numbers[1:])
    else:
        return False


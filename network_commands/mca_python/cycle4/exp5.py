def add_integers(*args):
    """
    Adds variable-length integer arguments.

    Parameters:
    *args (int): Variable number of integer arguments.

    Returns:
    int: Sum of the integer arguments.
    """
    total = 0
    for num in args:
        if isinstance(num, int):
            total += num
        else:
            raise TypeError("Arguments must be integers.")
    return total

user_input = input("Enter integers separated by spaces: ")
user_numbers = [int(num) for num in user_input.split()]
try:
    result = add_integers(*user_numbers)
    print(f"Result: {result}")
except TypeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter valid integers.")


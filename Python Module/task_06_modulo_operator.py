'''
#Name: Prasanna Sai
#objective: Use the modulo operator with function + validation + clean output.
#task: Check if a number is even or odd using %.
'''

def is_even_or_odd(number):
    """
    Validates if input is an integer, computes the remainder using %,
    and returns 'Even' or 'Odd'.
    """
    # Validation logic
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    # Compute remainder
    remainder = number % 2
    
    if remainder == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    number = 17
    
    try:
        result = is_even_or_odd(number)
        print(f"Number: {number}")
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Validation Error: {e}")

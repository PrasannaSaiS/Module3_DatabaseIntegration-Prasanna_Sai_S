'''
#Name: Prasanna Sai
#objective: Two-way decision using functions + validation + formatted output.
#task: Check if a number is even or odd.
'''

def determine_even_or_odd(num):
    """
    Validates input is an integer and checks if it's even or odd using if-else.
    """
    # Validation logic
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")
        
    # If-Else logic
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    # Specified variable
    num = 8
    
    try:
        result = determine_even_or_odd(num)
        print(f"Number: {num}")
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Validation Error: {e}")

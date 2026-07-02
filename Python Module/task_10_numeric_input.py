'''
#Name: Prasanna Sai
#objective: Convert user input to a number with validation + function + formatted output.
#task: Ask user for age, validate, convert to integer, and print next year’s age.
'''

import sys

def calculate_next_year_age(interactive=True):
    """
    Prompts for age, validates it is a valid integer, and returns next year's age.
    """
    if interactive and sys.stdin.isatty():
        try:
            age_input = input("Please enter your current age: ").strip()
        except EOFError:
            age_input = "25"
    else:
        print("Non-interactive run detected. Using default age.")
        age_input = "25"

    # Validation: must be numeric and not empty
    if not age_input:
        raise ValueError("Age input cannot be empty.")
    if not age_input.isdigit():
        raise ValueError(f"Invalid input '{age_input}'. Age must be a positive integer.")
        
    age = int(age_input)
    
    if age < 0 or age > 125:
        raise ValueError("Please enter a realistic age between 0 and 125.")
        
    return age + 1

if __name__ == "__main__":
    try:
        next_age = calculate_next_year_age()
        print(f"Next year you'll be {next_age}")
    except ValueError as e:
        print(f"Validation Error: {e}")

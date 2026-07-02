'''
#Name: Prasanna Sai
#objective: Read and validate user input using a function + formatted output.
#task: Get the user’s name and greet them.
'''

import sys

def get_and_validate_name(interactive=True):
    """
    Prompts the user for their name, validates that it is not blank,
    and returns a formatted greeting.
    """
    if interactive and sys.stdin.isatty():
        try:
            name_input = input("Enter your name: ").strip()
        except EOFError:
            name_input = "Guest"
    else:
        # Fallback for non-interactive test runs
        print("Non-interactive run detected. Using default name.")
        name_input = "Prasanna"

    if not name_input:
        raise ValueError("Input cannot be empty. Please enter a valid name.")
        
    return f"Hello, {name_input}! Welcome to the Python training module."

if __name__ == "__main__":
    try:
        greeting = get_and_validate_name()
        print(greeting)
    except ValueError as e:
        print(f"Validation Error: {e}")

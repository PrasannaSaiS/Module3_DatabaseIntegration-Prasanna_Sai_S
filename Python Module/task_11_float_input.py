'''
#Name: Prasanna Sai
#objective: Handle decimal input with validation + function + formatted output.
#task: Convert weight from kilograms to pounds.
'''

import sys

def convert_kg_to_lbs(kg_value):
    """
    Validates the kilogram input and converts it to pounds.
    """
    if not isinstance(kg_value, (int, float)):
        raise TypeError("Weight must be a numeric value.")
    if kg_value < 0:
        raise ValueError("Weight cannot be a negative value.")
        
    return kg_value * 2.20462

if __name__ == "__main__":
    # Handle environment (interactive vs non-interactive)
    if sys.stdin.isatty():
        try:
            input_val = input("Enter weight in kilograms: ").strip()
            kg = float(input_val)
        except ValueError:
            print("Invalid numeric value entered. Defaulting to 10.0 kg.")
            kg = 10.0
        except EOFError:
            kg = 10.0
    else:
        print("Non-interactive run detected. Using default 10.0 kg.")
        kg = 10.0

    try:
        lbs = convert_kg_to_lbs(kg)
        print(f"Weight in Kilograms: {kg:.2f} kg")
        print(f"Weight in Pounds:    {lbs:.2f} lbs")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

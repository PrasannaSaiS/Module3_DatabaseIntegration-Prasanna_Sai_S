'''
#Name: Prasanna Sai
#objective: Use a condition-based loop with validation + function + formatted output.
#task: Countdown from 5 to 1 using a while loop.
'''

def perform_countdown(start_count):
    """
    Validates starting count value and counts down to 1 using a while loop.
    """
    # Validation logic
    if not isinstance(start_count, int):
        raise TypeError("Countdown start value must be an integer.")
    if start_count <= 0:
        raise ValueError("Countdown start value must be a positive integer.")
        
    count = start_count
    print(f"Initiating countdown from {count}:")
    
    # Use while count > 0
    while count > 0:
        print(f"Count: {count}")
        # Decrease using count -= 1
        count -= 1
        
    print("Blast off!")

if __name__ == "__main__":
    try:
        perform_countdown(5)
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

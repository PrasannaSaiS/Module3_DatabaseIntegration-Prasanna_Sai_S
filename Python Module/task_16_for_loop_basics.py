'''
#Name: Prasanna Sai
#objective: Iterate a fixed number of times with a function + validation + formatted output.
#task: Print numbers from 1 to 5 using range().
'''

def print_numbers_in_range(loop_count):
    """
    Validates that the loop count is a positive integer and uses a for-loop
    with range() to print numbers starting from 1 up to the loop_count.
    """
    # Validation logic
    if not isinstance(loop_count, int):
        raise TypeError("Loop count must be an integer.")
    if loop_count <= 0:
        raise ValueError("Loop count must be greater than zero.")
        
    print(f"Iterating {loop_count} times using range({loop_count}):")
    # Use for i in range(loop_count) - printing numbers 1 to loop_count
    for i in range(loop_count):
        print(f"Number: {i + 1}")

if __name__ == "__main__":
    try:
        # Standard input limit is 5 as requested by the task
        print_numbers_in_range(5)
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

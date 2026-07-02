'''
#Name: Prasanna Sai
#objective: Use a break statement to exit a loop early with function + validation + clean output.
#task: Find and print the first even number in a given range.
'''

def find_first_even_in_range(start_val, end_val):
    """
    Validates range, loops over it, checks for even using %, and breaks on first even.
    """
    # Validation logic
    if not isinstance(start_val, int) or not isinstance(end_val, int):
        raise TypeError("Range boundaries must be integers.")
        
    range_size = end_val - start_val
    if range_size < 0:
        raise ValueError("Invalid range: end value must be greater than or equal to start value.")
        
    print(f"Searching for the first even number in range({start_val}, {end_val + 1}):")
    
    first_even = None
    # Loop with for i in range(...)
    for i in range(start_val, end_val + 1):
        # Use modulo % to check even
        if i % 2 == 0:
            first_even = i
            # Break once the first even is found
            break
            
    return first_even

if __name__ == "__main__":
    try:
        # Testing with range 11 to 20. The first even should be 12.
        result = find_first_even_in_range(11, 20)
        if result is not None:
            print(f"First even number found: {result}")
        else:
            print("No even number found in the range.")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

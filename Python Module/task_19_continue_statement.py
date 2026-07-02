'''
#Name: Prasanna Sai
#objective: Use continue to skip even numbers, with a function + validation + formatted output.
#task: Sum only the odd numbers in a given range.
'''

def sum_odds_in_range(limit):
    """
    Loops through range(limit), skips even numbers using continue, and sums odd numbers.
    """
    # Validation logic
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")
        
    odd_sum = 0
    print(f"Analyzing numbers from 0 to {limit - 1}:")
    
    # Loop with range(...)
    for i in range(limit):
        # Skip even numbers using continue
        if i % 2 == 0:
            continue
        
        # Accumulate only odd numbers
        print(f"Adding odd number: {i}")
        odd_sum += i
        
    return odd_sum

if __name__ == "__main__":
    try:
        # Testing with range(10) as instructed
        total = sum_odds_in_range(10)
        print(f"Sum of odd numbers in range(10): {total}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

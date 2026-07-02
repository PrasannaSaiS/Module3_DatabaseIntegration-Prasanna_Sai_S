'''
#Name: Prasanna Sai
#objective: Perform integer division with function + validation + formatted output.
#task: Split a total bill equally among people.
'''

def calculate_individual_share(total_bill, people):
    """
    Validates inputs and splits the bill using floor division (//).
    """
    # Validation logic
    if not isinstance(total_bill, (int, float)) or total_bill <= 0:
        raise ValueError("Total bill must be a positive numeric value.")
    if not isinstance(people, int) or people <= 0:
        raise ValueError("Number of people must be a positive integer.")
    
    # Floor division
    individual_share = total_bill // people
    return individual_share

if __name__ == "__main__":
    # Given variables
    total_bill = 1250
    people = 4
    
    try:
        share = calculate_individual_share(total_bill, people)
        print(f"Total Bill: ${total_bill:.2f}")
        print(f"Number of People: {people}")
        print(f"Individual Share (using floor division): ${share}")
    except ValueError as e:
        print(f"Validation Error: {e}")

'''
#Name: Prasanna Sai
#objective: Basic conditional with function, validation, and user interaction.
#task: Check if a student passes based on marks.
'''

def check_passing_status(marks, passing_threshold=50):
    """
    Validates the marks and returns 'Pass' or 'Fail' based on the threshold.
    """
    # Validation logic
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a number.")
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100 (inclusive).")
        
    # Simple if structure
    if marks >= passing_threshold:
        return "Pass"
    
    return "Fail"

if __name__ == "__main__":
    # Specified variable
    marks = 75
    
    try:
        status = check_passing_status(marks)
        print(f"Student Marks: {marks}")
        print(f"Result: {status}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

'''
#Name: Prasanna Sai
#objective: Multi-way decision using functions + validation + structured output.
#task: Assign a grade based on the score.
'''

def calculate_grade(score):
    """
    Validates score (0-100) and returns a grade along with descriptive feedback.
    """
    # Validation logic
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value (int or float).")
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100 (inclusive).")
        
    # Multi-way decision logic (enhanced version with descriptors)
    if score >= 90:
        grade = "A+"
        remarks = "Excellent / Outstanding performance!"
    elif score >= 80:
        grade = "A"
        remarks = "Very Good / Highly commendable."
    elif score >= 70:
        grade = "B"
        remarks = "Good effort / Steady progress."
    elif score >= 60:
        grade = "C"
        remarks = "Satisfactory / Room for improvement."
    else:
        grade = "Fail"
        remarks = "Needs Improvement / Please study harder."
        
    return grade, remarks

if __name__ == "__main__":
    # Given variable
    score = 88
    
    try:
        grade, feedback = calculate_grade(score)
        print("Grade Report Summary:")
        print("--------------------")
        print(f"Score:    {score}")
        print(f"Grade:    {grade}")
        print(f"Remarks:  {feedback}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

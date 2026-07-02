'''
#Name: Prasanna Sai
#objective: Use built-in min() and max() with validation + function + structured output.
#task: Find the highest and lowest salary in a list.
'''

def get_salary_extremes(salary_list):
    """
    Validates a list of salaries and returns the minimum and maximum salary.
    """
    # Validation logic
    if not isinstance(salary_list, list):
        raise TypeError("Salaries must be passed in a list format.")
    if len(salary_list) == 0:
        raise ValueError("The salary list cannot be empty.")
    if not all(isinstance(salary, (int, float)) and salary >= 0 for salary in salary_list):
        raise ValueError("All salaries must be non-negative numeric values.")
    
    # Compute min and max
    lowest = min(salary_list)
    highest = max(salary_list)
    
    return lowest, highest

if __name__ == "__main__":
    # Given list
    salaries = [50000, 75000, 62000, 95000]
    
    try:
        lowest_sal, highest_sal = get_salary_extremes(salaries)
        print("Salary Analysis Summary:")
        print("------------------------")
        print(f"Salary List: {salaries}")
        print(f"Lowest Salary:  ${lowest_sal:,.2f}")
        print(f"Highest Salary: ${highest_sal:,.2f}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

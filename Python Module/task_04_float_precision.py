'''
#Name: Prasanna Sai
#objective: Handle floating-point arithmetic with functions + validation + formatted output.
#task: Calculate net salary after tax and print with 2 decimals.
'''

def calculate_net_salary(salary, tax_rate):
    """
    Validates input and calculates the net salary after subtracting tax.
    """
    # Validation logic
    if not isinstance(salary, (int, float)) or salary < 0:
        raise ValueError("Salary must be a non-negative numeric value.")
    if not isinstance(tax_rate, (int, float)) or not (0 <= tax_rate <= 1):
        raise ValueError("Tax rate must be a number between 0 and 1 (inclusive).")
    
    # Calculation
    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount
    return net_salary

if __name__ == "__main__":
    # Given variables
    salary = 75000.5
    tax_rate = 0.18
    
    try:
        net_val = calculate_net_salary(salary, tax_rate)
        print(f"Gross Salary: ${salary:.2f}")
        print(f"Tax Rate: {tax_rate * 100:.1f}%")
        print(f"Net Salary (after 18% tax): ${net_val:.2f}")
    except ValueError as e:
        print(f"Validation Error: {e}")

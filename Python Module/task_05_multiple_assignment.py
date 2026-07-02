'''
#Name: Prasanna Sai
#objective: Use multiple assignment with basic validation + function + formatted output.
#task: Unpack (x, y) coordinates and display them.
'''

def unpack_coordinates(coords):
    """
    Validates a coordinate container and unpacks them using multiple assignment.
    """
    # Validation logic
    if not isinstance(coords, (list, tuple)):
        raise TypeError("Coordinates input must be a list or tuple.")
    if len(coords) != 2:
        raise ValueError("Coordinates must contain exactly two values (x, y).")
    if not all(isinstance(c, (int, float)) for c in coords):
        raise TypeError("All coordinate elements must be numeric (int or float).")
    
    # Multiple assignment
    x, y = coords
    return x, y

if __name__ == "__main__":
    test_coords = (10.5, -25.3)
    
    try:
        x_val, y_val = unpack_coordinates(test_coords)
        print(f"Successfully unpacked coordinates.")
        print(f"X-Coordinate: {x_val:.2f}")
        print(f"Y-Coordinate: {y_val:.2f}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")

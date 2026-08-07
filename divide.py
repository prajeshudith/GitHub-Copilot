def divide(x, y):
    """Divides two numbers and returns the result.

    Args:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float: The result of the division.
    """
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x / y
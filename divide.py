def divide(a, b):
    """Divides two numbers and returns the result.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
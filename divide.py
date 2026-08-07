def divide(c, d):
    """Divides two numbers and returns the result.

    Args:
        c (float): The numerator.
        d (float): The denominator.

    Returns:
        float: The result of the division.
    """
    if d == 0:
        raise ValueError("Denominator cannot be zero.")
    return c / d
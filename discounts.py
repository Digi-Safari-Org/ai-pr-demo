def calculate_discount(price, discount):
    """
    Calculate the discounted price.

    Args:
        price (float or int): The original price.
        discount (float or int): The discount rate (0 <= discount <= 1).

    Returns:
        float: The price after applying the discount.

    Raises:
        ValueError: If inputs are invalid.
    """
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number (int or float).")
    if not isinstance(discount, (int, float)):
        raise ValueError("Discount must be a number (int or float).")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1 (inclusive).")

    return price - (price * discount)

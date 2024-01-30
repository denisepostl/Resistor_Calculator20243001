def calculate_series(resistances):
    """
    Calculate the total resistance in a series circuit.

    Parameters:
    - resistances (list): A list of resistance values in ohms.

    Returns:
    - float: The total resistance in ohms, rounded to 3 decimal places.
    """
    total_resistance = sum(resistances)
    return round(total_resistance, 3)

def calculate_parallel(resistances):
    """
    Calculate the total resistance in a parallel circuit.

    Parameters:
    - resistances (list): A list of resistance values in ohms.

    Returns:
    - float: The total resistance in ohms, rounded to 3 decimal places.
    """
    reciprocal_sum = sum(1 / r for r in resistances)
    total_resistance = 1 / reciprocal_sum
    return round(total_resistance, 3)

from r_calculator import calculate_series, calculate_parallel
import pytest

def test_calculate_series():
    """
    Test the calculate_series function.

    Checks if the sum of resistances in series is calculated correctly.

    Parameters:
    - None

    Returns:
    - None
    """
    resistances = [10, 20, 30, 40]
    expected_result = sum(resistances)
    assert calculate_series(resistances) == expected_result

def test_calculate_parallel():
    """
    Test the calculate_parallel function.

    Checks if the reciprocal sum of resistances in parallel is calculated correctly.

    Parameters:
    - None

    Returns:
    - None
    """
    resistances = [10, 20, 30, 40]
    reciprocal_sum = sum(1 / r for r in resistances)
    expected_result = 1 / reciprocal_sum
    assert calculate_parallel(resistances) == expected_result

def test_calculate_parallel_with_zero_resistance():
    """
    Test the calculate_parallel function with zero resistance.

    Checks if the function raises a ZeroDivisionError when there is a zero resistance.

    Parameters:
    - None

    Returns:
    - None
    """
    resistances = [10, 0, 30, 40]
    with pytest.raises(ZeroDivisionError):
        calculate_parallel(resistances)

def test_calculate_parallel_with_empty_list():
    """
    Test the calculate_parallel function with an empty list of resistances.

    Checks if the function raises a ZeroDivisionError when the resistance list is empty.

    Parameters:
    - None

    Returns:
    - None
    """
    resistances = []
    with pytest.raises(ZeroDivisionError):
        calculate_parallel(resistances)

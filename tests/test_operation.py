"""
@overview A test file
"""

from operation.operation import Operation





# Initialize GuessMime class
obj_op = Operation()



def test_factorial_positive_value():
    """
    @overview Test factorial for a positive integer value.
    This test will return the factorial of an integer value : i >= 1
    """

    fac_value = obj_op.factorial(5)
    assert fac_value == 120, f"Expected '120' but got {fac_value}"



def test_factorial_negative_value():
    """
    @overview Test factorial for a negative integer value.
    This test will return `None`.
    """

    fac_value = obj_op.factorial(-5)
    assert fac_value is None, f"Expected 'None' but got {fac_value}"

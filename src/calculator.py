def fun1 (x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    """
    return x + y

def fun2 (x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    """
    return x - y

def fun3 (x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    """
    return x * y

def fun4(x,y):
    """
    Adds the results of fun1, fun2, and fun3 together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of fun1, fun2, and fun3.
        Raises:
            ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    f1_result = fun1(x,y)
    f2_result = fun2(x,y)
    f3_result = fun3(x,y)
    total = f1_result + f2_result + f3_result
    return total


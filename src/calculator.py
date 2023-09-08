def fun1 (x, y):
    return x + y

def fun2 (x, y):
    return x - y

def fun3 (x, y):
    return x * y

def fun4(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    f1_result = fun1(x,y)
    f2_result = fun2(x,y)
    f3_result = fun3(x,y)
    total = f1_result + f2_result + f3_result
    return total


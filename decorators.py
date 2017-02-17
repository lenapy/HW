def check_data_type(func):
    def wrapper(*args):
        for elem in args:
            if not isinstance(elem, (int, float)):
                raise ValueError("data type must be int or float")
            f = func(*args)
            return f
    return wrapper


def check_zero_value(func):
    def wrapper(*args):
        if 0 in args:
            raise ZeroDivisionError('value must be not zero')
        f = func(*args)
        return f
    return wrapper


@check_data_type
def summ_(a, b):
    return a + b


@check_data_type
def substr(a, b):
    return a - b


@check_data_type
def mul(a, b):
    return a * b


@check_data_type
@check_zero_value
def division(a, b):
    return a / b




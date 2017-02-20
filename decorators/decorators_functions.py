def check_data_type(allowed_data_types=None):
    allowed_data_types = allowed_data_types if allowed_data_types else (int, float)

    def decorator(func):
        def wrapper(a, b):
            wrapper.__name__ = func.__name__
            if not isinstance(a, allowed_data_types):
                raise ValueError("invalid data type")
            elif not isinstance(b, allowed_data_types):
                raise TypeError("second value has different data type")
            f = func(a, b)
            return f
        return wrapper
    return decorator


def check_zero_value(func):
    def wrapper(a, b):
        if b == 0:
            raise ZeroDivisionError('value must be not zero')
        f = func(a, b)
        return f
    return wrapper


@check_data_type()
def summ_(a, b):
    return a + b


@check_data_type()
def substr(a, b):
    return a - b


@check_data_type()
def mul(a, b):
    return a * b


@check_data_type()
@check_zero_value
def division(a, b):
    return a / b



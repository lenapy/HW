import unittest

from decorators import decorators_functions
from decorators.decorators_functions import check_zero_value, check_data_type


class TestFunctions(unittest.TestCase):
    def test_add(self):
        res = decorators_functions.summ_(1, 1)
        self.assertEqual(2, res)

    def test_sub(self):
        res = decorators_functions.substr(2, 1)
        self.assertEqual(1, res)

    def test_mul(self):
        res = decorators_functions.mul(2, 2)
        self.assertEqual(4, res)

    def test_div(self):
        res = decorators_functions.division(4, 2)
        self.assertEqual(2, res)


class TestDecoratorFunc(unittest.TestCase):
    def test_check_zero_value_with_zero_value(self):
        @check_zero_value
        def div(a, b):
            return a / b
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)

    def test_check_zero_value_without_zero(self):
        @check_zero_value
        def div(a, b):
            return a / b
        self.assertEqual(2, div(4, 2))

    def test_check_data_type(self):
        @check_data_type()
        def summ_val(a, b):
            return a + b
        self.assertEqual(4, summ_val(2, 2))

    def test_check_data_type_first_value_str(self):
        @check_data_type()
        def summ_val(a, b):
            return a + b
        with self.assertRaises(ValueError):
            summ_val('2', 2)

    def test_check_data_type_second_value_str(self):
        @check_data_type()
        def summ_val(a, b):
            return a + b
        with self.assertRaises(TypeError):
            summ_val(2, '2')

    def test_check_data_type_attributes(self):
        @check_data_type(str)
        def summ_val(a, b):
            return a + b
        self.assertEqual('22', summ_val('2', '2'))

    def test_check_data_type_attributes_not_valid_values_in_func(self):
        @check_data_type((str, float))
        def summ_val(a, b):
            return a + b
        with self.assertRaises(ValueError):
            summ_val(2, 2.1)


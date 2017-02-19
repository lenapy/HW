from decorators import decorators_functions
import unittest


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
        with self.assertRaises(ZeroDivisionError):
            func = decorators_functions.division(4, 0)
            decorators_functions.check_zero_value(func)

    # def test_check_zero_value_without_zero(self):
    #     func = decorators_functions.division(4, 2)
    #     res = decorators_functions.check_zero_value(func)
    #     self.assertEqual(2, res)

    def test_check_data_type_first_value_str(self):
        with self.assertRaises(ValueError):
            func = decorators_functions.summ_('2', 2)
            decorators_functions.check_data_type(func)

    def test_check_data_type_second_value_str(self):
        with self.assertRaises(TypeError):
            func = decorators_functions.summ_(2, '2')
            decorators_functions.check_data_type(func)

    # def test_check_data_type_attributes(self):
    #     with self.assertRaises(ValueError):
    #         func = decorators_functions.summ_(2, 2)
    #         decorators_functions.check_data_type(str)

    # def test_check_data_type(self):
    #     with self.assertRaises(ValueError):
    #         func = decorators_functions.division(4, 2)
    #         decorators_functions.check_zero_value(func)
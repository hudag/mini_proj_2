import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data1 = CsvReader('Tests/Data/Addition.csv').data
        for row in test_data1:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sub_method_calculator(self):
        test_data2 = CsvReader('Tests/Data/Subtraction.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_mult_method_calculator(self):
        test_data = CsvReader('Tests/Data/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_div_method_calculator(self):
        test_data = CsvReader('Tests/Data/Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squared_method_calculator(self):
        test_data = CsvReader('Tests/Data/Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.doubled(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_root_method_calculator(self):
        test_data = CsvReader('Tests/Data/SquareRoot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sq_root(float(row['Value 1'])), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
import unittest
import math
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/dataset.csv')
        self.test_data = CsvReader('Tests/Data/answers.csv').data

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean(self):
        for row in self.test_data:
            self.assertEqual(self.statistics.mean(),float(row['Result Mean']) )

    def test_population_standard_deviation(self):
        for row in self.test_data:
            self.assertEqual(round(self.statistics.stdev(),8),float(row['Result PStdev']) )

    def test_variance_of_population_portion(self):
        for row in self.test_data:
            self.assertEqual(round(self.statistics.popvar(),8), round(float(row['Result Variance']),8))

    def test_median(self):
        for row in self.test_data:
            self.assertEqual(self.statistics.median(), float(row['Result Median']))


if __name__ == '__main__':
    unittest.main()
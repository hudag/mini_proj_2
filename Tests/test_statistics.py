import unittest
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/dataset.csv')

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean(self):
        test_data= CsvReader('Tests/Data/answers.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.mean(),float(row['Result Mean']) )

#    def test_population_standard_deviation(self):
#        self.assertEqual(self.statistics.stdev(), )

#    def test_variance_of_population_portion(self):
#        self.assertEqual(self.statistics.popvar(), )


if __name__ == '__main__':
    unittest.main()
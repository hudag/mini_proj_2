from Calculator.Calculator import Calculator
from Statistics.mean import mean
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.Data = CsvReader(filepath).data
        self.data = []
        for row in self.Data:
            self.data.append(row['Value 1'])
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result
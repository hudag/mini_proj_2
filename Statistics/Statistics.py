from Calculator.Calculator import Calculator
from Statistics.mean import mean
from Statistics.popvar import popvar
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

    def popvar(self):
        self.result = popvar(self.data)
        return self.result

    def stdev(self):
        self.result = stdev(self.data)
        return self.result
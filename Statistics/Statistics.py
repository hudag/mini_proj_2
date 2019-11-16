from Calculator.Calculator import Calculator
from Statistics.mean import mean
from Statistics.popvar import popvar
from Statistics.stdev import stdev
from Statistics.median import median
from Statistics.stscore import stscore
from Statistics.samplemean import samplemean
from Statistics.samplestdev import samplestdev
from Statistics.zscore import zscore
from Statistics.proportion import proportion
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.Data = CsvReader(filepath).data
        self.data = []
        for row in self.Data:
            self.data.append(float(row['Value 1']))
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

    def median(self):
        self.result = median(self.data)
        return self.result

    def stscore(self):
        self.result = stscore(self.data)
        return self.result

    def samplemean(self, sample_size):
        self.result = samplemean(self.data,sample_size)
        return self.result

    def samplestdev(self):
        self.result = samplestdev(self.data)
        return self.result

    def zscore(self):
        self.result = zscore(self.data)
        return self.result

    def proportion(self,size,corr):
        self.result = proportion(size,corr)
        return self.result
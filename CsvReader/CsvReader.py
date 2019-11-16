import csv
from pprint import pprint
from Fileutilities.absolutepath import absolutepath

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolutepath(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
        except FileNotFoundError:
            print("Invalid file path")
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
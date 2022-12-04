import csv
import numpy as np

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines
    def save_sum(self, column):
        l = np.array(self.read())
        extracted_data = l[:, 2]
        num_data = [int(d) for d in extracted_data]



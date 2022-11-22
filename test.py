import unittest
from CSVPrinter import CSVPrinter

class Test_CSVPrinter(unittest.TestCase):
    def test_LoadCurrentRows(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3,len(l))

    def test_LoadCurrentValues(self):
        printer = CSVPrinter("sample.csv")
        current_values = [
            ["Value1A","Value1B","Value1C"],
            ["Value2A","Value2B","Value2C"],
            ["Value3A","Value3B","Value3C"]
            ]
        l = printer.read()
        self.assertEqual(current_values,l)

    def test_FileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("sampl.csv")
            l = printer.read()

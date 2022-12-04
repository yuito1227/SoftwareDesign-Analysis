import unittest
from CSVPrinter import CSVPrinter

class Test_CSVPrinter(unittest.TestCase):
    def test_correct_ans(self):
        printer = CSVPrinter("only_num.csv")
        sum = printer.sum(2)
        self.assertEqual(18, sum)

    def test_not_number(self):
        with self.assertRaises(ValueError):
            printer = CSVPrinter("not_only_num.csv")
            sum = printer.sum(2)
    def test_invaild_column(self):
        with self.assertRaises(IndexError):
            printer = CSVPrinter("only_num.csv")
            sum = printer.sum(100)

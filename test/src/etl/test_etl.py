import unittest
import uuid
from os.path import exists
from src.etl.etl import calculate_percentile
import os


class EtlTest(unittest.TestCase):

    def setUp(self):
        self.date = '2022-03'
        filename = str(uuid.uuid4())
        self.output_file = f'{filename}.csv'
        self.column_name = 'trip_distance'

    def test_calculate_percentile(self):
        percent = 0.9
        self.assertFalse(exists(self.output_file))
        calculate_percentile(self.date, self.column_name, percent, self.output_file)
        self.assertTrue(exists(self.output_file))
        os.remove(self.output_file)

    def test_calculate_percentile_invalid_percent(self):
        percent = 13.0
        with self.assertRaises(ValueError) as context:
            calculate_percentile(self.date, self.column_name, percent, self.output_file)
            self.assertTrue(f'expected value greater than 1.0, but got {percent}' in context.exception)


if __name__ == '__main__':
    unittest.main()

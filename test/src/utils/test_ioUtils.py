import unittest
from src.utils.ioUtils import read_parquet


class IoUtilsTest(unittest.TestCase):

    def test_read_parquet_invalid_date_format(self):
        invalid_date = '2022-09-01'
        column_name = 'trip_distance'
        with self.assertRaises(Exception) as context:
            read_parquet(invalid_date, column_name)
            self.assertTrue('Error when trying to access URL file' in context.exception)


if __name__ == '__main__':
    unittest.main()

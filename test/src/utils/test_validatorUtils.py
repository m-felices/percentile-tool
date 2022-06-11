import unittest
from src.utils.validatorUtils import date_format_check, is_float, validate_parser, validate_between_range, \
    is_valid_csv_filename
from src.utils.parser import parse_args


class ValidatorTest(unittest.TestCase):


    def test_format_checkl(self):
        date = '2022-04'
        result = date_format_check(date)
        assert result

    def test_is_float(self):
        value = '9.0'
        result = is_float(value)
        assert result

    def test_validate_parser(self):
        date = '2022-09'
        percent = '0.1'
        output_file = 'results.csv'
        args = ['--d', date, '--p', percent, '--o', output_file]
        parser = parse_args(args)
        result = validate_parser(parser)
        assert result

    def test_validate_between_range(self):
        value = '1.8'
        min_value = '1.0'
        max_value = '16,9'
        result = validate_between_range(value, min_value, max_value)
        assert result

    def test_is_valid_filename(self):
        path = 'results.csv'
        result = is_valid_csv_filename(path)
        assert result


if __name__ == '__main__':
    unittest.main()

import unittest
from src.utils.parser import parse_args


class ParseTest(unittest.TestCase):

    def test_parser(self):
        date = '2022-02'
        percent = '0.1'
        output_filemane = 'results.csv'
        args = ['--d', date, '--p', percent, '--o', output_filemane]
        parser = parse_args(args)
        assert (parser.d == date)
        assert (parser.p == percent)
        assert (parser.o == output_filemane)


if __name__ == '__main__':
    unittest.main()

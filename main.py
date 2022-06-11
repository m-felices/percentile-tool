import sys
from src.utils.parser import parse_args
from src.utils.validatorUtils import validate_parser
from src.etl.etl import calculate_percentile

def main():
    try:
        parser = parse_args(sys.argv[1:])
        if validate_parser(parser):
            date = parser.d
            percent = float(parser.p)
            output_file = parser.o
            column_name = 'trip_distance'
            calculate_percentile(date, column_name, percent, output_file)
    except ValueError as err:
        print(f'Exception occurred: {err}')
    except Exception as err:
        print(f'Exception occurred: {err}')


if __name__ == '__main__':
    main()



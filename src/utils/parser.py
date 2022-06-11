import argparse


def parse_args(args):
    """
    Returns all the passed values from command line
    :param args: List of string to parse
    :return: An object with the argument strings
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--d', help='date with format "yyyy-mm"')
    parser.add_argument('--p', help='percentile')
    parser.add_argument('--o', help='output file')
    return parser.parse_args(args)


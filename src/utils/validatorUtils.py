import datetime


def date_format_check(value):
    """
    Check if the value has a valid date format "yyyy-mm"
    :param date: string containing the date
    :return: a value True if data has a valid date format. Otherwise, it returns False
    """
    try:
        datetime.datetime.strptime(value, '%Y-%m')
    except:
        return False
    else:
        return True


def is_float(value) -> bool:
    """
    Checks if the data is a float.
    :param value: string to check
    :return:a value True if data is a float. Otherwise, it returns False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_csv_filename(file):
    """
    Check if the file has a CSV extension
    :param file: string that contain the filename
    :return: a value True if the file has a CSV extension. Otherwise, it returns False
    """
    if file is not None:
        return file.lower().endswith('.csv')
    else:
        return False


def validate_parser(args):
    """
    Checks if argument strings contain a valid value
    :param args: argument strings
    :return: a value True if argument strings contain a valid value. Otherwise, it returns False
    """
    date = args.d
    if not date_format_check(date):
        raise ValueError('Invalid date')
    percent = args.p
    if not is_float(percent):
        raise ValueError('Invalid percent')
    output_file =args.o
    if not is_valid_csv_filename(output_file):
        raise ValueError('Invalid output file name')
    return True


def validate_between_range(value, min_value=0.0, max_value=1.0):
    """
    Determines whether the value is between a minimum ana maximum value
    :param value: number to compare
    :param min_value: a float containing the minimum value
    :param max_value: a float containing the maximum value
    :return: True if the value is between the minimum and maximum value
    """
    if value is None:
        return

    if min_value is not None and value < min_value:
        raise ValueError((
            f"expected value less than {min_value}, but got {value}"))

    if max_value is not None and value > max_value:
        raise ValueError((
            f"expected value greater than {max_value}, but got {value}"))
    return True

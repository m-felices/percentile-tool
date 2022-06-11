from src.utils.ioUtils import read_parquet, write_csv
from src.utils.validatorUtils import validate_between_range
import numpy as np


def calculate_percentile(date, column_name, percent, output_file):
    """
    Computes the percentile of list of values and stores it in a csv file
    :param date: A date with format 'yyyy-mm'
    :param column_name: column name that will be read from the source
    :param percent: float number
    :param output_file: file name in CSV format to store output data
    :return: None
    """
    try:
        if validate_between_range(percent, min_value=0.0, max_value=1.0):
            trip_distance_df = read_parquet(date, column_name)

            trip_distance_percentile = np.quantile(trip_distance_df, percent)
            trip_distance_over_percentile_df = trip_distance_df[trip_distance_df > trip_distance_percentile].dropna()
            print(f'{percent}th percentile of trip distance= {trip_distance_percentile}')
            write_csv(trip_distance_over_percentile_df, output_file)
            print(f'{output_file} file created successfully.')
    except ValueError as err:
        raise ValueError(err)
    except Exception as err:
        raise ValueError(err)

import pandas as pd
import urllib.request


def read_parquet(date, column):
    """
    Loads a parquet file over http(s)
    :param date: A date with format 'yyyy-mm'
    :param column: Column to read.
    :return: A dataframe
    """
    url = f'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_{date}.parquet'
    filename = f"temp_{date}.parquet"
    try:
        urllib.request.urlretrieve(url, filename)
        df = pd.read_parquet(filename, engine='pyarrow', columns=[column])
        if df.empty:
            raise Exception(f'Parquet file is empty: {url}')
        return df
    except Exception as err:
        raise Exception(f'Error when trying to access URL file: {err}')


def write_csv(dataframe, filename):
    """
    Write a dataframe to CSV file
    :param dataframe: Object containing dataset
    :param filename: string with the filename
    :return: None
    """
    if dataframe is None:
        return
    if filename is None:
        return
    dataframe.to_csv(filename, chunksize=10000, index=False)

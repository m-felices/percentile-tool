# Percentile Tool
 > A python utility to get the taxi rides in NYC dataset over a specified percentile.

## Table of contents
* [Description](#description)
* [About the project](#about-the-project)
* [Demo](#demo)
* [Required tools](#required-tools)
* [Getting Started](#getting-started)
  - [Setup](#setup)
  - [Executing program](#executing-program)
  - [Executing test](#executing-tests)
* [Roadmap](#roadmap)


## Description 
It calculates the k-th element for a dataset where k is 0 to 1 (inclusive) and returns all the trips over 
the specified percentile in distance traveled for a dataset. 
It is only compatible with "Yellow Taxi" Parquet files: [NYC “Yellow Taxi” Trips Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
since it includes column trip_distance, which indicates the elapsed trip distance in miles. 

## About the project 
The goal is to compute the k-th element of the percentile and return the values over that percentile. 

How does it work? 

1. Open a URL (see examples above) for the specified date (yyyy-mm format) and download a local file with Parquet extension. 
2. Load the Parquet file previously saved. The advantages of using Parquet:
   - 1: The file is read quickly since parquet format is optimized in the following ways: 
     * It loads n columns instead of the total columns of the file m results in n/m raw I/O volume.
     * The similarity of values within separate columns result in more efficient compression.
   - 2: Parquet files are self-describing so the schema is preserved and support schema evolution. 
3. Compute the value of the k-th element for the specified percentile. Data greater than that kth element is filter out. 
5. Finally, the result is stored as a CSV file. 

## Demo
The following example illustrates an example of how to run it: 

```
$ python main.py  --d "2022-01" --p 0.9 --o results.csv
0.9th percentile of trip distance= 7.17
results.csv file created successfully.
```
The output file can be found in the working directory.

Required arguments: 
```
* -d --date - A string with the date format "YYYY-mm".

* -p --percentile - A float number from 0 to 1, inclusive.

* -o --outputfile  - A filename in CSV format where the results will be saved.
```
 
## Required tools
* Python 3.9
* numpy v1.22.4
* pandas v1.4.2
* pyarrow v8.0.0


## Getting Started

### Setup
On Linux, install it locally using the following steps: 

1. Clone the repository:

```$ git clone https://github.com/m-felices/percentile-tool.git```

2. Access the project folder:

```cd percentile-tool ```

3. Install the ```python3-venv``` package that provides the ``venv``` module:

```$ sudo apt install python3-venv```

4. Switch to the directory where you would like to store your Python 3 virtual environments. 
Within the directory run the following command to create your new virtual environment:

```$ python3 -m venv my-project-env```

5. Enable the virtual environment:

```$ source venv/bin/activate```

6. Install the python dependencies on the virtual environment:

```$ pip install -r requirements.txt```


### Executing program 
From the project's directory:

```$ python main.py  --d "2021-01" --p 0.9 --o results.csv```


### Executing tests
From the project's directory run tests locally:

```$ python -m unittest```

## Roadmap

1. In case of dealing with large-scale data (e.g., more than 3 GB), instead of storing the files locally,
I would use a database to leverage the flexibility and optimization that SQL provides.
2. Table partitioning is a common optimization approach when using Parquet files. In a partitioned table, data are 
usually stored in different directories, with partitioning column values encoded in the path of each partition 
directory. A future enhancement could be, for example, storing all our previously used dataset into a partitioned 
table using the following directory structure with two columns: ```RateCodeID``` (final rate code in effect at 
the end of the trip) and ```Payment_type``` as partitioning columns.
This would improve I/O performance when loading part of dataset corresponding to a partition key.

```
path
└── to
    └── table
        ├── RateCodeID="Standard rate"
        │   ├── ...
        │   │
        │   ├── Payment_type="Credit Card"
        │   │   └── data.parquet
        │   ├── Payment_type="Cash"
        │   │   └── data.parquet
        │   └── ...
```



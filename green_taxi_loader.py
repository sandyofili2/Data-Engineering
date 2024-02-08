import io
import pandas as pd
import requests
import glob
import os
import numpy as np
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
   
    url1 = '/home/src/green_tripdata_2020-10.csv.gz'
    url2 = '/home/src/green_tripdata_2020-11.csv.gz'
    url3 = '/home/src/green_tripdata_2020-12.csv.gz'
    
    green_taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float 

    }
    taxi_parse=['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    df1 = pd.read_csv(url1, sep =',', compression="gzip", dtype= green_taxi_dtypes, parse_dates=taxi_parse)
    df2 = pd.read_csv(url2, sep =',', compression="gzip", dtype= green_taxi_dtypes, parse_dates=taxi_parse)
    df3 = pd.read_csv(url3, sep =',', compression="gzip", dtype= green_taxi_dtypes, parse_dates=taxi_parse)
    df = pd.concat([df1,df2,df3])
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

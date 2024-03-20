                            #Exporting data from csv
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

                                    #Transforming the Data

import inflection
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # Specify your transformation logic here

    data = data[data['passenger_count'] >0]
    data = data[data['trip_distance'] >0]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = data.columns.str.replace(" ", "_", regex=True).str.lower()
    #print(data['vendorid'].unique())
    assert (data['passenger_count']>0).any()
    assert (data['trip_distance']>0).any()
    return data
    
   
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

#Exporting the data to postgress

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """
    schema_name = 'mage'  # Specify the name of the schema to export data to
    table_name = 'green_taxi'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

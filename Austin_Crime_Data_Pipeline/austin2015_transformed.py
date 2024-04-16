import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = data.columns.str.replace(" ", "_", regex=True).str.lower()
    data = data.drop('unnamed:_0',axis=1)
    data = data.rename(columns={'highest_nibrs/ucr_offense_description': 'highest_offense_description'})
    

    return data

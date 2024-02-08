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

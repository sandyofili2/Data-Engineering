with 

source as (

    select * from {{ source('staging', 'Green-taxi-data') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['vendorid', 'lpep_pickup_datetime']) }} as tripid,
        vendorid,
        lpep_pickup_datetime,
        lpep_dropoff_datetime,
        store_and_fwd_flag,
        ratecodeid,
        pulocationid,
        dolocationid,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount,
        payment_type,
        {{get_payment_type_description('payment_type')}} as payment_type_description,
        trip_type,
        congestion_surcharge,
        lpep_pickup_date,
        __index_level_0__

    from source

)

select * from renamed

with 

source as (

    select * from {{ source('staging', 'yellow_cab_data') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['vendorid', 'lpep_pickup_datetime']) }} as tripid,
        vendorid,
        tpep_pickup_datetime,
        tpep_dropoff_datetime,
        passenger_count,
        trip_distance,
        ratecodeid,
        store_and_fwd_flag,
        pulocationid,
        dolocationid,
        payment_type,
        {{get_payment_type_description('payment_type')}} as payment_type_description,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        congestion_surcharge

    from source

)

select * from renamed

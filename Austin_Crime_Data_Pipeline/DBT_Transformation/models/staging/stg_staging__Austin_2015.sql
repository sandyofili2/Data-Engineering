with 

source as (

    select * from {{ source('staging', 'Austin_2015') }}

),

renamed as (

    select
        go_primary_key,
        council_district,{{property_location(council_district)}} as district_direction,
        go_highest_offense_desc,
        highest_offense_description,
        go_report_date,
        go_location,
        clearance_status,
        clearance_date,
        go_district,
        go_location_zip,
        go_census_tract,
        go_x_coordinate,
        go_y_coordinate

    from source

)

select * from renamed

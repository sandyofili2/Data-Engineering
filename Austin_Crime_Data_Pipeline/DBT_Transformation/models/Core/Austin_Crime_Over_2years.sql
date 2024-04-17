{{
    config(
        materialized='table'
    )
}}
with Austins2015 as (
    select *,
    '2015' as year
    From {{ref('stg_staging__Austin_2015')}}
),
 Austins2016 as (
    select *,
    '2016' as year
    From {{ref('stg_staging__Austin_2016')}}
),
AustinsCrimeData as (
    Select * from Austins2015
    union all
    Select * from Austins2016
)

Select * from AustinsCrimeData

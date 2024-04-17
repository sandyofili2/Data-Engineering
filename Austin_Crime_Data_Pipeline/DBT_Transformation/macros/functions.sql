{#
    This macro returns the description of the district the property is located in
#}
{#
Including the description of property location, so that we can use that information later to find the zone with the highest amount of crime
#}

{% macro property_location(council_district) -%}

    case {{ dbt.safe_cast("council_district", api.Column.translate_type("integer")) }}  
        when 1 then 'Northeast Austin'
        when 2 then 'Southeast Austin'
        when 3 then 'Central-East and East Austin'
        when 4 then 'North and Central Austin'
        when 5 then 'South Austin and part of Central Austin'
        when 6 then 'Northwest Austin'
        when 7 then 'Northwest and North Austin'
        when 8 then 'Southwest Austin'
        when 9 then 'Central Austin'
        when 10 then 'West Austin'
        else 'EMPTY'
    end

{%- endmacro %}

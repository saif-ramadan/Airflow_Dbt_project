with sales_teams as(
    select * from {{ref('stg_sales_teams')}}
)
select 
    row_number() over() as team_id,
    sales_agent,
    manager,
    regional_office,
from sales_teams
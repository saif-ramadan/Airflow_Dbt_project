with pipeline as (
    select * from {{ ref('stg_sales_pipeline') }}
),

accounts as (
    select * from {{ ref('dim_accounts') }}
),

products as (
    select * from {{ ref('dim_products') }}
),

teams as (
    select * from {{ ref('dim_sales_teams') }}
)

select
    p.opportunity_id,
    p.deal_stage,
    p.engage_date,
    p.close_date,
    p.close_value,
    
    -- Foreign Keys
    a.account_id,
    pro.product_id,
    t.team_id

from pipeline p
left join accounts a 
    on p.account_id = a.account_id
left join products pro 
    on p.product_name = pro.product_name
left join teams t 
    on p.sales_agent = t.sales_agent
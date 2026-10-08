with source as (
    select * from {{ source('raw_crm', 'raw_sales_pipeline') }}
),

renamed as (
    select
        opportunity_id,
        sales_agent,
        product as product_name,
        account as account_id,
        deal_stage,
        engage_date,
        close_date,
        close_value
    from source
)

select * from renamed
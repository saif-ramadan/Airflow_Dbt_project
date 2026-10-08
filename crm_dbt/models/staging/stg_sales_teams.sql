with source as (
    select * from {{ source('raw_crm', 'raw_sales_teams') }}
),

renamed as (
    select
        sales_agent,
        manager,
        regional_office,
    from source
)

select * from renamed
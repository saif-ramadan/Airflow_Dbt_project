with source as (
    select * from {{ source('raw_crm', 'raw_products') }}
),

renamed as (
    select
        series,
        product as product_name,
        sales_price
    from source
)

select * from renamed
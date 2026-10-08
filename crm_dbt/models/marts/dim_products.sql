with products as (
    select * from {{ ref('stg_products') }}
)

select
    row_number() over () as product_id,
    product_name,
    series,
    sales_price
from products
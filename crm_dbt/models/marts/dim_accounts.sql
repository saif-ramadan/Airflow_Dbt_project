with accounts as (
    select * from {{ ref('stg_accounts') }}
)

select
    account_id,
    sector,
    year_established,
    revenue,
    employees,
    office_location,
    subsidiary_of
from accounts
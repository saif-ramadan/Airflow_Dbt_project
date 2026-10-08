with source as (
    select * from {{ source('raw_crm', 'raw_accounts') }}
),

renamed as (
    select
        account as account_id,
        sector,
        year_established,
        revenue,
        employees,
        office_location,
        subsidiary_of
    from source
)

select * from renamed
-- models/transformed_data.sql
with raw_data as (
    select
        message_id,
        file_path,
        channel,
        date
    from {{ ref('raw_data') }}
)

select
    message_id,
    file_path,
    channel,
    date::timestamp as transformed_date -- Ensure the date is in timestamp format
from raw_data
where date is not null -- Exclude null dates

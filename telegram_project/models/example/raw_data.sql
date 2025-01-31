-- models/raw_data.sql
select
    message_id,
    file_path,
    channel,
    date
from public.cleaned_data

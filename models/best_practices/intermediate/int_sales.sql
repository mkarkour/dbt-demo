select *
from {{ source('raw_data', 'sales') }}
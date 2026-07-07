# Write your MySQL query statement below
SELECT id, count(*) as num
from(
    select requester_id as id
    from RequestAccepted
    union all
    select Accepter_id as id
    from RequestAccepted

) as t
group by id
order by num desc
limit 1;
-- -- # Write your MySQL query statement below
select 
CASE
    when id=(select IF((max(id))%2 =1,max(id),0) from seat) then id
    when id%2=0 then id-1
    when id%2=1 then id+1
    else id
END as id,
student
from seat order by id
-- -- select max(id) from seat

#select IF((max(id))%2 =1,max(id),0) from seat
# Write your MySQL query statement below
select e.name from employee as e join employee as m on e.id=m.managerId group by e.id, e.name having 
Count(m.id)>=5

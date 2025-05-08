# Write your MySQL query statement below
-- select employee_id from employees where employee_id>(select max(employee_id) from employees where employee_id<30000  ) ORDER BY employee_id
-- LIMIT 1;
SELECT employee_id
FROM Employees
WHERE salary < 30000
AND manager_id NOT IN (
  SELECT employee_id FROM Employees
)
ORDER BY employee_id;
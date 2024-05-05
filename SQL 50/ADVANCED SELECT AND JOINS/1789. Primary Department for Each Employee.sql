(SELECT employee_id, department_id FROM Employee
GROUP BY employee_id HAVING COUNT(department_id) = 1)
UNION 
(SELECT employee_id, department_id FROM Employee
WHERE primary_flag = 'Y');

-- Here we combine the results of 2 queries using the union function.
-- The first part is when there is no primary department when the employee joins for the first time. This is when the no of departments the employee works in will be 1.
-- Second part is when the employee works in multiple departments and we are selecting only the department where the primary_flag = "Y"

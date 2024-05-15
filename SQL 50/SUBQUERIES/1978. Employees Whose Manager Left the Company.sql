SELECT employee_id FROM Employees WHERE salary < 30000 AND manager_id NOT IN 
(
    SELECT employee_id FROM Employees
)
ORDER BY employee_id

-- Here we are first taking the employee_id with a salary less than 30000 and then checking if the manager_id is still present in the employee_id
-- Returning all the employee_id with manager_id not present in the subquery.

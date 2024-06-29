SELECT 
E1.employee_id,
E1.name AS employee_name
FROM employee AS E
LEFT JOIN 
employee AS E1
ON E.employee_id = E1.manager_id
WHERE E1.salary > E.salary

/*
- Here we first need to join the table so that we can compare the employee as well as the manager's salary
- Here E1.salary is the employee's salary and E.salary is the manager's salary. 
- We are using a LEFT JOIN on the same table to compare the salaries of the employee and the manager.
*/

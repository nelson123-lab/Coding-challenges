-- Using Common table expression

WITH managers AS(
    SELECT reports_to AS employee_id,
            COUNT(reports_to) AS reports_count,
            ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)

SELECT employee_id,
        name,
        reports_count,
        average_age
FROM managers AS m
INNER JOIN Employees AS e
USING(employee_id)
ORDER BY employee_id;

-- Using JOIN Operations.

SELECT mang.employee_id, mang.name, COUNT(emp.employee_id) as reports_count, ROUND(AVG(emp.age)) as average_age FROM Employees emp JOIN Employees mang
ON emp.reports_to = mang.employee_id
GROUP BY employee_id
ORDER by employee_id

-- Here we are using a self-join to make the number of employees who report to the manager.

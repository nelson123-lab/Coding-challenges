WITH highest_salary_cte AS (
  SELECT MAX(salary) AS highest_salary
  FROM employee
)

SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary < (
    SELECT highest_salary
    FROM employee
);

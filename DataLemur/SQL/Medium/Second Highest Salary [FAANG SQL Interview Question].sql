/* SOlution using subquery*/
SELECT MAX(salary) as second_highest_salary
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee)

-- Here we are first finding the max salary and then finding the max salary below the highest salary.
-- This solution is good for this question but if we want to find the third-highest salary we need to do a different approach. The generalization capability of this solution is very poor.

/* Solution using CTE */

WITH ranked_salaries AS (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM employee
)
SELECT salary AS second_highest_salary
FROM ranked_salaries
WHERE rn = 2;

-- First, we are storing the rank of all the salaries in a CTE using the ROW_NUMBER() OVER (ORDER BY salary DESC)
-- Then with a simple query with the required rank as the row number we can find whichever rank we prefer.

-- Write your MySQL query statement below
WITH running_weights AS (
    SELECT *, SUM(weight) 
    OVER(ORDER BY turn) as running_wt 
    FROM Queue 
    ORDER BY turn
)

-- First ordering the information by turn in which people enter the bus. 
-- Running sum of the weights of the individuals is found and stored as a new column.

SELECT person_name
FROM running_weights
WHERE running_wt <= 1000
ORDER BY running_wt DESC
LIMIT 1

-- Ordering by the running_wt in descending order and checking for person_name with less than 1000 in running_wit which will be the last person to enter the bus.
-- LIMIT 1 returns just 1 row.

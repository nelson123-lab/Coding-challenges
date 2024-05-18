-- Write your MySQL query statement below
-- Using the CASE Function to create a table where it keeps track of the number of accounts in different ranges.
WITH Acc_category AS (
    SELECT 
        CASE 
            WHEN income < 20000 THEN "Low Salary"
            WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
            ELSE "High Salary"
        END AS category 
    FROM Accounts
),

-- Here we are creating a table with the actual values present in this since there won't be every type of account from the actual data.
All_categories AS (
    SELECT "Low Salary" AS category
    UNION
    SELECT "Average Salary"
    UNION
    SELECT "High Salary"
)

-- Here we are doing a LEFT JOIN to join the all_category and actual_category information to get the count of all the accounts information.
SELECT all_c.category, COUNT(act_c.category) AS accounts_count
FROM All_categories AS all_c
LEFT JOIN Acc_category AS act_c
ON all_c.category = act_c.category
GROUP BY category

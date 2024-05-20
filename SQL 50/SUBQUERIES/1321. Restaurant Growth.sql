-- Initial Approach
/* Here we need to GROUOP BY the visited_on because in the same day there are multiple people purchasing items so we need to combine 
the total amount per day inorder move forward.
*/
WITH PerdayTotal AS (
    SELECT visited_on, SUM(amount) as amount FROM Customer
GROUP BY visited_on
),

/* Now I am creating a row number to keep track of the row_number since we don't have any other column to keep track of the window count.
  This is taken as a separate column because when the visited column is used for ordering and adding the row number we cannot do GROUP BY using the same column
  in the same query.
*/
NumberedCustomer AS (
    SELECT visited_on, amount, ROW_NUMBER() OVER (ORDER BY visited_on) AS row_num
    FROM PerdayTotal
),

/* Here we are using the OVER () method in CASE() to create a sliding window.
*/
Final_Table AS (
SELECT row_num, visited_on, 
  /* Creating a sliding window for the moving average.
  */
       CASE
           WHEN row_num >= 7 THEN AVG(amount) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           )
           ELSE NULL
       END AS moving_average, 
  /* Creating a sliding window for the moving sum.
  */
       CASE
           WHEN row_num >= 7 THEN SUM(amount) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           )
           ELSE NULL
       END AS moving_sum
FROM NumberedCustomer)

SELECT visited_on, ROUND(moving_sum, 2) AS amount, ROUND(moving_average, 2) AS average_amount FROM Final_Table
WHERE row_num > 6

/* 
#########
  -- More Optimized Solution
#########
*/
-- Created a table that creates row number and GROUP BY the visited_on to generate the sum of amounts for each day.
WITH PerdayTotal AS (
    SELECT visited_on, SUM(amount) as amount, ROW_NUMBER() OVER () AS row_num FROM Customer
GROUP BY visited_on
),

Final_Table AS (
SELECT row_num, visited_on, 
       ROUND(CASE
           WHEN row_num >= 7 THEN AVG(amount) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           )
           ELSE NULL
       END, 2) AS average_amount, 

       ROUND(CASE
           WHEN row_num >= 7 THEN SUM(amount) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           )
           ELSE NULL
       END, 2) AS amount
FROM PerdayTotal)

SELECT visited_on, amount, average_amount FROM Final_Table
WHERE row_num > 6

-- This solution can be optimized more by adding LAG() method along with RANGE() BETWEEN instead of ROW () BETWEEN

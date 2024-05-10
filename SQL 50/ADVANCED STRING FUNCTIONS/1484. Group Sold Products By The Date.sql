-- Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products FROM Activities
GROUP BY sell_date

-- Here we are using GROUP_CONCAT to combine the products into the row for the same date.

-- Write your MySQL query statement below
-- Here we cannot make the table using the max price because there are cases when the price of a product becomes less in the future days. eg: initially 30, 35, and then 5. So we have to take 5 as the price.
WITH pre_date AS (
    SELECT product_id, MAX(change_date) AS date 
    FROM Products 
    WHERE change_date <= "2019-08-16"
    GROUP BY product_id)
  
-- Query to get the latest price values before the date "2019-08-16"
SELECT P.product_id, new_price as price 
FROM Products AS P JOIN pre_date AS PRE
ON P.product_id = PRE.product_id AND P.change_date = PRE.date
UNION

-- Query to get the price of products that are not present before "2019-08-16"
SELECT DISTINCT product_id, 10 AS price 
FROM Products WHERE product_Id NOT IN (
    SELECT product_id FROM pre_date)
GROUP BY product_id

-- Here we are using the UNION function to combine the results of both the queries.



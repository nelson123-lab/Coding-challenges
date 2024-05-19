-- Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit FROM Orders AS O
LEFT JOIN Products AS P
ON P.product_id = O.product_id
WHERE O.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY O.product_id HAVING unit >= 100

-- Here we use a LEFT JOIN to combine the Products and the order table. 
-- Extract the order date in February.
-- Grouping by product_id and having the unit total price greater than 100.

-- Write your MySQL query statement below
SELECT P.product_id, IFNULL(ROUND(SUM(U.units * P.price)/SUM(U.units),2),0) AS average_price FROM Prices as P LEFT JOIN UnitsSold as U ON P.product_id = U.product_id
AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id

"""
- Here we are joining the tables on the product_id and purchase date betweeen start date and enddatae.
"""

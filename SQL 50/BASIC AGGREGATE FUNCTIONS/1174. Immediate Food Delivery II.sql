-- Write your MySQL query statement below
-- SELECT *, MIN(order_date), (CASE WHEN order_date = customer_pref_delivery_date THEN "immediate" ELSE "scheduled" END) as status FROM Delivery 
-- GROUP BY customer_id
-- ORDER BY customer_id

SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100, 2) as immediate_percentage FROM Delivery as D 
WHERE D.order_date = ( 
    SELECT MIN(D2.order_date) FROM Delivery as D2 WHERE D2.customer_id = D.customer_id
)

"""
- Here we are using a case condition to determine the immediate percentage of the first order of the customers.
"""

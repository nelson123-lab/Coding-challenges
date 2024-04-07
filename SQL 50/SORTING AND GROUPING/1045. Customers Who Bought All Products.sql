-- Write your MySQL query statement below
SELECT  customer_id FROM Customer 
GROUP BY customer_id HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)

"""
- Hre we need find the customers that have all types of products.
- Here we are finding the customer_id which have all products by the distinct count of the products.
"""

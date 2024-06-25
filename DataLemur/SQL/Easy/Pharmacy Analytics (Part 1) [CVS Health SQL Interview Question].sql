SELECT drug, (total_sales - cogs) AS total_profit 
FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3

/*
- Here we finding the total profit by finding the difference between the total sales - cogs(cost of good sold).
*/

SELECT 
manufacturer, 
CONCAT('$', ROUND(SUM(total_sales) / 1000000), ' million')  AS 	sales_mil 
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC, manufacturer

/*
- Here we are finding the sum of the total sales only difficulty here is adding the dollar symbol and the million using the concatenating as sales_mil.
- Ordering the sales based on the total sales and then using the manufacturer.
*/

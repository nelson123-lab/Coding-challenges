SELECT manufacturer, COUNT(drug) AS drug_count, SUM(cogs - total_sales) AS total_loss 
FROM pharmacy_sales
WHERE cogs > total_sales
GROUP BY manufacturer
ORDER BY total_loss DESC

/*
- Here we need to filter out the drugs that had a loss in sales. For this, we need to check if the cogs(cost of the goods) are greater than the total sales.
- Then we need to find the sum of the total loss and the count of the drug. We use aggregate functions within the group by sum and count respectively.
*/

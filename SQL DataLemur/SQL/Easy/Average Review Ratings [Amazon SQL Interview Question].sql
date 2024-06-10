SELECT 
    EXTRACT(MONTH FROM submit_date) AS mth,
    product_id, 
    ROUND(AVG(stars), 2) AS avg_stars
FROM 
    reviews
GROUP BY 
    mth, 
    product_id
ORDER BY 
    mth, product_id;

-- Explanation
/*
- Here we are first extracting the month and then grouping by month and product_Id to get the products grouped per month.
- Finding the average star ratings per month using the aggregate AVG() function of GROUP BY ()
*/

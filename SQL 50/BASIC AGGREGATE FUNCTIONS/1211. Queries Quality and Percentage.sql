SELECT query_name, 
ROUND(SUM(rating/position)/COUNT(rating), 2) as quality,  
ROUND(
    (
        (
            SELECT COUNT(rating) as rating_count 
            FROM Queries q2 
            WHERE q2.query_name = Q1.query_name AND rating < 3
        ) 
        / COUNT(*)
    ) * 100, 2
)
 as poor_query_percentage
FROM Queries as Q1
WHERE query_name IS NOT NULL
GROUP BY query_name


SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance 

-- Here we need to have the same tiv_2015 value as one or more other policyholders
-- Here we are extracting this by checking in a subquery where the tiv_2015 is more than 1.
WHERE tiv_2015 IN (
    SELECT tiv_2015 
    FROM Insurance
    GROUP BY tiv_2015 
    HAVING COUNT(tiv_2015) > 1
) 
-- Here we need to have the (lat, long) not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique
-- Here we are checking it using a subquery where all the unique lat, lon are present.
AND (lat, lon) IN (
    SELECT lat, lon 
    FROM Insurance
    GROUP BY lat, lon 
    HAVING COUNT(*) = 1
)
/*
- Here we have two conditions to meet which are connected by the AND condition.
*/

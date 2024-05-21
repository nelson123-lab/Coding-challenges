-- Write your MySQL query statement below
SELECT name, COALESCE(SUM(distance), 0) AS travelled_distance
FROM Users AS U
LEFT JOIN Rides AS R ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, U.name;

/*
Here we use LEFT JOIN to combine the Users and rides tables. Users table is in the LEFT because it has all the information about the user's name and the id.
Using COALESCE() to keep null values as 0.
*/

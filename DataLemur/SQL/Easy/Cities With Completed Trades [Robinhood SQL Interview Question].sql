SELECT city, COUNT(*)  FROM trades AS T LEFT JOIN users AS U 
ON T.user_id = U.user_id
WHERE T.status = 'Completed'
GROUP BY city
ORDER BY count DESC
LIMIT 3

/*
- Here we need to first do a left join to get the city in which trade is happening for each of the users.
- We are filtering out the completed orders 
- A group by city is required to find the count of the trades
/*

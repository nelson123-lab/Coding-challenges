WITH Friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, COUNT(id) AS num 
FROM Friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;

/*
-- Here person with the most number of friends can be found by combining the requester_id and accepter_id and then GROUP BY id.
-- RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+

In the above example when we combine the table it gets converted to the below format.

| id |
| -- |
| 1  |
| 1  |
| 2  |
| 3  |
| 2  |
| 3  |
| 3  |
| 4  |

-- Here we can find that the 3 is repeated 3 times which means 3 has 3 friends 1 (1-3 connection), 2 (2-3 connection), 4 (3-4 connection) and similarly for other
-- Now we GROUP BY id to find the solution.
*/

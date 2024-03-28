-- Write your MySQL 
SELECT ROUND(COUNT(DISTINCT A1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity A1
WHERE (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)

"""
- Here we are using DATE_SUB to find login of the player with a interval of 1 day.
"""

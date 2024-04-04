-- Write your MySQL query statement below
SELECT activity_date as day, COUNT(DISTINCT user_id) AS active_users 
FROM Activity 
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND DATE('2019-07-27')
GROUP BY activity_date;

"""
Here we need check for the date between the '2019-07-27' and 30 days before it that's why we are using the date_sub method.
"""

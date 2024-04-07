-- Write your MySQL query statement below
SELECT user_id, COUNT(follower_id) as followers_count 
FROM Followers
GROUP BY user_id
ORDER BY user_id

"""
Here we need the followers count which can be only found using the GROUPING BY user_id
"""

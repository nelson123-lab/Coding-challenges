-- Using Subquery method

SELECT tweet_bucket, COUNT(user_id) AS users_num
FROM 
  (
  SELECT user_id, 
  COUNT(tweet_id) AS tweet_bucket 
  FROM tweets 
  WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31' 
  GROUP BY user_id
  )
AS total_tweets
GROUP BY tweet_bucket

-- Using CTE (common table expression)

WITH total_tweets AS
  (
  SELECT user_id, 
  COUNT(tweet_id) AS tweet_bucket 
  FROM tweets 
  WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31' 
  GROUP BY user_id
  )

SELECT tweet_bucket, COUNT(user_id) AS users_num FROM total_tweets
GROUP BY tweet_bucket

-- Here the table can be used anywhere in future. This is better than using a subquery method to solve the problem.

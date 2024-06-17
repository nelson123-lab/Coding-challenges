-- Creating a table using user_posts with all the user's first and last posts in the year 2021
-- Here we are also checking if the number of posts exceeds 2.
WITH user_posts AS (
    SELECT user_id, 
    -- Finding the first post for each user.
    MIN(post_date) AS first_post,
    -- Finding the last post for each user.
    MAX(post_date) AS last_post
    FROM posts
    WHERE user_id IN (
        SELECT user_id
        FROM posts
  -- Checking if the post date is from 2021
        WHERE DATE_PART('year', post_date) = 2021
        GROUP BY user_id
        HAVING COUNT(*) > 2
    )
    GROUP BY user_id
)

SELECT user_id, 
       EXTRACT(DAY FROM (last_post - first_post)) AS days_between
FROM user_posts
ORDER BY days_between DESC

-- Extracting the no of days from the first and the last post using the Extract method of the PostgreSQL.

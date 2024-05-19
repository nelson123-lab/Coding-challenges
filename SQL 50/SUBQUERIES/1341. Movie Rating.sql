-- Write your MySQL query statement below
-- Combining the MovieRating table with the Users table to get the person who reviewed the maximum number of Movies.
WITH Names AS (SELECT name, COUNT(MR.user_id) AS No_rat FROM MovieRating AS MR LEFT JOIN Users AS U
ON MR.user_id = U.user_id
GROUP BY MR.user_id
  -- lexicographically ordering the query results. Here first we need to order by ratings count and then by name.
ORDER BY No_rat DESC, name
LIMIT 1),

  -- Combining the MovieRating with the Movies table to get the movie that has the maximum rating.
Movies AS (SELECT title, AVG(rating) AS Avg_rating FROM MovieRating AS MR LEFT JOIN Movies AS M
ON MR.movie_id = M.movie_id
  -- Using a between method to extract all the movie reviews in February.
WHERE created_at BETWEEN "2020-02-01" AND "2020-02-29"
GROUP BY MR.movie_id
    -- lexicographically ordering the query results. Here first we need to order by Average_ratings and then by title.
ORDER BY Avg_rating DESC, title
LIMIT 1 )

-- Selecting the queries FROM Names and titles from Movies and combining the results using UNION ALL to display the results of the query together.
SELECT name AS results FROM Names
UNION ALL
SELECT title AS results FROM Movies

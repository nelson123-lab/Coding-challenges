# Write your MySQL query statement below
Select tweet_id from Tweets
where CHAR_LENGTH(content) > 15

/*
Here the CHAR_LENGTH(content) is used to find the length of the string in the content column.
/*

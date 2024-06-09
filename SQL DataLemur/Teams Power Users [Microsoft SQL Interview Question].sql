SELECT sender_id, COUNT(message_id) AS counts
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = '8' 
  AND EXTRACT(YEAR FROM sent_date) = '2022'
GROUP BY sender_id
ORDER BY counts DESC
LIMIT 2;

-- Explanation
-- Solution using COUNT to count the number of messages
-- Using a WHERE condition to check the month and year and grouping the sender_id and the count messages.
-- Using LIMIT 2 to display the first 2 sender_id based on the count of messages

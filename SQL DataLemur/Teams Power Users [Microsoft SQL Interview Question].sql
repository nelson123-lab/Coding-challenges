-- Solution using COUNT to count the number of messages
-- Using a WHERE condition to check the month and year and grouping my the sender_id and the count messages.
SELECT 
  sender_id,
  COUNT(message_id) AS count_messages
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = '8'
  AND EXTRACT(YEAR FROM sent_date) = '2022'
GROUP BY sender_id
ORDER BY count_messages DESC
LIMIT 2; 

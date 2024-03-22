SELECT R.contest_id, ROUND((COUNT(R.user_id) / (SELECT COUNT(*) FROM Users)) * 100, 2) AS percentage 
FROM Users AS U 
JOIN Register AS R ON R.user_id = U.user_id
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id ASC

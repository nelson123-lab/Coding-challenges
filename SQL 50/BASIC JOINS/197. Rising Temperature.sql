WITH temp_lag AS (
SELECT id, temperature, recordDate as currDate, 
LAG(temperature) OVER(ORDER BY recordDate ASC) AS lag_temp,
LAG(recordDate) OVER(ORDER BY recordDate ASC) AS lag_date
FROM Weather
)
SELECT id
FROM temp_lag
WHERE temperature > lag_temp AND DATEDIFF(currDate, lag_date) = 1

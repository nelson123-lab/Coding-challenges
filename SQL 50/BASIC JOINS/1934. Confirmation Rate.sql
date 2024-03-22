SELECT s.user_id , IfNull(Round (Avg(c.action='confirmed'),2), 0.00) as confirmation_rate FROM Signups S LEFT JOIN Confirmations C ON S.user_id = C.user_id
GROUP BY S.user_id 

-- COmbining the function to determine the average of the confirmed column.

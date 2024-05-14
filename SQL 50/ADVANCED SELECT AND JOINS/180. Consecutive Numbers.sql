SELECT DISTINCT a.num AS ConsecutiveNums FROM Logs a
JOIN Logs b ON a.id = b.id + 1
JOIN Logs c ON b.id = c.id + 1
WHERE a.num = b.num AND b.num = c.num

-- Here we are using the self join to combine the same table skipping one row and skipping two rows.
-- We are then selecting the distinct element to find the elements that exist consecutively using the WHERE clause.

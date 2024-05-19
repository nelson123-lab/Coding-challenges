SELECT 
CASE 
  -- Checking for even cases
    WHEN id % 2 = 0 THEN id - 1
  -- Checking for odd cases the last element.
    WHEN (id % 2 != 0 AND id = (SELECT max(id) FROM Seat)) THEN id
  -- Checking for odd cases
    WHEN id % 2 != 0 THEN id + 1
END AS id,
student
FROM Seat
ORDER BY id


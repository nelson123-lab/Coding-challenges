SELECT *,
CASE WHEN (x+y > z) AND (x+z > y) AND (y+z > x) THEN "Yes" ELSE "No" END AS triangle
FROM Triangle

-- Here we are using CASE method to check if the traingle can be created using the line segments.

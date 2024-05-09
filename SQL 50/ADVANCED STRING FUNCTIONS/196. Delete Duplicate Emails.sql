-- Write your MySQL query statement below
DELETE p1 FROM Person p1, Person p2
WHERE p1.email = p2.email and p1.id > p2.id

-- (p1.id > p2.id). This condition ensures that only rows with higher IDs (later entries) are deleted when multiple rows have the same email address.

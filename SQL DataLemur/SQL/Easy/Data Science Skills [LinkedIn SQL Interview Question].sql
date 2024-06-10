SELECT candidate_id FROM candidates
WHERE skill in ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id HAVING COUNT(skill) = 3

-- Used where condition to check if skill of the candidate exist in the required skillsets.
-- GROUP BY was used to identify the how many such candidates are there and checking the number of skils =3 in the HAVING condition.

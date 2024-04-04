-- Write your MySQL query statement below
SELECT  teacher_id, COUNT(DISTINCT subject_id) as cnt FROM Teacher
GROUP BY teacher_id

"""
Here we are finding the distinct subject_id from the teachers.
"""

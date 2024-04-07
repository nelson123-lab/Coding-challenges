-- Write your MySQL query statement below
SELECT class FROM Courses 
GROUP BY class HAVING COUNT(student) >= 5

"""
Here we need to find the classes with more than 5 students enrolled in it which is done with the help of using HAVING condition along with the GROUP BY.
"""

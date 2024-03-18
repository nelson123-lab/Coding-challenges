-- Write your MySQL query statement below
SELECT E.name, B.bonus FROM Employee as E LEFT JOIN Bonus as B
ON E.empId = B.empId WHERE B.bonus < 1000 OR B.bonus IS NULL

"""
- Here we are using Left join to keep all the values in the left table and the common employee_id from the right table. 
- We are two conditions on the top of the joined table for finding the bonus.
"""

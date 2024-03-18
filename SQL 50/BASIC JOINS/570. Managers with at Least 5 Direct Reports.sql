-- Approach 1 subquery
SELECT E.name FROM Employee E WhERE E.id IN (SELECT M.managerId FROM Employee M
GROUP BY M.managerId HAVING COUNT(M.managerId) >= 5)

-- Approach 2 using JOINS
SELECT E.name FROM Employee E JOIN Employee M ON E.id = M.managerId
GROUP BY M.managerId HAVING COUNT(M.managerId) >= 5

"""
- Here we are joining the same table on id = mangerid and applying a condition to check the count.
"""

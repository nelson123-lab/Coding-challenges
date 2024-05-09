-- Write your MySQL query statement below
SELECT (SELECT DISTINCT salary FROM Employee 
ORDER BY Salary DESC LIMIT 1 OFFSET 1 ) AS SecondHighestSalary

-- Here we are taking the distinct salary from the Employee and ordering them by Salary in descending order to get the highest to lowest and then select them again to handle the null case.

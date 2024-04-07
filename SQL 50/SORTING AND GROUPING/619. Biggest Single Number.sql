-- Write your MySQL query statement below
SELECT MAX(num) as num FROM MyNumbers WHERE num IN (SELECT num FROM MyNumbers
GROUP BY num HAVING COUNT(num) = 1)

"""
Here we need to find the max number from the MyNumbers. There are several cases where the max number of occurance is not existing when the occurance are same for different numbers.
We use WHERE num in a subquery to handle this case.
"""

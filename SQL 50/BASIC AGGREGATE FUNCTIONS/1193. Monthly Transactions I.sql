-- Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date , "%Y-%m") as month, 
country, 
COUNT(id) as trans_count, 
SUM(CASE WHEN lower(state) = "approved" THEN 1 ELSE 0 END) as approved_count,
SUM(amount) as trans_total_amount, 
SUM(CASE WHEN lower(state) = "approved" THEN amount ELSE 0 END) as approved_total_amount FROM Transactions
GROUP BY country, month

"""
- Here we are using the DATE_FORMAT() function to filter out the year and the month inorder to groupby by month.
- CASE method is used to get the approved count and the approved_total_amount.
- CASE SYNTAX :- CASE WHEN "CONDITION" THEN "ACTION" ELSE "ACTION" END
"""

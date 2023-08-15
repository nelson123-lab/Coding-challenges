# Write your MySQL query statement below
SELECT V.customer_id, COUNT(V.visit_id) AS count_no_trans
FROM Visits V
LEFT JOIN Transactions T
ON V.visit_id = T.visit_id
WHERE T.Transaction_id IS NULL
GROUP BY V.customer_id;


/* Here LEFT JOIN is used to get all the visitors. The Visitors with Transactions = NuLL are the visitors that haven't made any transaction after visting the mall.
We need to find the count of these specific people. */

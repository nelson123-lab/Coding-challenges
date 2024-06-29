WITH total_deals AS (
    SELECT employee_id, SUM(deal_size) AS total_deals 
    FROM deals
    GROUP BY employee_id
)

SELECT T.employee_id,
CASE WHEN S.quota < T.total_deals THEN 'yes' ELSE 'no' END AS made_quota
FROM sales_quotas AS S
LEFT JOIN total_deals AS T
ON T.employee_id = S.employee_id
ORDER BY S.employee_id

/*
- Here we first need to group by employee_id to get the total sum of the deal_size to get the total deal amount.
- Then write a case method to keep track of whether the total deals crossed the quota or not. 
*/

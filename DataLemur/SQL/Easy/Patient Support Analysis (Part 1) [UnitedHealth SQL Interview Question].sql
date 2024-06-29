WITH policy_calls_count AS (
    -- Selecting the count of policy_holder_id occurrences that appear 3 or more times
    SELECT COUNT(policy_holder_id) AS policy_holder_count
    FROM callers
    GROUP BY policy_holder_id
    HAVING COUNT(case_id) >= 3
)

-- Counting the number of policyholders that meet the criteria
SELECT COUNT(policy_holder_count) AS policy_holder_count
FROM policy_calls_count;

/*
- Here first we need to group by the policy_holder_id having case_id >= 3 in order to identify the set of policyholders that made more than 3 calls.
- Now we need to count the number of policy holders using a CTE table or subquery.
*/

-- Brute force solution
WITH sign_up AS (
    SELECT 
        user_id, 
        E.email_id, 
        signup_action, 
        EXTRACT(DAY FROM (action_date - signup_date)) AS difference 
    FROM 
        emails AS E 
    LEFT JOIN 
        texts AS T ON E.email_id = T.email_id
    ORDER BY 
        T.action_date
)

SELECT 
    user_id 
FROM 
    sign_up 
WHERE 
    difference = 1 
    AND signup_action = 'Confirmed';

-- Optimized Solution

  SELECT 
      user_id
  FROM 
      emails AS E 
  LEFT JOIN 
      texts AS T ON E.email_id = T.email_id
  WHERE
      action_date = signup_date + INTERVAL '1 day' 
      AND
      T.signup_action = 'Confirmed'

/*
Explanation
- Removed extra usage of the table.
- Removed the usage of the EXTRACT function and used the INTERVAL method to check if action_date = signup_date + 1
*/

-- Solution using CTE
WITH CTR_cte AS (
    SELECT 
        app_id,
        SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END) AS impressions,
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks
    FROM 
        events
    WHERE 
        EXTRACT(YEAR FROM timestamp) = 2022
    GROUP BY 
        app_id
)

SELECT 
    app_id, 
    CASE 
        WHEN impressions = 0 THEN 0
        ELSE ROUND((clicks::numeric / impressions::numeric) * 100.0, 2)
    END AS ctr
FROM 
    CTR_cte
ORDER BY 
    ctr DESC
  
-- Explanation
/*
- We only want the events in the year 2022 so we use the EXTRACT () method.
- To find the CTR first, we need to find the number of clicks as well as impressions from the evnet_type column. This is the reason why we are using the CASE () method.
- The main SELECT query uses a CASE condition to handle the zero division error when the impressions counts are 0. If not handled the query fails( here no test cases are present to test it.)
*/

-- Optimized Solution
SELECT 
    app_id, 
    ROUND(
        100.0 * 
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) / 
        SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END), 
        2
    ) AS ctr
FROM 
    events
WHERE 
    timestamp >= '2022-01-01' 
  AND timestamp < '2023-01-01'
GROUP BY 
    app_id
ORDER BY 
    ctr DESC;

-- Explanation
/*
- Here we removed the EXTRACT method and added a where condition to filter out the year date to improve the performance.
- Removed the extra table 
- Removed handling the impressions = 0, as impressions cannot be zero when a click is present.
*/

-- Solution using the Filter method
SELECT
  app_id,
  ROUND(100.0 *
    SUM(1) FILTER (WHERE event_type = 'click') /
    SUM(1) FILTER (WHERE event_type = 'impression'), 2) AS ctr_app
FROM events
WHERE timestamp >= '2022-01-01' 
  AND timestamp < '2023-01-01'
GROUP BY app_id;
-- Using the FILTER () method instead of CASE.

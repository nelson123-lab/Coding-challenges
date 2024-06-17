/*
Solution using Subquery
*/
SELECT page_id
FROM pages
WHERE page_id NOT IN (
  SELECT page_id
  FROM page_likes
  WHERE page_id IS NOT NULL
)
  
/*
- Here it uses a subquery to check if the page_id is present in present in a list or not.
*/

/*
Solution using JOIN
*/
SELECT 
    p.page_id 
FROM 
    pages AS p 
LEFT JOIN 
    page_likes AS pl
ON 
    p.page_id = pl.page_id 
WHERE 
    pl.liked_date IS NULL
ORDER BY 
    p.page_id

/*
- Here we need to know all the pages with No likes. So from the pages table, we need all the page information. 
- We are using a LEFT JOIN to combine the page table and the page_like table along with a where clause to find the like_date = NULL
*/

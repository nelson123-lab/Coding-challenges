SELECT 
    SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_reviews,
    SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_reviews
FROM 
    viewership;

/*
- Here we are first creating the number of reviews using the CASE statement. 
- The first CASE statement is used to extract the laptop reviews and the second CASE statement for extracting the mobile_reviews 
*/

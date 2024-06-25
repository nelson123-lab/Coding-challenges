SELECT ROUND(
  SUM(item_count::DECIMAL * order_occurrences)/SUM(order_occurrences), 
  1) AS mean 
FROM items_per_order

/*
We need to find the sum of the order occurrences and the total number of order occurrences for each item count in order to calculate the mean.
*/

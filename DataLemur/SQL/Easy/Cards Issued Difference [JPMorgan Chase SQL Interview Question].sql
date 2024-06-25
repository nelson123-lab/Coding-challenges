SELECT card_name, MAX(issued_amount) - MiN(issued_amount) AS difference 
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY difference DESC

/*
- Here we need to check the difference between the best price month vs the worst price month of each of the credit cards.
- Since there is no priority for the month in this question we can just group by the card_name and find the difference.
/*

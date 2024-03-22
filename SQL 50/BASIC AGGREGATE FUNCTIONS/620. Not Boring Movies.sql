SELECT id, movie, description, rating FROM Cinema WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC

"""
- Here we need to return the odd number of movies with description not equal to boring.
"""

def min_inequity(salaries, n):
    salaries = sorted(salaries)[:n]
    return max(salaries) - min(salaries)

"""
- Here we are first sorting the list in increasing order.
- Sorted() is used instead of sort() as we want a new list.

Time Complexity O(nlogn)
Space Complexity O(n)
"""

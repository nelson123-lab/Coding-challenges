def fizzbuzz(n):
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

"""
Time Complexity O(n)
- Here one iteration is happening. This varies accoring to the input.
Space COmplexity O(1)
- There is no extra space used here. The results are only being printed.
"""

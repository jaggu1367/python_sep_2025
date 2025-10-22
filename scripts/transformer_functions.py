# MAGIC %md
# ## map(), filter(), reduce(), and sorted() in Python
# This notebook explains four powerful built-in functions in Python: `map()`, `filter()`, `reduce()`, and `sorted()`. Each section includes theory and examples using named functions (not `lambda`).

# MAGIC %md
# ### 1. `map(function, iterable)`
# **What it does**: Applies a function to each item in an iterable and returns a new iterable (a `map` object).  
# **Use case**: When you want to transform or modify each element.

# DBTITLE 1, Example: Squaring numbers with `map()`
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# MAGIC %md
# ### 2. `filter(function, iterable)`
# **What it does**: Filters items in an iterable using a function that returns `True` or `False`.  
# **Use case**: When you want to keep only items that meet a condition.

# DBTITLE 1, Example: Filtering even numbers with `filter()`
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

# MAGIC %md
# ### 3. `reduce(function, iterable)`
# **What it does**: Applies a rolling computation to sequential pairs of items.  
# **Use case**: When you want to reduce a list to a single value (like a sum or product).  
# `reduce()` comes from the `functools` module.

# DBTITLE 1, Example: Multiplying all elements with `reduce()`
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)

print(product)  # Output: 24

# MAGIC %md
# ### 4. `sorted(iterable, key=..., reverse=...)`
# **What it does**: Returns a new sorted list from the items in an iterable.  
# **Use case**: Sort using default or custom key (e.g., sort by string length).

# DBTITLE 1, Example: Sorting words by length with `sorted()`
def get_length(word):
    return len(word)

words = ['apple', 'banana', 'kiwi', 'cherry']
sorted_words = sorted(words, key=get_length)

print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'cherry']

# MAGIC %md
# ### Summary
# | Function | Purpose                     | Returns      | Function Type       |
# |----------|-----------------------------|--------------|----------------------|
# | `map()`  | Transform each element       | map object   | Any transformation   |
# | `filter()`| Select items by condition   | filter object| Boolean-returning    |
# | `reduce()`| Combine items into one       | Single value | Binary function      |
# | `sorted()`| Sort items (custom key optional) | list     | Key function (optional) |

# Databricks notebook source
# MAGIC %md
# MAGIC ### Transformer functions
# MAGIC <table>
# MAGIC   <thead>
# MAGIC     <tr>
# MAGIC       <th>Function</th>
# MAGIC       <th>Purpose</th>
# MAGIC       <th>Returns</th>
# MAGIC       <th>Function Type</th>
# MAGIC     </tr>
# MAGIC   </thead>
# MAGIC   <tbody>
# MAGIC     <tr>
# MAGIC       <td><code>map()</code></td>
# MAGIC       <td>Transform each element</td>
# MAGIC       <td>map object</td>
# MAGIC       <td>Any transformation</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td><code>filter()</code></td>
# MAGIC       <td>Select items by condition</td>
# MAGIC       <td>filter object</td>
# MAGIC       <td>Boolean-returning</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td><code>reduce()</code></td>
# MAGIC       <td>Combine items into one</td>
# MAGIC       <td>Single value</td>
# MAGIC       <td>Binary function</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td><code>sorted()</code></td>
# MAGIC       <td>Sort items (custom key optional)</td>
# MAGIC       <td>list</td>
# MAGIC       <td>Key function (optional)</td>
# MAGIC     </tr>
# MAGIC   </tbody>
# MAGIC </table>
# MAGIC
# MAGIC This notebook explains four powerful built-in functions in Python:
# MAGIC - `map()`
# MAGIC - `filter()`
# MAGIC - `reduce()`
# MAGIC - `sorted()`
# MAGIC
# MAGIC Each section includes theory and examples using named functions without using `lambda`

# COMMAND ----------

# MAGIC %md ### 1. map()
# MAGIC ### syntax : `map(function, iterable)`
# MAGIC - > **What it does**: Applies a function to each item in an iterable and returns a new iterable (a `map` object).
# MAGIC - > **Use case**: When you want to transform or modify each element.

# COMMAND ----------

# DBTITLE 1, Example: Squaring numbers with `map()`
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# COMMAND ----------

# MAGIC %md ### 2. filter()
# MAGIC ### syntax: `filter(function, iterable)`
# MAGIC - > **What it does**: filters items in an iterable using a function that returns `True` or `False`.  
# MAGIC - > **Use case**: when you want to keep only items that meet a condition.

# COMMAND ----------

# DBTITLE 1, Example: Filtering even numbers with `filter()`
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

# COMMAND ----------

# MAGIC %md ### 3. reduce()
# MAGIC ### `reduce(function, iterable)`
# MAGIC - > **What it does**: Applies a rolling computation to sequential pairs of items.  
# MAGIC - > **Use case**: When you want to reduce a list to a single value (like a sum or product).  
# MAGIC - > `reduce()` comes from the `functools` module.

# COMMAND ----------

# DBTITLE 1, Example: Multiplying all elements with `reduce()`
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)

print(product)  # Output: 24

# COMMAND ----------

# MAGIC %md ### 4. sorted()
# MAGIC ### `sorted(iterable, key=..., reverse=...)`
# MAGIC - > **What it does**: Returns a new sorted list from the items in an iterable.  
# MAGIC - > **Use case**: Sort using default or custom key (e.g., sort by string length).
# MAGIC
# MAGIC **Parameters**: 
# MAGIC - >  `key` is optional and often used for custom sorting. 
# MAGIC - > `reverse` is not mandatory can be either `True` or `False` and used to apply reverse sort on the iterable

# COMMAND ----------

# DBTITLE 1, Example: Sorting words by length with `sorted()`
- > **Note**: key is optional. often used for custom sortingdef get_length(word):
    return len(word)

words = ['apple', 'banana', 'kiwi', 'cherry']
sorted_words = sorted(words, key=get_length)

print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'cherry']

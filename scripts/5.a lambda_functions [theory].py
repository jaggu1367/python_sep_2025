# Databricks notebook source
# MAGIC %md
# MAGIC ## 💡 What is a Lambda Function in Python?
# MAGIC
# MAGIC A **lambda** function in Python is a small **anonymous function**. It can take any number of arguments, but **can only have one expression**.
# MAGIC
# MAGIC **Why use lambda?**
# MAGIC - To write quick, throwaway functions
# MAGIC - For functional programming (alongside `map`, `filter`, `reduce`)
# MAGIC - Used where function objects are needed temporarily
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC lambda arguments: expression
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Basic Lambda Function Examples
# Simple lambda function to add 10 to a number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(4, 5))  # Output: 20

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Lambda vs Regular Function
# MAGIC
# MAGIC Let's compare how we define a regular function vs. a lambda function.

# COMMAND ----------

# DBTITLE 1,Lambda vs Regular Function
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print("Regular Function:", square(6))
print("Lambda Function:", square_lambda(6))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Using Lambda with `map()`
# MAGIC
# MAGIC `map()` applies a function to **all items** in an iterable (like a list).
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC map(function, iterable)
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Lambda with map()
numbers = [1, 2, 3, 4, 5]

# Double each number using lambda
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Using Lambda with `filter()`
# MAGIC
# MAGIC `filter()` filters elements from a list based on a condition.
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC filter(function, iterable)
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Lambda with filter()
# Get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)

# Filter names starting with 'A'
names = ["Alice", "Bob", "Ankit", "Charlie"]
starts_with_A = list(filter(lambda name: name.startswith('A'), names))
print("Names starting with A:", starts_with_A)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Using Lambda with `reduce()`
# MAGIC
# MAGIC `reduce()` is used to apply a rolling computation to sequential pairs of values in a list.
# MAGIC
# MAGIC You must import it from `functools`.

# COMMAND ----------

# DBTITLE 1,Lambda with reduce()
from functools import reduce

# Sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Lambda in Sorting (Custom Sort)
# MAGIC
# MAGIC Lambda functions are often used as the key function in sorting lists of tuples or dictionaries.

# COMMAND ----------

# DBTITLE 1,Using Lambda for Sorting
# Sort list of tuples by second item
data = [(1, 4), (3, 1), (5, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted by 2nd item:", sorted_data)

# Sort dictionary by value
my_dict = {'apple': 10, 'banana': 5, 'orange': 7}
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
print("Sorted by value:", sorted_items)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Lambda with `if-else` (Ternary Operator)
# MAGIC
# MAGIC Lambda can include conditional expressions like:
# MAGIC ```python
# MAGIC lambda x: x if x > 0 else -x
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Lambda with Conditional Logic
# Absolute value using lambda
absolute = lambda x: x if x >= 0 else -x
print(absolute(5))    # 5
print(absolute(-5))   # 5

# Check even or odd
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(4))  # Even
print(even_or_odd(7))  # Odd

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Nested Lambda Functions
# MAGIC
# MAGIC You can nest lambda functions to create curried functions.

# COMMAND ----------

# DBTITLE 1,Nested Lambda Functions
# Create a lambda that adds two numbers, one at a time
add = lambda x: (lambda y: x + y)
add_5 = add(5)
print(add_5(10))  # 15

# Another way to directly use nested lambda
print((lambda x: (lambda y: x * y))(3)(4))  # 12

# COMMAND ----------

# MAGIC %md
# MAGIC ## 👉 Interview-style Lambda Challenges
# MAGIC
# MAGIC Let's explore some examples that mimic real interview questions.

# COMMAND ----------

# DBTITLE 1,Interview-Oriented Lambda Exercises
# 1. Sort a list of strings by their length
words = ['apple', 'banana', 'kiwi', 'grape']
sorted_by_len = sorted(words, key=lambda x: len(x))
print("Sorted by length:", sorted_by_len)

# 2. Create a lambda to extract last character
last_char = lambda s: s[-1]
print("Last char of 'Python':", last_char("Python"))

# 3. Count how many strings start with a vowel using filter + lambda
words = ['apple', 'orange', 'grape', 'umbrella', 'banana']
vowel_words = list(filter(lambda x: x[0].lower() in 'aeiou', words))
print("Starts with vowel:", vowel_words)
print("Count:", len(vowel_words))

# 4. Multiply only even numbers from list
nums = [1, 2, 3, 4, 5, 6]
even_product = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, nums))
print("Product of even numbers:", even_product)
# 5. Sort a list of tuples by the last character of the second element
pairs = [('a', 'cat'), ('b', 'dog'), ('c', 'bat')]
sorted_pairs = sorted(pairs, key=lambda x: x[1][-1])
print("Sorted by last char of 2nd element:", sorted_pairs)

# 6. Extract all uppercase words from a list using filter and lambda
words = ['Python', 'JAVA', 'sql', 'HTML', 'css']
uppercase_words = list(filter(lambda x: x.isupper(), words))
print("Uppercase words:", uppercase_words)

# 7. Find max length word using reduce and lambda
from functools import reduce
words = ['data', 'machine', 'learning', 'AI']
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("Longest word:", longest)

# 8. Convert a list of temperatures in Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))
print("Fahrenheit:", fahrenheit)

# 9. Count how many numbers are divisible by 3 or 5
nums = list(range(1, 21))
div_3_or_5 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, nums))
print("Divisible by 3 or 5:", div_3_or_5)
print("Count:", len(div_3_or_5))

# 10. Create a list of squares for only odd numbers
nums = [1, 2, 3, 4, 5, 6, 7]
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, nums)))
print("Squares of odd numbers:", odd_squares)

# 11. Sort a list of dictionaries by a specific key using lambda
people = [{'name': 'Alice', 'age': 30},
          {'name': 'Bob', 'age': 25},
          {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda x: x['age'])
print("Sorted by age:", sorted_people)

# 12. Filter out palindromes from a list
words = ['madam', 'apple', 'racecar', 'banana', 'level']
palindromes = list(filter(lambda x: x == x[::-1], words))
print("Palindromes:", palindromes)

# 13. Find the word with most vowels using reduce + lambda
vowel_count = lambda word: sum(map(lambda c: c in 'aeiouAEIOU', word))
words = ['data', 'science', 'artificial', 'intelligence']
most_vowels = reduce(lambda a, b: a if vowel_count(a) > vowel_count(b) else b, words)
print("Word with most vowels:", most_vowels)

# 14. Add index to list items using map and lambda (like enumerate)
words = ['one', 'two', 'three']
indexed = list(map(lambda x: f"{x[0]}: {x[1]}", enumerate(words)))
print("Indexed words:", indexed)

# 15. Format a list of full names into initials using lambda and map
names = ["John Doe", "Jane Smith", "Alice Johnson"]
# Convert to "J.D.", "J.S.", etc.
initials = list(map(lambda name: '.'.join([part[0].upper() for part in name.split()]) + '.', names))
print("Formatted initials:", initials)



# COMMAND ----------

# MAGIC %md
# MAGIC ## *** Summary ***
# MAGIC
# MAGIC Lambda functions are powerful tools in Python, especially when used with:
# MAGIC - `map()`, `filter()`, `reduce()`
# MAGIC - Sorting custom structures
# MAGIC - Conditional logic
# MAGIC
# MAGIC **Tip:** Use lambda when the function is small and used only once. Otherwise, prefer regular functions for readability.

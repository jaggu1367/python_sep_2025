# Databricks notebook source
# MAGIC %md
# MAGIC # 🐍 Mastering Python Lists
# MAGIC
# MAGIC Welcome! In this notebook, we'll explore all the essential operations on **Python Lists**:
# MAGIC
# MAGIC - Creating a list
# MAGIC - Printing a list
# MAGIC - Finding list size
# MAGIC - Adding/removing elements
# MAGIC - Accessing by index
# MAGIC - List concatenation
# MAGIC - Iterating over a list
# MAGIC - List comprehension (with examples)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 1. Creating a List
# MAGIC
# MAGIC In Python, lists are defined using square brackets `[]`. Let's create a list of integers.

# COMMAND ----------

# DBTITLE 1,creating a list
numbers = [1, 2, 3, 4, 5]
numbers

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 2. Printing the List
# MAGIC
# MAGIC Use the `print()` function to display the contents of a list.

# COMMAND ----------

# DBTITLE 1,print the list
print(numbers)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 3. Finding the Size of a List
# MAGIC
# MAGIC Use the `len()` function to find the number of elements in a list.

# COMMAND ----------

# DBTITLE 1,finding size
size_of_list = len(numbers)
print(f"Size of the list: {size_of_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 4. Adding an Element to a List
# MAGIC
# MAGIC Use the `append()` method to add a new element at the end of a list.

# COMMAND ----------

# DBTITLE 1,adding element to list
numbers.append(6)
print(numbers)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 5. Accessing Elements by Index
# MAGIC
# MAGIC Python lists are zero-indexed.
# MAGIC
# MAGIC - Use `[0]` to access the first element.
# MAGIC - Use `[-1]` to access the last element.

# COMMAND ----------

# DBTITLE 1,accessing elements using index
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 6. Removing Elements from a List
# MAGIC
# MAGIC - `remove(x)`: removes the first occurrence of value `x`
# MAGIC - `pop()`: removes the last element by default

# COMMAND ----------

# DBTITLE 1,removing elements from a List
numbers.remove(3)
print(f"After removing 3: {numbers}")

removed = numbers.pop()
print(f"After popping last element: {numbers}")
print(f"Popped element: {removed}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 7. Adding One List to Another List
# MAGIC
# MAGIC - Use `extend()` to add elements of one list to another.
# MAGIC - Use `+` to concatenate lists.

# COMMAND ----------

# DBTITLE 1,concatenate lists
another_list = [7, 8, 9]
numbers.extend(another_list)
print(f"After extending: {numbers}")

numbers = numbers + [10, 11]
print(f"After adding another list: {numbers}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 8. Iterating Over a List
# MAGIC
# MAGIC Use a `for` loop to process each item in a list.

# COMMAND ----------

# DBTITLE 1,iterate over a list/ traverse through the list
for num in numbers:
    print(num)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📌 9. Creating a New List Using a Generic `for` Loop
# MAGIC
# MAGIC Let's create a list of squares using a standard `for` loop.

# COMMAND ----------

# DBTITLE 1,create new list using another list
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(f"Squared numbers: {squared_numbers}")

# COMMAND ----------

# MAGIC %md
# MAGIC # 🚀 List Comprehension
# MAGIC
# MAGIC List comprehension is a concise way to create new lists in Python.
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC [expression for item in iterable if condition]
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Example 1: Squares of Numbers

# COMMAND ----------

# DBTITLE 1,list comprehension example 1
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Example 2: Filter Even Numbers

# COMMAND ----------

# DBTITLE 1,list comprehension example 2
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Example 3: Multiply Elements by 10

# COMMAND ----------

# DBTITLE 1,list comprehension example 3
times_ten = [x * 10 for x in numbers]
print(f"Numbers ×10: {times_ten}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Example 4: Words Longer Than 3 Characters

# COMMAND ----------

# DBTITLE 1,list comprehension example 4
words = ['apple', 'is', 'a', 'fruit', 'banana']
long_words = [word for word in words if len(word) > 3]
print(f"Words > 3 characters: {long_words}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Example 5: Flatten a Nested List

# COMMAND ----------

# DBTITLE 1,list comprehension example 5
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Flattened list: {flattened}")

# COMMAND ----------

# MAGIC %md
# MAGIC # 🎓 Summary & Challenge
# MAGIC
# MAGIC You learned how to:
# MAGIC - Create and manipulate Python lists
# MAGIC - Access, add, and remove elements
# MAGIC - Use list comprehension to transform data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🔥 Challenges for You:**
# MAGIC ---
# MAGIC **🔥 Challenge 1:**
# MAGIC **Sort the list** in descending order and print the elements
# MAGIC ---
# MAGIC
# MAGIC **🔥 Challenge 2:**
# MAGIC **Remove duplicates** in a list
# MAGIC ---
# MAGIC
# MAGIC **🔥 Challenge 3:**
# MAGIC Create a list of **prime numbers between 1 and 100** using list comprehension!
# MAGIC ---

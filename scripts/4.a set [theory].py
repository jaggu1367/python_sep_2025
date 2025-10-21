# Databricks notebook source
# MAGIC %md
# MAGIC # Python Sets
# MAGIC
# MAGIC Sets are **unordered collections** of **unique** elements.
# MAGIC They are useful when you want to store distinct items and perform operations like union, intersection, difference, etc.

# COMMAND ----------

# DBTITLE 1,Creating Sets - Examples
# Creating sets using curly braces
set1 = {1, 2, 3, 4, 5}
print("Set1:", set1)

# Creating a set from a list (duplicates removed)
set2 = set([3, 4, 4, 5, 6, 7])
print("Set2:", set2)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set Characteristics
# MAGIC - Sets are **unordered**: elements have no index.
# MAGIC - Sets contain **unique** elements only.
# MAGIC - Sets are **mutable** (you can add or remove elements).
# MAGIC - Sets **cannot contain mutable elements** like lists or dictionaries.

# COMMAND ----------

# DBTITLE 1,Accessing & Modifying Sets
# You cannot access elements by index because sets are unordered
# But you can add or remove elements

my_set = {1, 2, 3}
print("Original set:", my_set)

# Adding elements
my_set.add(4)
print("After adding 4:", my_set)

# Adding multiple elements
my_set.update([5, 6])
print("After adding 5 and 6:", my_set)

# Removing elements
my_set.remove(2)  # Raises error if element not found
print("After removing 2:", my_set)

my_set.discard(10) # Does NOT raise error if element not found
print("After discarding 10 (not present):", my_set)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set Operations
# MAGIC - **Union:** combine all unique elements
# MAGIC - **Intersection:** common elements
# MAGIC - **Difference:** elements in one set but not in another
# MAGIC - **Symmetric Difference:** elements in either set but not both

# COMMAND ----------

# DBTITLE 1,Set Operations - Examples
a = {1, 2, 3, 4} 
b = {3, 4, 5, 6}

print("Set a:", a)
print("Set b:", b)

print("Union (a | b):", a | b)
print("Intersection (a & b):", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference (a ^ b):", a ^ b)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Other Useful Set Methods
# MAGIC - `issubset()`
# MAGIC - `issuperset()`
# MAGIC - `copy()`
# MAGIC - `clear()`

# COMMAND ----------

# DBTITLE 1,Other Set Methods - Examples
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print("x:", x)
print("y:", y)

print("Is x subset of y?", x.issubset(y))
print("Is y superset of x?", y.issuperset(x))

# Copying a set
z = x.copy()
print("Copy of x:", z)

# Clearing a set
z.clear()
print("After clearing z:", z)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Practice Exercises
# MAGIC - Create a set from a list and remove duplicates.
# MAGIC - Find the union and intersection of two sets.
# MAGIC - Check if one set is a subset of another.
# MAGIC - Remove an element safely from a set without error if it doesn’t exist.

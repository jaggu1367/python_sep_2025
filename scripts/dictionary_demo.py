# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 1: Creating a Dictionary
# MAGIC 
# MAGIC In this cell, we will create a Python dictionary with initial key-value pairs.

# COMMAND 1, Create a dictionary with initial key-value pairs
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 2: Adding a New Key-Value Pair
# MAGIC 
# MAGIC This cell demonstrates how to add a new key-value pair to an existing dictionary.

# COMMAND 2, Add a new key-value pair
my_dict["orange"] = 4
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 3: Updating the Value of an Existing Key
# MAGIC 
# MAGIC In this cell, we will update the value of an existing key in the dictionary.

# COMMAND 3, Update the value of an existing key
my_dict["banana"] = 5
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 4: Deleting a Key-Value Pair
# MAGIC 
# MAGIC Demonstrates how to delete a specific key-value pair using `del`.

# COMMAND 4, Delete a key-value pair
del my_dict["cherry"]
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 5: Using `pop()` to Remove a Key-Value Pair
# MAGIC 
# MAGIC The `pop()` method removes a key and returns its value.

# COMMAND 5, Remove a key-value pair using pop()
removed_value = my_dict.pop("apple")
removed_value, my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 6: Using `popitem()` to Remove the Last Inserted Item
# MAGIC 
# MAGIC The `popitem()` method removes and returns the last inserted key-value pair.

# COMMAND 6, Remove the last inserted item using popitem()
last_item = my_dict.popitem()
last_item, my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 7: Clearing All Items in the Dictionary
# MAGIC 
# MAGIC The `clear()` method removes all key-value pairs from the dictionary.

# COMMAND 7, Clear all items in the dictionary
my_dict.clear()
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 8: Using `update()` to Merge Two Dictionaries
# MAGIC 
# MAGIC The `update()` method is used to merge one dictionary into another.

# COMMAND 8, Merge two dictionaries using update()
another_dict = {"kiwi": 6, "grape": 7}
my_dict.update(another_dict)
my_dict

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 9: Checking if a Key Exists in a Dictionary
# MAGIC 
# MAGIC Use the `in` keyword to check if a key exists.

# COMMAND 9, Check if a key exists in the dictionary
key_exists = "kiwi" in my_dict
key_exists

# Databricks notebook source
# MAGIC %md
# MAGIC # Cell 10: Iterating Through a Dictionary
# MAGIC 
# MAGIC Use a `for` loop to iterate through key-value pairs.

# COMMAND 10, Iterate through dictionary items
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

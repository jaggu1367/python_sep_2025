# Databricks notebook source
# MAGIC %md
# MAGIC # 1: Creating a Dictionary
# MAGIC
# MAGIC Let's create a Python dictionary with initial key-value pairs.

# COMMAND ----------

# DBTITLE 1,create a dictionary
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
my_dict

# COMMAND ----------

# MAGIC %md
# MAGIC # 2: Adding a New Key-Value Pair
# MAGIC
# MAGIC Demonstrate how to add a new key-value pair to an existing dictionary.

# COMMAND ----------

# DBTITLE 1,add a new key value pair
my_dict["orange"] = 4
my_dict

# COMMAND ----------

# MAGIC %md
# MAGIC # 3: Updating the Value of an Existing Key
# MAGIC
# MAGIC update the value of an existing key in the dictionary.

# COMMAND ----------

# DBTITLE 1,update a value of existing key
my_dict["banana"] = 5
my_dict

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 4: Deleting a Key-Value Pair
# MAGIC
# MAGIC Demonstrates how to delete a specific key-value pair using `del`.

# COMMAND ----------

# DBTITLE 1,delete a specific item using key
del my_dict["cherry"]
my_dict

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 5: Using `pop()` to Remove a Key-Value Pair
# MAGIC
# MAGIC The `pop()` method removes a key and returns its value.

# COMMAND ----------

# DBTITLE 1,using pop()
removed_value = my_dict.pop("apple")
removed_value, my_dict

# COMMAND ----------

# MAGIC %md
# MAGIC # 6: Using `popitem()` to Remove the Last Inserted Item
# MAGIC
# MAGIC The `popitem()` method removes and returns the last inserted key-value pair.

# COMMAND ----------

# DBTITLE 1,using popitem()
last_item = my_dict.popitem()
last_item, my_dict

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 7: Clearing All Items in the Dictionary
# MAGIC
# MAGIC The `clear()` method removes all key-value pairs from the dictionary.

# COMMAND ----------

# DBTITLE 1,using clear()
my_dict.clear()
my_dict

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 8: Using `update()` to Merge Two Dictionaries
# MAGIC
# MAGIC The `update()` method is used to merge one dictionary into another.

# COMMAND ----------

# DBTITLE 1,using update()
another_dict = {"kiwi": 6, "grape": 7}
my_dict.update(another_dict)
my_dict

# COMMAND ----------

# MAGIC %md
# MAGIC # 9: Checking if a Key Exists in a Dictionary
# MAGIC
# MAGIC Use the `in` keyword to check if a key exists.

# COMMAND ----------

# DBTITLE 1,check if key is present using in
key_exists = "kiwi" in my_dict
key_exists

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 10: getting list of keys from a Dictionary
# MAGIC keys() method returns list of keys
# MAGIC

# COMMAND ----------

# DBTITLE 1,using keys()
for key in my_dict.keys():
    print(key)

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # 11: Iterating Through a Dictionary
# MAGIC
# MAGIC Use a `for` loop to iterate through key-value pairs.

# COMMAND ----------

# DBTITLE 1,for loop iteration
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Databricks notebook source
# MAGIC %md
# MAGIC ### Question 1
# MAGIC Use `map()` with `lambda` to divide each value in the list by 3.
# MAGIC
# MAGIC **Input:**  
# MAGIC nums = [12, 17, 5, 30, 21]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [4.0, 5.666666666666667, 1.6666666666666667, 10.0, 7.0]

# COMMAND ----------

# DBTITLE 1, Question_1_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 2
# MAGIC Use `map()` with `lambda` to capitalize each name in the tuple.
# MAGIC
# MAGIC **Input:**  
# MAGIC names = ("alice", "Bob", "CHARLIE")
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["Alice", "Bob", "Charlie"]

# COMMAND ----------

# DBTITLE 1, Question_2_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 3
# MAGIC Use `map()` with `lambda` on dictionary items to generate strings of format "Name:Value".
# MAGIC
# MAGIC **Input:**  
# MAGIC sales = {"Alice":1500, "Bob":2300, "Charlie":1800}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["Alice:1500", "Bob:2300", "Charlie:1800"]

# COMMAND ----------

# DBTITLE 1, Question_3_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 4
# MAGIC Convert Celsius temperatures to Fahrenheit using `map()` and `lambda`.
# MAGIC
# MAGIC **Input:**  
# MAGIC temps = {23.4, 19.8, 30.2, 25.0}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC Values converted using (C * 9/5 + 32), order may vary.

# COMMAND ----------

# DBTITLE 1, Question_4_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 5
# MAGIC Use `map()` with `lambda` to sum two lists element-wise.
# MAGIC
# MAGIC **Input:**  
# MAGIC a = [1,2,3]  
# MAGIC b = [4,5,6]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [5, 7, 9]

# COMMAND ----------

# DBTITLE 1, Question_5_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 6
# MAGIC Use `filter()` with `lambda` to keep numbers that are multiples of 4.
# MAGIC
# MAGIC **Input:**  
# MAGIC nums = [3, 12, 8, 5, 21, 16]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [12, 8, 16]

# COMMAND ----------

# DBTITLE 1, Question_6_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 7
# MAGIC Use `filter()` with `lambda` to retain words with length ≥ 5.
# MAGIC
# MAGIC **Input:**  
# MAGIC words = ("data", "AI", "python", "ML", "deeplearning")
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["python", "deeplearning"]

# COMMAND ----------

# DBTITLE 1, Question_7_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 8
# MAGIC Filter dictionary items whose stock > 0.
# MAGIC
# MAGIC **Input:**  
# MAGIC inventory = {"apple":5, "banana":2, "cherry":0, "date":4}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC {"apple":5, "banana":2, "date":4}

# COMMAND ----------

# DBTITLE 1, Question_8_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 9
# MAGIC Filter only positive numbers.
# MAGIC
# MAGIC **Input:**  
# MAGIC values = {10, -3, 0, 7, -1, 15}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [10, 7, 15] (order may vary)

# COMMAND ----------

# DBTITLE 1, Question_9_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 10
# MAGIC Filter transactions where amt ≥ 100, then keep only "user".
# MAGIC
# MAGIC **Input:**  
# MAGIC transactions = [ {"user":"A","amt":100}, {"user":"B","amt":30}, {"user":"A","amt":200}, {"user":"C","amt":20} ]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["A", "A"]

# COMMAND ----------

# DBTITLE 1, Question_10_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 11
# MAGIC Use `reduce()` with `lambda` to compute product of numbers.
# MAGIC
# MAGIC **Input:**  
# MAGIC nums = [2,3,5,7,11]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC 2310

# COMMAND ----------

# DBTITLE 1, Question_11_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 12
# MAGIC Use `reduce()` to join words with hyphens.
# MAGIC
# MAGIC **Input:**  
# MAGIC words = ("one","two","three")
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC "one-two-three"

# COMMAND ----------

# DBTITLE 1, Question_12_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 13
# MAGIC Use `reduce()` to find maximum price.
# MAGIC
# MAGIC **Input:**  
# MAGIC prices = {"A":10, "B":15, "C":5}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC 15

# COMMAND ----------

# DBTITLE 1, Question_13_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 14
# MAGIC Sum all durations using `reduce()`.
# MAGIC
# MAGIC **Input:**  
# MAGIC durations = {2.5, 3.0, 1.75, 4.25}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC 11.5

# COMMAND ----------

# DBTITLE 1, Question_14_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 15
# MAGIC Aggregate total score & count using `reduce()`.
# MAGIC
# MAGIC **Input:**  
# MAGIC records = [ {"id":1,"score":50}, {"id":2,"score":70}, {"id":3,"score":65} ]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC {"total":185, "count":3}

# COMMAND ----------

# DBTITLE 1, Question_15_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 16
# MAGIC Sort names case-insensitively.
# MAGIC
# MAGIC **Input:**  
# MAGIC names = ["alice","Bob","charlie","David"]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["alice","Bob","charlie","David"]

# COMMAND ----------

# DBTITLE 1, Question_16_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 17
# MAGIC Sort employees by age descending.
# MAGIC
# MAGIC **Input:**  
# MAGIC employees = (("A",30),("B",24),("C",29))
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [("A",30),("C",29),("B",24)]

# COMMAND ----------

# DBTITLE 1, Question_17_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 18
# MAGIC Sort dictionary by score descending and return names only.
# MAGIC
# MAGIC **Input:**  
# MAGIC scores = {"Alice":88,"Bob":92,"Charlie":85}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["Bob","Alice","Charlie"]

# COMMAND ----------

# DBTITLE 1, Question_18_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 19
# MAGIC Sort tags by string length.
# MAGIC
# MAGIC **Input:**  
# MAGIC tags = {"python","java","c","javascript","go"}
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC ["c","go","java","python","javascript"]

# COMMAND ----------

# DBTITLE 1, Question_19_Answer
# Write your code here


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 20
# MAGIC Sort list of dicts by name.
# MAGIC
# MAGIC **Input:**  
# MAGIC records = [ {"name":"Alice","age":30}, {"name":"Bob","age":24}, {"name":"Charlie","age":29} ]
# MAGIC
# MAGIC **Expected Output:**  
# MAGIC [{"name":"Alice","age":30},{"name":"Bob","age":24},{"name":"Charlie","age":29}]

# COMMAND ----------

# DBTITLE 1, Question_20_Answer
# Write your code here

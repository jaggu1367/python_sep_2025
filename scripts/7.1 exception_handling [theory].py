# Databricks notebook source
# MAGIC %md
# MAGIC # Python Exception Handling
# MAGIC Learn how to detect and handle runtime errors safely using `try`, `except`, `else`, `finally`, `raise`, and custom exceptions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## What is an Exception?
# MAGIC An **exception** is an error that occurs during program execution.  
# MAGIC Instead of crashing the program, we use **exception handling** to manage errors gracefully.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Basic `try` and `except`
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC try:
# MAGIC     # code that may cause error
# MAGIC except:
# MAGIC     # code to run if error occurs
# MAGIC ```

# COMMAND ----------

# DBTITLE 1, Basic try-except Example
try:
    x = 10 / 0
except:
    print("Error occurred: Division by zero")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Handling Specific Exceptions
# MAGIC We can catch different errors separately.

# COMMAND ----------

# DBTITLE 1, Specific Exception Example
try:
    num = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to number.")
except ZeroDivisionError:
    print("ZeroDivisionError occurred.")
    

# COMMAND ----------

# MAGIC %md
# MAGIC ## `else` Block
# MAGIC Code inside **else** runs only if **no exception occurs**.

# COMMAND ----------

# DBTITLE 1, else Block Example
try:
    result = 10 / 2
except:
    print("An error occurred.")
else:
    print("No errors! Result =", result)

# COMMAND ----------

# MAGIC %md
# MAGIC ## `finally` Block
# MAGIC Code inside **finally** runs **no matter what** (error or no error).
# MAGIC Useful for cleanup operations.

# COMMAND ----------

# DBTITLE 1, finally Block Example
try:
    file = open("/tmp/test_file.txt", "w")
    file.write("Hello!")
except:
    print("Error occurred.")
finally:
    file.close()
    print("File closed successfully.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Raising Exceptions Using `raise`
# MAGIC We can throw an exception manually.

# COMMAND ----------

# DBTITLE 1, raise Example
age = 15
if age < 18:
    raise ValueError("Age must be 18 or older.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Creating Custom Exceptions

# COMMAND ----------

# DBTITLE 1, Custom Exception Example
class AgeTooLowError(Exception):
    pass

try:
    age = 12
    if age < 18:
        raise AgeTooLowError("Custom Error: Age is below allowed limit.")
except AgeTooLowError as e:
    print(e)

# Databricks notebook source
# MAGIC %md
# MAGIC # **Decorators with Return Values (Enhanced)**
# MAGIC
# MAGIC In the previous lesson, we learned how decorators can add behavior **before and after** a function runs.
# MAGIC
# MAGIC Now we learn how decorators can:
# MAGIC
# MAGIC - **Capture the result** returned by the function
# MAGIC - **Modify the result**
# MAGIC - **Return a new or enhanced value**
# MAGIC
# MAGIC The wrapper function generally:
# MAGIC 1. Calls the original function
# MAGIC 2. Stores its return value
# MAGIC 3. Then returns something (same or modified)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Decorator Returning Original Result

# COMMAND ----------

# DBTITLE 1, Basic Return-Passing Decorator
def debug(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        result = func(*args, **kwargs)  # capture result
        print("Returned:", result)
        return result  # return original result unchanged
    return wrapper

@debug
def multiply(a, b):
    return a * b

value = multiply(5, 4)
print("Final Result:", value)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Decorator That **Modifies** the Returned Value

# COMMAND ----------

# DBTITLE 1, Modify Returned Result Example
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2   # modifies output
    return wrapper

@double_result
def sum_two(a, b):
    return a + b

print(sum_two(10, 5))  # Output doubled

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Decorator That Converts Result to Uppercase

# COMMAND ----------

# DBTITLE 1, Text Result Modification
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello {name}"

print(greet("Asha"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Decorator That Ensures Safe Division (Handles Errors)

# COMMAND ----------

# DBTITLE 1, Error Handling via Decorator
def safe_divide(func):
    def wrapper(a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return func(a, b)
    return wrapper

@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

# COMMAND ----------

# MAGIC %md
# MAGIC # ✅ Summary
# MAGIC
# MAGIC Decorators can:
# MAGIC
# MAGIC | Task | How |
# MAGIC |------|-----|
# MAGIC | Capture return value | `result = func()` |
# MAGIC | Return original result | `return result` |
# MAGIC | Modify result | `return modified_result` |
# MAGIC | Add safety/error-checking | Check arguments before calling function |
# MAGIC
# MAGIC Decorators allow us to **extend behavior** without modifying the original function.
# MAGIC

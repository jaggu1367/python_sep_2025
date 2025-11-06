# Databricks notebook source
# MAGIC %md
# MAGIC # **Decorators with Parameters (`@repeat(n)`)**
# MAGIC
# MAGIC A normal decorator takes a function as input.
# MAGIC
# MAGIC But when we need the decorator itself to accept arguments (like `@repeat(3)`), we use:
# MAGIC
# MAGIC 1. A **function that receives arguments** (e.g., repeat count)
# MAGIC 2. That function returns a **decorator function**
# MAGIC 3. The decorator returns the **wrapper function**
# MAGIC
# MAGIC This is called a **Decorator Factory**.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Without Parameters (Reminder)

# COMMAND ----------

# DBTITLE 1, Normal Decorator Reminder
def announce(func):
    def wrapper():
        print("Calling function...")
        func()
    return wrapper

@announce
def hello():
    print("Hello!")

hello()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Decorator **with Parameters**
# MAGIC
# MAGIC Example: `@repeat(3)` → repeat the function 3 times.

# COMMAND ----------

# DBTITLE 1, Decorator with Parameter Example
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):   # repeat n times
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)   # repeat count passed to the decorator
def greet():
    print("Hello!")

greet()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Returning Values While Repeating
# MAGIC
# MAGIC Usually when repeating, we return the **last computed result**.

# COMMAND ----------

# DBTITLE 1, Repeat Decorator Returning Last Result
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result  # return last call result
        return wrapper
    return decorator

@repeat(4)
def add(a, b):
    return a + b

print(add(5, 3))  # Run 4 times but show final return value

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Using Decorator Parameters for Dynamic Behavior

# COMMAND ----------

# DBTITLE 1, Example: Repeat with Message
def repeat_with_message(n, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_with_message(2, "Running the function:")
def say_name(name):
    print("Name:", name)

say_name("Asha")

# COMMAND ----------

# MAGIC %md
# MAGIC # ✅ Summary
# MAGIC
# MAGIC | Part | Meaning |
# MAGIC |------|---------|
# MAGIC | `repeat(n)` | Outer function → accepts decorator parameter |
# MAGIC | `decorator(func)` | Middle function → receives the function |
# MAGIC | `wrapper()` | Inner function → runs function & adds behavior |
# MAGIC
# MAGIC ```
# MAGIC repeat(n) → returns decorator
# MAGIC decorator → returns wrapper
# MAGIC wrapper → calls the function
# MAGIC ```

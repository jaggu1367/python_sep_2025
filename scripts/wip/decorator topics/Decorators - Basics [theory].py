# Databricks notebook source
# MAGIC %md
# MAGIC # **Python Decorators (Beginner Friendly)**
# MAGIC
# MAGIC A **decorator** is a function that **adds extra behavior** to another function **without modifying its code**.
# MAGIC
# MAGIC - Functions are treated as **objects** in Python.
# MAGIC - One function can **take another function as input**.
# MAGIC - A decorator **wraps** another function and **adds functionality** before/after it runs.
# MAGIC
# MAGIC Decorators use the **`@`** symbol.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Functions are Objects in Python

# COMMAND ----------

# DBTITLE 1, Function Assigned to a Variable
def greet():
    print("Hello!")

say = greet  # assign function to variable
say()        # calling through new name

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Passing a Function to Another Function

# COMMAND ----------

# DBTITLE 1, Function Passed as Argument
def add(a, b):
    return a + b

def calculate(func):
    result = func(10, 20)
    print("Result:", result)

calculate(add)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Creating a Simple Decorator (Manually)
# MAGIC
# MAGIC A decorator:
# MAGIC 1. Accepts a function
# MAGIC 2. Defines a wrapper function
# MAGIC 3. Returns the wrapper

# COMMAND ----------

# DBTITLE 1, Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_hello():
    print("Hello!")

decorated = my_decorator(say_hello)
decorated()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Using `@decorator_name` Shortcut

# COMMAND ----------

# DBTITLE 1, Using the @ Syntax
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_bye():
    print("Bye!")

say_bye()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Decorator with Function having Arguments

# COMMAND ----------

# DBTITLE 1, Decorator Supporting Arguments
def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function complete.")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

print("Returned Value:", add(5, 7))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Real-Life Use Case: Logging Function Calls

# COMMAND ----------

# DBTITLE 1, Logging Decorator
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Function '{func.__name__}' was called")
        return func(*args, **kwargs)
    return wrapper

@log
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Asha")

# COMMAND ----------

# MAGIC %md
# MAGIC # ✅ Summary
# MAGIC
# MAGIC | Term | Meaning |
# MAGIC |------|---------|
# MAGIC | Decorator | Function that adds behavior to another function |
# MAGIC | Wrapper Function | Inner function that executes extra code |
# MAGIC | `@decorator` | Shortcut to apply a decorator |
# MAGIC
# MAGIC Decorators let us **extend existing functions** without editing them.

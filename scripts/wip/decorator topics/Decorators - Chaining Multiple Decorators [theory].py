# Databricks notebook source
# MAGIC %md
# MAGIC # **Chaining Multiple Decorators**
# MAGIC
# MAGIC Python allows applying **multiple decorators** to the same function.
# MAGIC
# MAGIC Decorators are applied **from bottom to top**.
# MAGIC
# MAGIC ```
# MAGIC @decorator_A
# MAGIC @decorator_B
# MAGIC def func():
# MAGIC     pass
# MAGIC ```
# MAGIC
# MAGIC Means:
# MAGIC ```
# MAGIC func = decorator_A(decorator_B(func))
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 1: Two Simple Decorators

# COMMAND ----------

# DBTITLE 1, Chaining Two Decorators
def star(func):
    def wrapper(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")
    return wrapper

def line(func):
    def wrapper(*args, **kwargs):
        print("-----")
        func(*args, **kwargs)
        print("-----")
    return wrapper

@star
@line
def say_hello():
    print("Hello!")

say_hello()

# COMMAND ----------

# MAGIC %md
# MAGIC **Explanation**
# MAGIC
# MAGIC - `@line` is applied **first**
# MAGIC - Result is passed to `@star`
# MAGIC
# MAGIC So **output layer = decorator order from top to bottom**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 2: Decorators That Modify Return Values

# COMMAND ----------

# DBTITLE 1, Decorators with Return Values
def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

def square(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@double
@square
def number():
    return 3

print(number())  # What do you think this will output?

# COMMAND ----------

# MAGIC %md
# MAGIC ### Output Explanation
# MAGIC
# MAGIC ```
# MAGIC number() → square wrapper → 3^2 = 9 → double wrapper → 9 * 2 = 18
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 3: Real-Life Use Case (Logging + Performance Time)

# COMMAND ----------

# DBTITLE 1, Logging + Timing Decorators
import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@log
@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

print("Result:", slow_add(5, 7))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC | Item | Meaning |
# MAGIC |------|---------|
# MAGIC | Decorators stack from **bottom to top** | Bottom decorator executes first |
# MAGIC | Return values chain through each decorator | Careful when modifying return |
# MAGIC | Useful for logging, timing, access control | Often used in real systems |
# MAGIC
# MAGIC ```
# MAGIC @A
# MAGIC @B
# MAGIC def f():
# MAGIC     pass
# MAGIC
# MAGIC Equivalent:  f = A(B(f))
# MAGIC ```

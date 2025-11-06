# Databricks notebook source
# MAGIC %md
# MAGIC # **Class Decorators**
# MAGIC
# MAGIC A **class decorator** is similar to a function decorator, but it is applied to a **class** instead of a function.
# MAGIC
# MAGIC It takes a **class as input**, modifies or enhances it, and returns **the modified class**.
# MAGIC
# MAGIC ```
# MAGIC @decorator
# MAGIC class MyClass:
# MAGIC     pass
# MAGIC
# MAGIC → MyClass = decorator(MyClass)
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 1: Add a New Method to a Class

# COMMAND ----------

# DBTITLE 1, Adding a Method Using Class Decorator
def add_display_method(cls):
    def display(self):
        print(f"Object of class: {cls.__name__}")
    cls.display = display
    return cls

@add_display_method
class Sample:
    pass

obj = Sample()
obj.display()  # New method added by decorator!

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ The decorator took the class and added a new method to it.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 2: Automatically Logging Object Creation

# COMMAND ----------

# DBTITLE 1, Logging Constructor Calls
def log_creation(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        print(f"[LOG] Creating instance of {cls.__name__}")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    return cls

@log_creation
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ The decorator **wrapped the original `__init__`** to add logging.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 3: Enforcing Class Rules (No Empty Attributes!)

# COMMAND ----------

# DBTITLE 1, Enforcing Attribute Checks
def no_empty_strings(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        for value in args:
            if value == "":
                raise ValueError("Attributes cannot be empty strings!")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    return cls

@no_empty_strings
class Product:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

item1 = Product("Laptop", "Dell")   # Works
# item2 = Product("", "HP")         # Uncomment to see error

print(item1.name, item1.brand)

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ The decorator **validates attributes before the object is created.**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 4: Class Decorator That Converts All Attribute Names to Uppercase

# COMMAND ----------

# DBTITLE 1, Modifying Attributes After Object Creation
def uppercase_attributes(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, value in self.__dict__.items():
            if isinstance(value, str):
                setattr(self, attr, value.upper())
    
    cls.__init__ = new_init
    return cls

@uppercase_attributes
class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

c = City("Hyderabad", "India")
print(c.name, c.country)

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Useful when you want to **enforce formatting / data standardization**.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC | Concept | Meaning |
# MAGIC |--------|---------|
# MAGIC | Class Decorator | Decorator applied to a class instead of a function |
# MAGIC | Input | The **class** being decorated |
# MAGIC | Output | Usually the same class (optionally modified) |
# MAGIC | Common Uses | Logging, validation, auto adding methods, enforcing rules |
# MAGIC
# MAGIC ```
# MAGIC @decorator
# MAGIC class MyClass:
# MAGIC     ...
# MAGIC
# MAGIC → MyClass = decorator(MyClass)
# MAGIC ```
# MAGIC

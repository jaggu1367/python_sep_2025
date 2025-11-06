# Databricks notebook source
# MAGIC %md
# MAGIC # **Property Decorators (`@property`)**
# MAGIC
# MAGIC In Python, we use **`@property`** to **access methods like attributes**.
# MAGIC
# MAGIC This allows:
# MAGIC - **Controlled access** to variables (getter)
# MAGIC - **Validation before setting values** (setter)
# MAGIC - **Restriction of value updates** (deleter)
# MAGIC
# MAGIC Instead of:
# MAGIC ```
# MAGIC obj.get_value()
# MAGIC obj.set_value(10)
# MAGIC ```
# MAGIC We can write:
# MAGIC ```
# MAGIC obj.value
# MAGIC obj.value = 10
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 1: Simple Getter Using `@property`

# COMMAND ----------

# DBTITLE 1, Simple Property Getter
class Student:
    def __init__(self, name):
        self._name = name   # Notice: we use _name (suggested private)

    @property
    def name(self):
        return self._name

s = Student("Rahul")
print(s.name)   # Accessed like a variable, but it is actually a method

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ `@property` makes method **look like a variable**.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 2: Getter + Setter (Value Validation)

# COMMAND ----------

# DBTITLE 1, Property with Setter
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary   # Getter

    @salary.setter
    def salary(self, value):  # Setter
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

e = Employee(50000)
print(e.salary)

e.salary = 60000    # Calls setter
print(e.salary)

# e.salary = -1000   # Uncomment to see validation error

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Setter allows us to **control how data is changed**.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 3: Read-Only Property (No Setter)

# COMMAND ----------

# DBTITLE 1, Read-Only Property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius * self._radius

c = Circle(5)
print(c.area)

# c.area = 10  # ❌ Error: No setter defined → area is read-only

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Useful when the value should **not be modified** directly.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example 4: Deleter (`@propertyname.deleter`)

# COMMAND ----------

# DBTITLE 1, Using Deleter
class Account:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print("Deleting username...")
        self._username = None

a = Account("user123")
print(a.username)
del a.username
print(a.username)

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Deleter helps handle **cleanup** when attributes are removed.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC | Decorator | Purpose |
# MAGIC |----------|----------|
# MAGIC | `@property` | Used to define **getter** |
# MAGIC | `@variable.setter` | Used to define **setter** |
# MAGIC | `@variable.deleter` | Used to define **deleter** |
# MAGIC
# MAGIC ```
# MAGIC class Example:
# MAGIC     @property
# MAGIC     def value(self): ...
# MAGIC
# MAGIC     @value.setter
# MAGIC     def value(self, x): ...
# MAGIC
# MAGIC     @value.deleter
# MAGIC     def value(self): ...
# MAGIC ```
# MAGIC

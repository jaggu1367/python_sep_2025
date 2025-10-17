# Databricks notebook source
# MAGIC %md
# MAGIC ## 1. Introduction to Strings
# MAGIC - Strings are sequences of characters enclosed in quotes.
# MAGIC - Strings can be created using <br> single quotes `'...'`<br> double quotes `"..."` and <br> triple quotes `'''...'''` or `"""..."""`.
# MAGIC **Examples:**

# COMMAND ----------

# DBTITLE 1,Introduction to Strings - Examples
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''This is
a multi-line
string'''
print(single_quote)
print(double_quote)
print(triple_quote)

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC ## 2. String Basics
# MAGIC - Access characters using indexing.
# MAGIC - Slice strings to get substrings.
# MAGIC - Use `len()` to find the length of a string.

# COMMAND ----------

# DBTITLE 1,String Basics - Indexing, Slicing, Length
s = "Python"
print(s[0])   # P
print(s[-1])  # n
print(s[1:4]) # yth
print(len(s)) # 6

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. String Operations
# MAGIC - Concatenate strings with `+`
# MAGIC - Repeat strings with `*`
# MAGIC - Check membership with `in`

# COMMAND ----------

# DBTITLE 1,String Operations - Concatenation, Repetition, Membership
a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
print(a * 3)         # HelloHelloHello
print('H' in a)      # True

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Common String Methods
# MAGIC Some useful string methods:
# MAGIC - `lower()`, `upper()` - change case
# MAGIC - `strip()` - remove whitespace from start/end
# MAGIC - `replace()` - replace parts of string
# MAGIC - `split()` - split string into a list
# MAGIC - `join()` - join list into string
# MAGIC - `find()` - find substring position
# MAGIC - `count()` - count occurrences

# COMMAND ----------

# DBTITLE 1,Common String Methods - Examples
text = "  Hello World!  "
print(text.lower())      # hello world!
print(text.strip())      # Hello World!
print(text.replace("World", "Python"))  # Hello Python!
print(text.split())      # ['Hello', 'World!']
print("-".join(["Python", "is", "fun"]))  # Python-is-fun
print(text.find("World")) # 8
print(text.count("l"))    # 3

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Escape Characters
# MAGIC Special characters in strings:
# MAGIC - Newline `\n`
# MAGIC - Tab `\t`
# MAGIC - Quotes inside strings with escape `\"` or `\'`

# COMMAND ----------

# DBTITLE 1,Escape Characters - Examples
print("Hello\nWorld")
print("Hello\tWorld")
print("He said, \"Python is fun!\"")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. String Formatting
# MAGIC Ways to format strings:
# MAGIC - **f-strings** (Python 3.6+)
# MAGIC - `.format()` method
# MAGIC - Old `%` formatting

# COMMAND ----------

# DBTITLE 1,String Formatting - Examples
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Practice Exercises
# MAGIC Try these exercises:
# MAGIC - Extract domain name from an email address
# MAGIC - Count vowels in a string
# MAGIC - Reverse a string
# MAGIC - Check if a string is a palindrome
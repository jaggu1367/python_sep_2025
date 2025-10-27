# Databricks notebook source
# MAGIC %md
# MAGIC # How to open a file in Python?
# MAGIC
# MAGIC You can open files in Python using the `open()` function. There are two main ways:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 1. Using `open()` and manually closing
# MAGIC
# MAGIC python <br>
# MAGIC <pre>
# MAGIC f = open('example.txt', 'r')
# MAGIC content = f.read()
# MAGIC # do something with the content
# MAGIC f.close() 
# MAGIC </pre>
# MAGIC ### You must remember to close the file!
# MAGIC
# MAGIC **Disadvantage:**  
# MAGIC If you forget to call `close()`, the file may remain open, leading to resource leaks or data not being written properly.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 2. Using `with open()` (Context Manager)
# MAGIC
# MAGIC python <br>
# MAGIC <pre>
# MAGIC with open('example.txt', 'r') as f:
# MAGIC     content = f.read()
# MAGIC # File is automatically closed when block ends
# MAGIC </pre>
# MAGIC
# MAGIC **Advantage:**  
# MAGIC The file is automatically closed, even if an error occurs inside the block. This is safer and recommended.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Summary:**  
# MAGIC - `open()` requires manual closing (`close()`).
# MAGIC - `with open()` automatically closes the file, preventing resource leaks.

# COMMAND ----------

# DBTITLE 1,help(open)
help(open)

# COMMAND ----------

# MAGIC %md
# MAGIC # File Handling —  File Open Modes
# MAGIC
# MAGIC ### Introduction & Comparison
# MAGIC
# MAGIC **What are file modes?**
# MAGIC When opening a file in Python you give a *mode* that specifies how you want to work with the file.
# MAGIC
# MAGIC | Mode | Readable? | Writable? | File must exist? | Truncates existing file? |
# MAGIC |------|-----------|-----------|------------------|--------------------------|
# MAGIC | r    | Yes       | No        | Yes              | No                       |
# MAGIC | r+   | Yes       | Yes       | Yes              | No                       |
# MAGIC | w    | No        | Yes       | No (creates)     | Yes (clears file)        |
# MAGIC | w+   | Yes       | Yes       | No (creates)     | Yes (clears file)        |
# MAGIC | a    | No        | Yes       | No (creates)     | No                       |
# MAGIC | a+   | Yes       | Yes       | No (creates)     | No                       |

# COMMAND ----------

# MAGIC %md
# MAGIC # File Handling — File Open Modes Explained

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **r** (Read Only)
# MAGIC - Opens file for **reading only**
# MAGIC - **File must exist**
# MAGIC - Pointer starts at **beginning**

# COMMAND ----------

# DBTITLE 1, Demo_r_mode
with open("/tmp/mode_r_example.txt", "w") as f:
    f.write("Hello Students!\nWelcome to File Handling.")

with open("/tmp/mode_r_example.txt", "r") as f:
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **w** (Write Only)
# MAGIC - Opens file for **writing**
# MAGIC - **Creates** file if not exists
# MAGIC - **Erases** (truncates) existing file content

# COMMAND ----------

# DBTITLE 1, Demo_w_mode
with open("/tmp/mode_w_example.txt", "w") as f:
    f.write("This file was written using w mode.")

with open("/tmp/mode_w_example.txt", "r") as f:
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **a** (Append Only)
# MAGIC - Opens file for **adding new content**
# MAGIC - Does **not** erase existing content
# MAGIC - Always writes **at end**

# COMMAND ----------

# DBTITLE 1, Demo_a_mode
with open("/tmp/mode_a_example.txt", "w") as f:
    f.write("Line 1\n")

with open("/tmp/mode_a_example.txt", "a") as f:
    f.write("Line 2 (appended)\n")

with open("/tmp/mode_a_example.txt", "r") as f:
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **r+** (Read + Write)
# MAGIC - Opens file for **reading and writing**
# MAGIC - **File must exist**
# MAGIC - Does **not** erase content, but writing starts at current pointer

# COMMAND ----------

# DBTITLE 1, Demo_r_plus_mode
with open("/tmp/mode_r_plus_example.txt", "w") as f:
    f.write("ABCDEFG")

with open("/tmp/mode_r_plus_example.txt", "r+") as f:
    f.seek(3)
    f.write("***")
    f.seek(0)
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **w+** (Write + Read)
# MAGIC - Opens file to **write then read**
# MAGIC - **Erases** file before writing
# MAGIC - Pointer starts at beginning

# COMMAND ----------

# DBTITLE 1, Demo_w_plus_mode
with open("/tmp/mode_w_plus_example.txt", "w+") as f:
    f.write("Hello!")
    f.seek(0)
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mode: **a+** (Append + Read)
# MAGIC - Opens file to **read and append**
# MAGIC - Does **not erase** existing content
# MAGIC - Writing always happens **at end**

# COMMAND ----------

# DBTITLE 1, Demo_a_plus_mode
with open("/tmp/mode_a_plus_example.txt", "w") as f:
    f.write("Original Line\n")

with open("/tmp/mode_a_plus_example.txt", "a+") as f:
    f.write("New Appended Line\n")
    f.seek(0)
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC # File Handling — File Read & Write Methods
# MAGIC - `read()` reads whole or part of the file
# MAGIC - `readline()` reads one line
# MAGIC - `readlines()` returns list of lines
# MAGIC - `write()` writes data
# MAGIC - `writelines()` writes list of lines

# COMMAND ----------

# DBTITLE 1,Demo File read & write methods
demo_path = "/tmp/demo_read_write.txt"

with open(demo_path, "w") as f:
    f.write("First line\nSecond line\nThird line\n")

with open(demo_path, "r") as f:
    print("read():", f.read())

with open(demo_path, "r") as f:
    print("readline():", f.readline())

with open(demo_path, "a") as f:
    f.write("Fourth line (appended)\n")

with open(demo_path, "r") as f:
    print("After append:", f.read())

os.remove(demo_path)

# COMMAND ----------

# MAGIC %md
# MAGIC # File Handling — Controlling File Pointer
# MAGIC Use seek() to control the file pointer 
# MAGIC `seek(offset, whence)`
# MAGIC
# MAGIC
# MAGIC `seek()` moves the read/write pointer:
# MAGIC - `seek(0)` → start of file
# MAGIC - `seek(offset, 1)` → relative to current position
# MAGIC - `seek(offset, 2)` → relative to end of the file
# MAGIC - `seek(0, 2)` → end of file

# COMMAND ----------

# MAGIC %md
# MAGIC ## `seek(offset, 0)` — Move Pointer From **Start**
# MAGIC Example: move to 5th character and read from there.

# COMMAND ----------

# DBTITLE 1, Demo_seek_from_start
with open("/tmp/seek_example.txt", "w") as f:
    f.write("ABCDEFGHIJKLMN")

with open("/tmp/seek_example.txt", "r") as f:
    f.seek(5, 0)
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## `seek(offset, 1)` — Move Pointer From **Current Position**

# COMMAND ----------

# DBTITLE 1, Demo_seek_from_current
with open("/tmp/seek_example.txt", "r") as f:
    f.read(5)
    f.seek(2, 1)
    print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC ## `seek(offset, 2)` — Move Pointer From **End of File**

# COMMAND ----------

# DBTITLE 1,*** Demo_seek_from_end in text mode *** will fail
with open("/tmp/seek_example.txt", "r") as f:
    f.seek(-5, 2)
    print(f.read())

# COMMAND ----------

# DBTITLE 1,*** Demo_seek_from_end in binary mode *** will work
with open("/tmp/text.txt", "wb+") as f:
    f.write(b"hello python")
    f.seek(-6, 2)
    print(f.read().decode())

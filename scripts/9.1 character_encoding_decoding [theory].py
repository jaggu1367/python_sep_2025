# Databricks notebook source
# MAGIC %md ### ASCII
# MAGIC
# MAGIC **ASCII** (American Standard Code for Information Interchange) is a character encoding standard for electronic communication. Each character (letters, digits, symbols, and control codes) is assigned a unique number from 0 to 127. ASCII is widely used for representing text in computers and devices.
# MAGIC
# MAGIC <table>
# MAGIC   <thead>
# MAGIC     <tr>
# MAGIC       <th>Dec</th>
# MAGIC       <th>Char</th>
# MAGIC       <th>Description</th>
# MAGIC     </tr>
# MAGIC   </thead>
# MAGIC   <tbody>
# MAGIC     <tr><td>0</td><td>NUL</td><td>Null</td></tr>
# MAGIC     <tr><td>1</td><td>SOH</td><td>Start of Header</td></tr>
# MAGIC     <tr><td>2</td><td>STX</td><td>Start of Text</td></tr>
# MAGIC     <tr><td>3</td><td>ETX</td><td>End of Text</td></tr>
# MAGIC     <tr><td>4</td><td>EOT</td><td>End of Transmission</td></tr>
# MAGIC     <tr><td>5</td><td>ENQ</td><td>Enquiry</td></tr>
# MAGIC     <tr><td>6</td><td>ACK</td><td>Acknowledge</td></tr>
# MAGIC     <tr><td>7</td><td>BEL</td><td>Bell</td></tr>
# MAGIC     <tr><td>8</td><td>BS</td><td>Backspace</td></tr>
# MAGIC     <tr><td>9</td><td>TAB</td><td>Horizontal Tab</td></tr>
# MAGIC     <tr><td>10</td><td>LF</td><td>Line Feed</td></tr>
# MAGIC     <tr><td>11</td><td>VT</td><td>Vertical Tab</td></tr>
# MAGIC     <tr><td>12</td><td>FF</td><td>Form Feed</td></tr>
# MAGIC     <tr><td>13</td><td>CR</td><td>Carriage Return</td></tr>
# MAGIC     <tr><td>14</td><td>SO</td><td>Shift Out</td></tr>
# MAGIC     <tr><td>15</td><td>SI</td><td>Shift In</td></tr>
# MAGIC     <tr><td>16</td><td>DLE</td><td>Data Link Escape</td></tr>
# MAGIC     <tr><td>17</td><td>DC1</td><td>Device Control 1</td></tr>
# MAGIC     <tr><td>18</td><td>DC2</td><td>Device Control 2</td></tr>
# MAGIC     <tr><td>19</td><td>DC3</td><td>Device Control 3</td></tr>
# MAGIC     <tr><td>20</td><td>DC4</td><td>Device Control 4</td></tr>
# MAGIC     <tr><td>21</td><td>NAK</td><td>Negative Acknowledge</td></tr>
# MAGIC     <tr><td>22</td><td>SYN</td><td>Synchronous Idle</td></tr>
# MAGIC     <tr><td>23</td><td>ETB</td><td>End of Transmission Block</td></tr>
# MAGIC     <tr><td>24</td><td>CAN</td><td>Cancel</td></tr>
# MAGIC     <tr><td>25</td><td>EM</td><td>End of Medium</td></tr>
# MAGIC     <tr><td>26</td><td>SUB</td><td>Substitute</td></tr>
# MAGIC     <tr><td>27</td><td>ESC</td><td>Escape</td></tr>
# MAGIC     <tr><td>28</td><td>FS</td><td>File Separator</td></tr>
# MAGIC     <tr><td>29</td><td>GS</td><td>Group Separator</td></tr>
# MAGIC     <tr><td>30</td><td>RS</td><td>Record Separator</td></tr>
# MAGIC     <tr><td>31</td><td>US</td><td>Unit Separator</td></tr>
# MAGIC     <tr><td>32</td><td>(space)</td><td>Space</td></tr>
# MAGIC     <tr><td>33</td><td>!</td><td>Exclamation mark</td></tr>
# MAGIC     <tr><td>34</td><td>"</td><td>Double quote</td></tr>
# MAGIC     <tr><td>35</td><td>#</td><td>Number sign</td></tr>
# MAGIC     <tr><td>36</td><td>$</td><td>Dollar sign</td></tr>
# MAGIC     <tr><td>37</td><td>%</td><td>Percent</td></tr>
# MAGIC     <tr><td>38</td><td>&</td><td>Ampersand</td></tr>
# MAGIC     <tr><td>39</td><td>'</td><td>Single quote</td></tr>
# MAGIC     <tr><td>40</td><td>(</td><td>Left parenthesis</td></tr>
# MAGIC     <tr><td>41</td><td>)</td><td>Right parenthesis</td></tr>
# MAGIC     <tr><td>42</td><td>*</td><td>Asterisk</td></tr>
# MAGIC     <tr><td>43</td><td>+</td><td>Plus sign</td></tr>
# MAGIC     <tr><td>44</td><td>,</td><td>Comma</td></tr>
# MAGIC     <tr><td>45</td><td>-</td><td>Hyphen</td></tr>
# MAGIC     <tr><td>46</td><td>.</td><td>Period</td></tr>
# MAGIC     <tr><td>47</td><td>/</td><td>Slash</td></tr>
# MAGIC     <tr><td>48</td><td>0</td><td>Digit zero</td></tr>
# MAGIC     <tr><td>49</td><td>1</td><td>Digit one</td></tr>
# MAGIC     <tr><td>50</td><td>2</td><td>Digit two</td></tr>
# MAGIC     <tr><td>51</td><td>3</td><td>Digit three</td></tr>
# MAGIC     <tr><td>52</td><td>4</td><td>Digit four</td></tr>
# MAGIC     <tr><td>53</td><td>5</td><td>Digit five</td></tr>
# MAGIC     <tr><td>54</td><td>6</td><td>Digit six</td></tr>
# MAGIC     <tr><td>55</td><td>7</td><td>Digit seven</td></tr>
# MAGIC     <tr><td>56</td><td>8</td><td>Digit eight</td></tr>
# MAGIC     <tr><td>57</td><td>9</td><td>Digit nine</td></tr>
# MAGIC     <tr><td>58</td><td>:</td><td>Colon</td></tr>
# MAGIC     <tr><td>59</td><td>;</td><td>Semicolon</td></tr>
# MAGIC     <tr><td>60</td><td>&lt;</td><td>Less than</td></tr>
# MAGIC     <tr><td>61</td><td>=</td><td>Equals</td></tr>
# MAGIC     <tr><td>62</td><td>&gt;</td><td>Greater than</td></tr>
# MAGIC     <tr><td>63</td><td>?</td><td>Question mark</td></tr>
# MAGIC     <tr><td>64</td><td>@</td><td>At sign</td></tr>
# MAGIC     <tr><td>65</td><td>A</td><td>Uppercase A</td></tr>
# MAGIC     <tr><td>66</td><td>B</td><td>Uppercase B</td></tr>
# MAGIC     <tr><td>67</td><td>C</td><td>Uppercase C</td></tr>
# MAGIC     <tr><td>68</td><td>D</td><td>Uppercase D</td></tr>
# MAGIC     <tr><td>69</td><td>E</td><td>Uppercase E</td></tr>
# MAGIC     <tr><td>70</td><td>F</td><td>Uppercase F</td></tr>
# MAGIC     <tr><td>71</td><td>G</td><td>Uppercase G</td></tr>
# MAGIC     <tr><td>72</td><td>H</td><td>Uppercase H</td></tr>
# MAGIC     <tr><td>73</td><td>I</td><td>Uppercase I</td></tr>
# MAGIC     <tr><td>74</td><td>J</td><td>Uppercase J</td></tr>
# MAGIC     <tr><td>75</td><td>K</td><td>Uppercase K</td></tr>
# MAGIC     <tr><td>76</td><td>L</td><td>Uppercase L</td></tr>
# MAGIC     <tr><td>77</td><td>M</td><td>Uppercase M</td></tr>
# MAGIC     <tr><td>78</td><td>N</td><td>Uppercase N</td></tr>
# MAGIC     <tr><td>79</td><td>O</td><td>Uppercase O</td></tr>
# MAGIC     <tr><td>80</td><td>P</td><td>Uppercase P</td></tr>
# MAGIC     <tr><td>81</td><td>Q</td><td>Uppercase Q</td></tr>
# MAGIC     <tr><td>82</td><td>R</td><td>Uppercase R</td></tr>
# MAGIC     <tr><td>83</td><td>S</td><td>Uppercase S</td></tr>
# MAGIC     <tr><td>84</td><td>T</td><td>Uppercase T</td></tr>
# MAGIC     <tr><td>85</td><td>U</td><td>Uppercase U</td></tr>
# MAGIC     <tr><td>86</td><td>V</td><td>Uppercase V</td></tr>
# MAGIC     <tr><td>87</td><td>W</td><td>Uppercase W</td></tr>
# MAGIC     <tr><td>88</td><td>X</td><td>Uppercase X</td></tr>
# MAGIC     <tr><td>89</td><td>Y</td><td>Uppercase Y</td></tr>
# MAGIC     <tr><td>90</td><td>Z</td><td>Uppercase Z</td></tr>
# MAGIC     <tr><td>91</td><td>[</td><td>Left bracket</td></tr>
# MAGIC     <tr><td>92</td><td>\</td><td>Backslash</td></tr>
# MAGIC     <tr><td>93</td><td>]</td><td>Right bracket</td></tr>
# MAGIC     <tr><td>94</td><td>^</td><td>Caret</td></tr>
# MAGIC     <tr><td>95</td><td>_</td><td>Underscore</td></tr>
# MAGIC     <tr><td>96</td><td>`</td><td>Grave accent</td></tr>
# MAGIC     <tr><td>97</td><td>a</td><td>Lowercase a</td></tr>
# MAGIC     <tr><td>98</td><td>b</td><td>Lowercase b</td></tr>
# MAGIC     <tr><td>99</td><td>c</td><td>Lowercase c</td></tr>
# MAGIC     <tr><td>100</td><td>d</td><td>Lowercase d</td></tr>
# MAGIC     <tr><td>101</td><td>e</td><td>Lowercase e</td></tr>
# MAGIC     <tr><td>102</td><td>f</td><td>Lowercase f</td></tr>
# MAGIC     <tr><td>103</td><td>g</td><td>Lowercase g</td></tr>
# MAGIC     <tr><td>104</td><td>h</td><td>Lowercase h</td></tr>
# MAGIC     <tr><td>105</td><td>i</td><td>Lowercase i</td></tr>
# MAGIC     <tr><td>106</td><td>j</td><td>Lowercase j</td></tr>
# MAGIC     <tr><td>107</td><td>k</td><td>Lowercase k</td></tr>
# MAGIC     <tr><td>108</td><td>l</td><td>Lowercase l</td></tr>
# MAGIC     <tr><td>109</td><td>m</td><td>Lowercase m</td></tr>
# MAGIC     <tr><td>110</td><td>n</td><td>Lowercase n</td></tr>
# MAGIC     <tr><td>111</td><td>o</td><td>Lowercase o</td></tr>
# MAGIC     <tr><td>112</td><td>p</td><td>Lowercase p</td></tr>
# MAGIC     <tr><td>113</td><td>q</td><td>Lowercase q</td></tr>
# MAGIC     <tr><td>114</td><td>r</td><td>Lowercase r</td></tr>
# MAGIC     <tr><td>115</td><td>s</td><td>Lowercase s</td></tr>
# MAGIC     <tr><td>116</td><td>t</td><td>Lowercase t</td></tr>
# MAGIC     <tr><td>117</td><td>u</td><td>Lowercase u</td></tr>
# MAGIC     <tr><td>118</td><td>v</td><td>Lowercase v</td></tr>
# MAGIC     <tr><td>119</td><td>w</td><td>Lowercase w</td></tr>
# MAGIC     <tr><td>120</td><td>x</td><td>Lowercase x</td></tr>
# MAGIC     <tr><td>121</td><td>y</td><td>Lowercase y</td></tr>
# MAGIC     <tr><td>122</td><td>z</td><td>Lowercase z</td></tr>
# MAGIC     <tr><td>123</td><td>{</td><td>Left brace</td></tr>
# MAGIC     <tr><td>124</td><td>|</td><td>Vertical bar</td></tr>
# MAGIC     <tr><td>125</td><td>}</td><td>Right brace</td></tr>
# MAGIC     <tr><td>126</td><td>~</td><td>Tilde</td></tr>
# MAGIC     <tr><td>127</td><td>DEL</td><td>Delete</td></tr>
# MAGIC   </tbody>
# MAGIC </table>

# COMMAND ----------

# MAGIC %md
# MAGIC # Character Encoding in Python
# MAGIC In this notebook, we'll explore **Character Encoding** — how text is represented as bytes in computers.
# MAGIC
# MAGIC We'll cover:
# MAGIC 1. What is Encoding  
# MAGIC 2. What is Decoding  
# MAGIC 3. Types of Encodings available  
# MAGIC 4. Common Encodings used in Python  
# MAGIC 5. Examples of Encoding and Decoding in different formats

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. What is Encoding?
# MAGIC **Encoding** is the process of converting a string (sequence of characters) into bytes.
# MAGIC
# MAGIC Computers store and transmit text as bytes — numbers representing each character based on a particular encoding standard.
# MAGIC
# MAGIC For example:
# MAGIC - 'A' in ASCII = 65  
# MAGIC - 'A' in UTF-8 = 0x41  
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC encoded_bytes = text.encode(encoding_type)
# MAGIC ```
# MAGIC
# MAGIC **Common encodings:** `'utf-8'`, `'ascii'`, `'utf-16'`, `'cp1252'`

# COMMAND ----------

# DBTITLE 1,Example: Encoding a String into Bytes
text = "Hello, Python!"
encoded_utf8 = text.encode('utf-8')
encoded_ascii = text.encode('ascii')

print("Original text:", text)
print("UTF-8 encoded:", encoded_utf8)
print("ASCII encoded:", encoded_ascii)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. What is Decoding?
# MAGIC **Decoding** is the reverse process of encoding — converting bytes back into a human-readable string.
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC decoded_text = byte_data.decode(encoding_type)
# MAGIC ```
# MAGIC
# MAGIC It is important to use the **same encoding** for decoding that was used for encoding.  
# MAGIC Otherwise, you'll get errors or incorrect characters.

# COMMAND ----------

# DBTITLE 1,Example: Decoding Bytes Back to String
byte_data = b'Hello, Python!'
decoded_text = byte_data.decode('utf-8')

print("Byte data:", byte_data)
print("Decoded text:", decoded_text)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Types of Encodings
# MAGIC There are many encoding standards. Here are some key ones:
# MAGIC
# MAGIC | Encoding | Description | Character Support | Bytes per Character |
# MAGIC |-----------|--------------|-------------------|---------------------|
# MAGIC | ASCII | American Standard Code for Information Interchange | English letters and symbols only | 1 |
# MAGIC | UTF-8 | Universal text format (Unicode) | All characters worldwide | 1–4 |
# MAGIC | UTF-16 | Unicode encoding (2 or 4 bytes) | All characters worldwide | 2–4 |
# MAGIC | UTF-32 | Fixed-length Unicode encoding | All characters worldwide | 4 |
# MAGIC | CP1252 | Windows Latin encoding | Western European languages | 1 |
# MAGIC
# MAGIC Python’s **default encoding** (in most systems) is **UTF-8**.

# COMMAND ----------

# DBTITLE 1,Example: Encoding the Same Text in Different Formats
text = "Python 🐍"

utf8_bytes = text.encode('utf-8')
utf16_bytes = text.encode('utf-16')
utf32_bytes = text.encode('utf-32')

print("Original text:", text)
print("UTF-8  :", utf8_bytes)
print("UTF-16 :", utf16_bytes)
print("UTF-32 :", utf32_bytes)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Common Encodings in Python
# MAGIC Python supports hundreds of encodings, but these are the most commonly used:
# MAGIC - `'utf-8'` (default)
# MAGIC - `'utf-16'`
# MAGIC - `'utf-32'`
# MAGIC - `'ascii'`
# MAGIC - `'cp1252'`
# MAGIC
# MAGIC You can list all supported encodings using the `encodings` module.

# COMMAND ----------

# DBTITLE 1,Example: Listing Some Common Encodings
import encodings

common_encodings = ['utf-8', 'utf-16', 'utf-32', 'ascii', 'cp1252']
for enc in common_encodings:
    print(f"{enc:<8} → Example: {'A'.encode(enc)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Encoding and Decoding a File
# MAGIC When working with files, always specify the encoding to ensure consistency.
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC with open(filename, "w", encoding="utf-8") as f:
# MAGIC     f.write(text)
# MAGIC
# MAGIC with open(filename, "r", encoding="utf-8") as f:
# MAGIC     data = f.read()
# MAGIC ```
# MAGIC
# MAGIC If you use the wrong encoding while reading, you might see garbled text or get `UnicodeDecodeError`.

# COMMAND ----------

# DBTITLE 1,Example: Writing and Reading File with Encoding
file_path = "/tmp/encoding_demo.txt"
text = "Hello, world! नमस्ते 🌍"

# Write with UTF-8 encoding
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

# Read back correctly
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("File content read successfully:", content)

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Summary
# MAGIC - **Encoding** → Convert string → bytes  
# MAGIC - **Decoding** → Convert bytes → string  
# MAGIC - Always use the same encoding for both operations  
# MAGIC - Most common encoding today: **UTF-8**  
# MAGIC - Python supports many encodings via the `encodings` module
# MAGIC
# MAGIC 🧠 **Tip:** Prefer UTF-8 for new projects to ensure global compatibility.

# 0x04-utf8_validation

concepts and resources that will be helpful:

Concepts Needed:
Bitwise Operations in Python:

Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
Python Bitwise Operators
UTF-8 Encoding Scheme:

Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
Understanding the patterns that represent a valid UTF-8 encoded character.
UTF-8 Wikipedia
Characters, Symbols, and the Unicode Miracle
The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets
Data Representation:

How to represent and work with data at the byte level.
Handling the least significant bits (LSB) of integers to simulate byte data.
List Manipulation in Python:

Iterating through lists, accessing list elements, and understanding list comprehensions.
Python Lists
Boolean Logic:

Applying logical operations to make decisions within the program.
By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

Additional Resource
Mock Technical Interview

Tasks
0. UTF-8 Validation
mandatory
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
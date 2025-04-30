# Python Basics by Saheer Azmi
# Topics: Comments, Escape Sequences, end and sep parameters

# -------------------
# Single-line Comment Example
# This is a single-line comment explaining the next line
print("Hello Saheer Azmi!")  # Printing a welcome message

# -------------------
# Multi-line Comment Example
"""
This is a multi-line comment.
It can span multiple lines.
It is written between triple quotes.
"""
print("Learning Python with Saheer Azmi!")  # Printing learning message

# -------------------
# Escape Sequences Examples
print("Escape Sequences Demonstration:")

print("First Line\nSecond Line")     # \n inserts a new line
print("Column1\tColumn2")             # \t inserts a tab space
print("Saheer said: \"Python is fun!\"")  # \" allows double quotes inside string
print("This is a backslash: \\")      # \\ prints a single backslash

# -------------------
# Using 'end' parameter in print()
print("This is the first part", end=" -- ")
print("and this is the second part.", end=" **END\n")
# end=" --> " joins first and second print on the same line with an arrow

# -------------------
# Using 'sep' parameter in print()
print("Python", "Java", "C++", sep=" | ")  # separates words with |
print("2025", "04", "30", sep="/")          # formats date like 2025/04/30
print("Saheer", "Azmi", sep=" - ")          # prints name with hyphen
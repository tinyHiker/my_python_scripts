import re

text = "Lesson12"

# Regular expression for finding integers
pattern = r"\d+"

# Find all occurrences of the pattern
numbers = re.findall(pattern, text)

print(numbers)  # ['3', '5', '10']
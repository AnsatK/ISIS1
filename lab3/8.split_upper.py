import re

test_string = "MyNameIsAnsat"

reg = r"([A-Z][^A-Z]*)"

m = re.split(reg, test_string)
print(m)
print(test_string)
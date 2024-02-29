import re

test_string = "MyNameIsAnsat"

reg = r"([a-z])([A-Z])"
m = re.sub(reg, r'\1_\2', test_string)
m.lower()
print(m)
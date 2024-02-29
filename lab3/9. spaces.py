import re

test_string = "MyNameIsAnsat"

reg = r"([a-z])([A-Z])"
m = re.sub(reg, r'\1 \2', test_string)

print(m)
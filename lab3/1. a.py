import re

test_string="Hi how a re you abbbb"

reg = r"ab*"
m = re.search(reg, test_string)
print(m)



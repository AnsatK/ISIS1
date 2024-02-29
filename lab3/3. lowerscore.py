import re

test_string = "AAAAAAjqwpod_sds"

reg = r"(.)*([a-z]+)(_+)([a-z]+)"

m = re.match(reg, test_string)
print(m)
import re

test_string = "AA AAAj.wp......."

reg = r"([\s+ \.+ \,+]+)"

m = re.sub(reg, ":", test_string)
print(m)

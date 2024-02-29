import re

test_string = "sdwesadsafdfafdb"

reg = r"(.)*(a)*(.)(b$)"

m = re.match(reg, test_string)
print(m)
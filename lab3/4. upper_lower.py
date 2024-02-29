import re

test_string = "AAAAA_qwaApod_sds"

reg = r"(.)*([A-Z]+)([a-z]+)"

m = re.match(reg, test_string)
print(m)
import re

test_string = "Hello_everyone_how_are_you_doing"

reg = r"(_[a-zA-Z])"

m = re.sub(reg, lambda r: r.group(0).upper(), test_string)
m = re.sub(r"(\b[a-zA-Z])", lambda r: r.group(0).lower(), m)
m = re.sub(r"(_*)", "", m)
print(m)
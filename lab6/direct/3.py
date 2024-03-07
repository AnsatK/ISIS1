import os

def isPath(path):
    if not os.path.exists(path):
        return f"Path '{path}' does not exist."
    d, f = os.path.split(path)


    return f"Path exists Directory: {d} Filename: {f}"
print(isPath(r"lab6\2.py"))
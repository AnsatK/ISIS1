import os
def isPath(path):
    if not os.path.exists(path):
        return f"Path '{path}' does not exist."
    else: 
        return f"Path '{path}' exist"
p = "new.txt"
isPath(p)
os.remove(p)



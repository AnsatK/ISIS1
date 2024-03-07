import os

def path_access(path):
    if not os.path.exists(path):
        return f"Path '{path}' does not exist."

    if not os.access(path, os.R_OK):
        return f"No read access to '{path}'."
    
    if not os.access(path, os.W_OK):
        return f"No write access to '{path}'."

    if os.name == 'posix' and not os.access(path, os.X_OK):
        return f"No execute access to '{path}'."

    return f"'{path}' is accessible."

p = r'lab6\2.py'
print(path_access(p))
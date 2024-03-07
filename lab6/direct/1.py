import os
def dir_file_list(path):
    try:
        con = os.listdir(path)
    except FileNotFoundError:
        return f"Error: Path '{path}' not found."

    dirs = [i for i in con if os.path.isdir(os.path.join(path, i))]
    files = [i for i in con if os.path.isfile(os.path.join(path, i))]
    
    print("files:")
    for f in files:
        print(f"{f}")
    print("directories:")
    for d in dirs:
        print(f"{d}")
    print("files and dirs")
    for c in con:
        print(f"{c}")
p = r'C:\Users\Admin\OneDrive\Рабочий стол\pp2'
dir_file_list(p)

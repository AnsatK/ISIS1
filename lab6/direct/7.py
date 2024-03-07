with open("sa.txt", "r") as file:
    txt = file.read()
with open("new.txt", "w") as file:
    file.write(txt)
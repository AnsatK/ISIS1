#1
x = "Hello World"
print(len(x))
#2
txt = "Hello World"
x = txt[1]
print(x)
#3
txt = "Hello World"
x = txt[2:5]
print(x)
#4
txt = " Hello World "
x = x.strip()
print(x)
#5
txt = "Hello World "
x = txt.upper()
print(x)
#6
txt = "Hello World "
x = txt.lower()
print(x)
#7 
txt = "Hello World"
txt = txt.replace("H", "J")
#8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

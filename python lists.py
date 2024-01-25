#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2
fruits[0] = "kiwi"
print(fruits)

#3
fruits.append("orange")
print(fruits)

#4
fruits.insert(1, "lemon")
print(fruits)

#5
fruits.remove("banana")

#6
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8
print(len(fruits))